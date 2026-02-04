import os
from typing import Dict

# Try new API first, fall back to old one
try:
    from google import genai
    USE_NEW_API = True
except ImportError:
    import google.generativeai as genai
    USE_NEW_API = False

class EmailHookGenerator:
    def __init__(self):
        if USE_NEW_API:
            # New API initialization
            self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        else:
            # Old API initialization
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            self.model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    def generate_hook(self, analysis: Dict) -> str:
        """
        Generates a 3-sentence personalized email hook
        based on the pain point analysis
        """
        print("\n✍️  Generating personalized email hook...")
        
        prompt = self._build_email_prompt(analysis)
        
        if USE_NEW_API:
            response = self.client.models.generate_content(
                model='models/gemini-2.5-flash',
                contents=prompt
            )
            email_hook = response.text.strip()
        else:
            response = self.model.generate_content(prompt)
            email_hook = response.text.strip()
        
        print("✅ Email hook generated")
        
        return email_hook
    
    def _build_email_prompt(self, analysis: Dict) -> str:
        """Build the prompt for email hook generation"""
        
        system_prompt = """You are an expert sales copywriter specializing in cold outreach.

Your task: Write a 3-sentence email opener that proves you did deep research on the prospect.

RULES:
1. EXACTLY 3 sentences - no more, no less
2. First sentence: Reference a SPECIFIC recent event, news, or data point
3. Second sentence: Connect that event to a pain point IntellColabs solves
4. Third sentence: Soft CTA that offers value (not pushy)

STYLE REQUIREMENTS:
- Conversational, not corporate
- No buzzwords ("leverage", "synergy", "cutting-edge")
- No generic compliments ("I was impressed by...")
- Prove you're a human who did research, not a bot

BAD EXAMPLE:
"I came across your company and was impressed by your growth. I think we could help you scale. Would you be open to a quick call?"

GOOD EXAMPLE:
"I noticed you just raised $12M and are expanding into European markets based on your Series A announcement last week. Scaling sales ops across time zones usually means your team is drowning in manual lead research and timezone scheduling. We built an AI agent for a similar B2B SaaS company that cut their sales prep time by 60% - happy to show you the exact workflow if you're dealing with the same chaos."

Now write the email opener:
"""
        
        context = f"""
COMPANY: {analysis['company_name']}

PAIN POINT ANALYSIS:
{analysis['analysis']}

Write the 3-sentence email opener:
"""
        
        return f"{system_prompt}\n{context}"
