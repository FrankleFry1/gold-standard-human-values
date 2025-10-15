"""
Charter Parser - Fetches and parses the Gold Standard Human Values framework
from GitHub repository to create structured ethical knowledge base

This module automatically fetches the latest version of the framework from
the GitHub repository and parses it into a structured format for use by
the ethics engine.
"""

import re
import json
import os
import requests
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict


@dataclass
class Pillar:
    """Represents one ethical pillar"""
    name: str
    article: str  # e.g., "Article I"
    principles: List[str]
    commitments: List[str]
    rationale: str


@dataclass
class TensionGuidance:
    """Guidance for navigating tensions between pillars"""
    tension_pair: str  # e.g., "Curiosity vs. Empathy"
    description: str
    guidance: List[str]
    example: Optional[str] = None


@dataclass
class CaseStudy:
    """A case study showing framework application"""
    title: str
    scenario: str
    pillar_analysis: Dict[str, str]  # Pillar name -> analysis
    tensions: List[str]
    resolution: str


@dataclass
class CharterKnowledge:
    """Complete parsed knowledge from the GitHub repo"""
    pillars: Dict[str, Pillar]
    tension_guidance: List[TensionGuidance]
    case_studies: List[CaseStudy]
    existential_safeguards: List[str]
    never_compromise: List[str]
    metadata: Dict


