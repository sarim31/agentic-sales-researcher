import os
from typing import Dict, List

# Try new API first, fall back to old one
try:
    from google import genai
    USE_NEW_API = True
except ImportError:
    import google.generativeai as genai
    USE_NEW_API = False

class PainPointAnalyzer:
    def __init__(self):
        if USE_NEW_API:
            # New API initialization
            self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        else:
            # Old API initialization
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            self.model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    def analyze_pain_points(self, research_data: Dict) -> Dict:
        """
        Uses LLM to identify specific pain points from research data
        that IntellColabs can solve with AI automation
        """
        print("\n🧠 Analyzing pain points with AI...")
        
        # Construct the analysis prompt
        prompt = self._build_analysis_prompt(research_data)
        
        # Get AI analysis
        if USE_NEW_API:
            response = self.client.models.generate_content(
                model='models/gemini-2.5-flash',
                contents=prompt
            )
            analysis_text = response.text
        else:
            response = self.model.generate_content(prompt)
            analysis_text = response.text
        
        print("✅ Pain point analysis complete")
        
        return {
            "company_name": research_data["company_name"],
            "analysis": analysis_text,
            "sources": research_data["raw_sources"]
        }
    
    def _build_analysis_prompt(self, research_data: Dict) -> str:
        """Build the system prompt for pain point detection"""
        
        # Combine all research into context
        context = f"""
COMPANY: {research_data['company_name']}

RECENT NEWS & ANNOUNCEMENTS:
{self._format_list(research_data['news'])}

COMPANY BACKGROUND:
{self._format_list(research_data['about'])}

TECHNOLOGY INFORMATION:
{self._format_list(research_data['tech_stack'])}
"""
        
        system_prompt = """You are a Senior Sales Engineer at IntellColabs, an AI automation company. 

Your goal: Analyze the provided company research and identify 3 SPECIFIC pain points that IntellColabs can solve.

IntellColabs specializes in:
- AI-powered workflow automation
- Custom AI agents for sales, customer service, and operations
- LLM integration into existing business processes
- Reducing manual work through intelligent automation

CRITICAL RULES:
1. Be hyper-specific - reference actual events, numbers, or quotes from the research
2. NO generic statements like "they're growing fast" or "they value innovation"
3. Each pain point must be something we learned from the research (recent funding = scaling pains, new product = integration needs, etc.)
4. Focus on TECHNICAL inefficiencies or operational bottlenecks
5. If you don't find real pain points, say "Insufficient data" - don't make things up

OUTPUT FORMAT:
Pain Point 1: [Specific issue with evidence]
Pain Point 2: [Specific issue with evidence]
Pain Point 3: [Specific issue with evidence]

Key Hook Insight: [One sentence that proves we did deep research]
"""
        
        return f"{system_prompt}\n\n{context}\n\nProvide your analysis:"
    
    def _format_list(self, items: List[str]) -> str:
        """Format list items for the prompt"""
        if not items:
            return "No data found"
        return "\n".join([f"- {item[:500]}" for item in items[:5]])  # Limit to prevent token overflow