class CharterParser:
    """
    Parses the Gold Standard Human Values GitHub repository
    to extract structured ethical knowledge
    """
    
    BASE_URL = "https://raw.githubusercontent.com/FrankleFry1/gold-standard-human-values/main/"
    
    def __init__(self, cache_path: str = None):
        """
        Initialize parser
        
        Args:
            cache_path: Path to save/load cached parsed data (default: ./charter_cache.json)
        """
        self.cache_path = cache_path or os.path.join(os.getcwd(), "charter_cache.json")
        self.knowledge: Optional[CharterKnowledge] = None
    
    def fetch_and_parse(self, force_refresh: bool = False) -> CharterKnowledge:
        """
        Fetch and parse the entire repository
        
        Args:
            force_refresh: If True, ignore cache and fetch fresh
            
        Returns:
            CharterKnowledge object with all parsed data
        """
        # Try to load from cache first
        if not force_refresh and self.knowledge is None:
            cached = self._load_cache()
            if cached:
                print("Loaded charter knowledge from cache")
                self.knowledge = cached
                return self.knowledge
        
        print("Fetching charter from GitHub...")
        
        # Fetch all documents
        charter_md = self._fetch_file("CHARTER.md")
        readme_md = self._fetch_file("README.md")
        
        # Fetch all three case study files
        case_studies_text = ""
        case_study_files = [
            "examples/Case Studies/CASE_STUDIES_1.md",
            "examples/Case Studies/CASE_STUDIES_2.md",
            "examples/Case Studies/CASE_STUDIES_3.md"
        ]
        
        for path in case_study_files:
            content = self._fetch_file(path)
            if content:
                print(f"✓ Fetched: {path}")
                case_studies_text += "\n\n" + content
        
        if not case_studies_text:
            print("Warning: No case studies found")
        
        # Parse components
        pillars = self._parse_charter_pillars(charter_md)
        tension_guidance = self._parse_tension_guidance(charter_md)
        existential_rules = self._parse_existential_rules(charter_md)
        case_studies = self._parse_case_studies(case_studies_text) if case_studies_text else []
        
        # Create knowledge object
        self.knowledge = CharterKnowledge(
            pillars=pillars,
            tension_guidance=tension_guidance,
            case_studies=case_studies,
            existential_safeguards=existential_rules["safeguards"],
            never_compromise=existential_rules["never_compromise"],
            metadata={
                "source": "https://github.com/FrankleFry1/gold-standard-human-values",
                "version": "1.0",
                "last_updated": "2025-10-15"
            }
        )
        
        # Save to cache
        self._save_cache()
        
        print(f"Successfully parsed charter: {len(pillars)} pillars, {len(case_studies)} case studies")
        
        return self.knowledge
    
    def _fetch_file(self, filepath: str) -> str:
        """Fetch a file from GitHub"""
        url = self.BASE_URL + filepath
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Warning: Could not fetch {filepath}: {e}")
            return ""
    
    def _parse_charter_pillars(self, charter_text: str) -> Dict[str, Pillar]:
        """Parse the six pillars from CHARTER.md"""
        pillars = {}
        
        # Define the six pillars and their article numbers
        pillar_definitions = [
            ("Article I", "Curiosity and Truth-Seeking"),
            ("Article II", "Empathy and Mutual Flourishing"),
            ("Article III", "Dignity and Agency"),
            ("Article IV", "Sustainability and Long-Term Stewardship"),
            ("Article V", "Adaptability and Diversity"),
            ("Article VI", "Integrity and Responsibility")
        ]
        
        for article, pillar_name in pillar_definitions:
            pillar_data = self._extract_pillar_section(charter_text, article, pillar_name)
            if pillar_data:
                pillars[pillar_name] = pillar_data
        
        return pillars
    
    def _extract_pillar_section(self, text: str, article: str, pillar_name: str) -> Optional[Pillar]:
        """Extract a single pillar's data from charter text"""
        # Find the article section
        article_pattern = rf"{article}[:\s]+{re.escape(pillar_name)}(.*?)(?=Article [IVX]+|$)"
        match = re.search(article_pattern, text, re.DOTALL | re.IGNORECASE)
        
        if not match:
            # Fallback: use hardcoded principles
            return self._get_fallback_pillar(pillar_name)
        
        section_text = match.group(1)
        
        # Extract principles (look for numbered lists or bullet points)
        principles = self._extract_list_items(section_text, ["Principles", "We commit to"])
        commitments = self._extract_list_items(section_text, ["Commitments", "We commit to"])
        
        # Extract rationale (usually in a "Rationale" or "Why this matters" section)
        rationale_match = re.search(r"(?:Rationale|Why this matters)[:\s]+(.*?)(?=\n##|\n#|$)", 
                                    section_text, re.DOTALL | re.IGNORECASE)
        rationale = rationale_match.group(1).strip() if rationale_match else ""
        
        return Pillar(
            name=pillar_name,
            article=article,
            principles=principles or self._get_fallback_principles(pillar_name),
            commitments=commitments or [],
            rationale=rationale
        )
    
    def _extract_list_items(self, text: str, section_markers: List[str]) -> List[str]:
        """Extract bullet points or numbered items from a section"""
        items = []
        
        # Find the section
        for marker in section_markers:
            pattern = rf"{marker}[:\s]+(.*?)(?=\n##|\n#|$)"
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            
            if match:
                section = match.group(1)
                
                # Extract items (support both - bullets and 1. numbered)
                item_pattern = r"(?:^|\n)\s*(?:[-*]|\d+\.)\s+(.+?)(?=\n\s*(?:[-*]|\d+\.)|$)"
                items = re.findall(item_pattern, section, re.MULTILINE)
                items = [item.strip() for item in items if item.strip()]
                
                if items:
                    break
        
        return items
    
    def _parse_tension_guidance(self, charter_text: str) -> List[TensionGuidance]:
        """Parse Article VII tension navigation guidance"""
        guidance_list = []
        
        # Find Article VII section
        article7_pattern = r"Article VII[:\s]+.*?Navigating.*?Tensions(.*?)(?=Article [IVX]+|$)"
        match = re.search(article7_pattern, charter_text, re.DOTALL | re.IGNORECASE)
        
        if not match:
            return self._get_fallback_tensions()
        
        section_text = match.group(1)
        
        # Look for common tension patterns
        tension_patterns = [
            "Curiosity vs. Empathy",
            "Sustainability vs. Present Well-Being",
            "Dignity/Agency vs. Collective Flourishing",
            "Truth vs. Harm Prevention",
            "Individual Freedom vs. Social Good"
        ]
        
        for tension in tension_patterns:
            # Try to find guidance for this tension
            tension_pattern = rf"{re.escape(tension)}[:\s]+(.*?)(?=\n##|(?:Curiosity|Sustainability|Dignity)|$)"
            tension_match = re.search(tension_pattern, section_text, re.DOTALL | re.IGNORECASE)
            
            if tension_match:
                guidance_text = tension_match.group(1).strip()
                guidance_points = self._extract_list_items(guidance_text, ["Guidance", "Approach", "Consider"])
                
                guidance_list.append(TensionGuidance(
                    tension_pair=tension,
                    description=guidance_text[:200] + "..." if len(guidance_text) > 200 else guidance_text,
                    guidance=guidance_points if guidance_points else [guidance_text],
                    example=None
                ))
        
        return guidance_list if guidance_list else self._get_fallback_tensions()
    
    def _parse_existential_rules(self, charter_text: str) -> Dict[str, List[str]]:
        """Parse existential compromise rules from Article VII"""
        # Look for safeguards section
        safeguards_pattern = r"(?:Seven Safeguards|Safeguards for Emergency)(.*?)(?=\n##|What Can Never|$)"
        safeguards_match = re.search(safeguards_pattern, charter_text, re.DOTALL | re.IGNORECASE)
        
        safeguards = []
        if safeguards_match:
            safeguards = self._extract_list_items(safeguards_match.group(1), [""])
        else:
            safeguards = [
                "Proportionality: Response must be proportional to threat",
                "Temporality: Deviations must be time-limited",
                "Democratic authorization: Require broad democratic consent",
                "Oversight: Independent monitoring required",
                "Transparency: Document and justify all deviations",
                "Sunset clauses: Automatic expiration of emergency measures",
                "Moral residue: Acknowledge the cost of compromise"
            ]
        
        # Look for never compromise section
        never_pattern = r"(?:What Can Never Be Compromised|Never Compromise)(.*?)(?=\n##|$)"
        never_match = re.search(never_pattern, charter_text, re.DOTALL | re.IGNORECASE)
        
        never_compromise = []
        if never_match:
            never_compromise = self._extract_list_items(never_match.group(1), [""])
        else:
            never_compromise = [
                "Prohibition of torture and genocide",
                "Fundamental equality of human worth",
                "Right to challenge authority",
                "Core democratic processes"
            ]
        
        return {
            "safeguards": safeguards,
            "never_compromise": never_compromise
        }
    
    def _parse_case_studies(self, case_studies_text: str) -> List[CaseStudy]:
        """Parse case studies from case study markdown files"""
        if not case_studies_text:
            return []
        
        case_studies = []
        
        # Split by case study headers (look for # Case Study pattern)
        case_pattern = r"#\s+Case Study\s+\d+:(.*?)(?=#\s+Case Study\s+\d+:|$)"
        matches = re.finditer(case_pattern, case_studies_text, re.DOTALL | re.IGNORECASE)
        
        for match in matches:
            case_text = match.group(1)
            
            # Extract title (first line)
            title_match = re.search(r"^(.+?)(?=\n)", case_text)
            title = title_match.group(1).strip() if title_match else "Untitled Case"
            
            # Extract scenario
            scenario_match = re.search(r"(?:Scenario|Context)[:\s]+(.*?)(?=\n##|Pillar Analysis|$)", 
                                       case_text, re.DOTALL | re.IGNORECASE)
            scenario = scenario_match.group(1).strip() if scenario_match else ""
            
            # Extract pillar analysis
            pillar_analysis = {}
            for pillar_name in ["Curiosity", "Empathy", "Dignity", "Sustainability", "Adaptability", "Integrity"]:
                analysis_match = re.search(rf"{pillar_name}[:\s]+(.*?)(?=\n-|$)", 
                                          case_text, re.DOTALL | re.IGNORECASE)
                if analysis_match:
                    pillar_analysis[pillar_name] = analysis_match.group(1).strip()
            
            # Extract resolution
            resolution_match = re.search(r"(?:Resolution|Recommendation)[:\s]+(.*?)(?=\n##|$)", 
                                        case_text, re.DOTALL | re.IGNORECASE)
            resolution = resolution_match.group(1).strip() if resolution_match else ""
            
            if scenario or pillar_analysis:
                case_studies.append(CaseStudy(
                    title=title,
                    scenario=scenario,
                    pillar_analysis=pillar_analysis,
                    tensions=[],  # Could extract tensions if marked
                    resolution=resolution
                ))
        
        return case_studies
    
    def _get_fallback_pillar(self, pillar_name: str) -> Pillar:
        """Return hardcoded pillar if parsing fails"""
        principles = self._get_fallback_principles(pillar_name)
        return Pillar(
            name=pillar_name,
            article="",
            principles=principles,
            commitments=[],
            rationale="Fallback definition"
        )
    
    def _get_fallback_principles(self, pillar_name: str) -> List[str]:
        """Hardcoded fallback principles"""
        fallbacks = {
            "Curiosity and Truth-Seeking": [
                "Pursue truth through evidence-based reasoning",
                "Practice intellectual humility and acknowledge uncertainty",
                "Respect diverse paths to meaning and understanding",
                "Reject deliberate deception or misinformation",
                "Foster open inquiry and critical thinking"
            ],
            "Empathy and Mutual Flourishing": [
                "Minimize suffering and expand moral consideration",
                "Balance individual rights with collective well-being",
                "Consider impacts on vulnerable populations",
                "Promote equity and address systemic harms",
                "Foster conditions for human and ecological flourishing"
            ],
            "Dignity and Agency": [
                "Respect inherent human worth regardless of capability",
                "Preserve and enhance human autonomy",
                "Enable meaningful participation in governance",
                "Ensure accountability for actions",
                "Protect privacy and informed consent"
            ],
            "Sustainability and Long-Term Stewardship": [
                "Consider long-term and intergenerational impacts",
                "Maintain ecological balance and biodiversity",
                "Ensure AI alignment with human values over time",
                "Plan for systemic resilience and adaptation",
                "Avoid irreversible harms to future generations"
            ],
            "Adaptability and Diversity": [
                "Respect cultural pluralism and diverse values",
                "Allow for moral evolution based on evidence",
                "Build resilience through diversity of approaches",
                "Avoid rigid universalism or moral imperialism",
                "Adapt to changing contexts while preserving core values"
            ],
            "Integrity and Responsibility": [
                "Align words and actions consistently",
                "Exercise moral courage in difficult situations",
                "Maintain robust accountability systems",
                "Repair harm when ethical failures occur",
                "Resist corruption of values under pressure"
            ]
        }
        return fallbacks.get(pillar_name, ["Principle not found"])
    
    def _get_fallback_tensions(self) -> List[TensionGuidance]:
        """Hardcoded fallback tension guidance"""
        return [
            TensionGuidance(
                tension_pair="Curiosity vs. Empathy",
                description="When truth-seeking may cause harm",
                guidance=[
                    "Assess the severity and likelihood of harm",
                    "Consider whether information serves the public good",
                    "Explore ways to pursue truth while minimizing harm"
                ]
            ),
            TensionGuidance(
                tension_pair="Sustainability vs. Present Well-Being",
                description="When long-term survival requires present sacrifice",
                guidance=[
                    "Ensure burdens are distributed equitably",
                    "Maintain democratic legitimacy for sacrifices",
                    "Preserve core dignity even during hardship"
                ]
            )
        ]
    
    def _save_cache(self):
        """Save parsed knowledge to cache file"""
        if not self.knowledge:
            return
        
        try:
            cache_data = {
                "pillars": {name: asdict(pillar) for name, pillar in self.knowledge.pillars.items()},
                "tension_guidance": [asdict(t) for t in self.knowledge.tension_guidance],
                "case_studies": [asdict(cs) for cs in self.knowledge.case_studies],
                "existential_safeguards": self.knowledge.existential_safeguards,
                "never_compromise": self.knowledge.never_compromise,
                "metadata": self.knowledge.metadata
            }
            
            with open(self.cache_path, 'w') as f:
                json.dump(cache_data, f, indent=2)
            
            print(f"Saved charter cache to {self.cache_path}")
            
        except Exception as e:
            print(f"Warning: Could not save cache: {e}")
    
    def _load_cache(self) -> Optional[CharterKnowledge]:
        """Load parsed knowledge from cache file"""
        try:
            with open(self.cache_path, 'r') as f:
                cache_data = json.load(f)
            
            # Reconstruct objects from dictionaries
            pillars = {name: Pillar(**data) for name, data in cache_data["pillars"].items()}
            tension_guidance = [TensionGuidance(**t) for t in cache_data["tension_guidance"]]
            case_studies = [CaseStudy(**cs) for cs in cache_data["case_studies"]]
            
            return CharterKnowledge(
                pillars=pillars,
                tension_guidance=tension_guidance,
                case_studies=case_studies,
                existential_safeguards=cache_data["existential_safeguards"],
                never_compromise=cache_data["never_compromise"],
                metadata=cache_data["metadata"]
            )
            
        except Exception as e:
            print(f"Could not load cache: {e}")
            return None


# Example usage and testing
if __name__ == "__main__":
    parser = CharterParser()
    
    # Force refresh to fetch from GitHub
    knowledge = parser.fetch_and_parse(force_refresh=True)
    
    print("\n" + "="*60)
    print("Charter Knowledge Parsed Successfully")
    print("="*60)
    
    print(f"\nPillars: {len(knowledge.pillars)}")
    for name, pillar in knowledge.pillars.items():
        print(f"\n  {pillar.article}: {name}")
        print(f"    Principles: {len(pillar.principles)}")
        if pillar.principles:
            print(f"      - {pillar.principles[0][:60]}...")
    
    print(f"\nTension Guidance: {len(knowledge.tension_guidance)} scenarios")
    for tension in knowledge.tension_guidance:
        print(f"  - {tension.tension_pair}")
    
    print(f"\nCase Studies: {len(knowledge.case_studies)}")
    for study in knowledge.case_studies:
        print(f"  - {study.title}")
    
    print(f"\nExistential Safeguards: {len(knowledge.existential_safeguards)}")
    print(f"Never Compromise: {len(knowledge.never_compromise)}")
    
    print("\n" + "="*60)
