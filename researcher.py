import os
from tavily import TavilyClient
from typing import Dict, List

class WebResearcher:
    def __init__(self):
        self.tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    
    def research_company(self, company_name: str) -> Dict:
        """
        Performs comprehensive web research on a company
        Returns structured data about news, tech stack, and company info
        """
        print(f"\n🔍 Researching {company_name}...")
        
        # Search 1: Recent news and announcements
        news_query = f"{company_name} news funding product launch 2024 2025"
        news_results = self.tavily.search(
            query=news_query,
            search_depth="advanced",
            max_results=5
        )
        
        # Search 2: Company about page and mission
        about_query = f"{company_name} about mission technology"
        about_results = self.tavily.search(
            query=about_query,
            search_depth="basic",
            max_results=3
        )
        
        # Search 3: Tech stack (if available)
        tech_query = f"{company_name} technology stack tools software uses"
        tech_results = self.tavily.search(
            query=tech_query,
            search_depth="basic",
            max_results=3
        )
        
        # Compile all research
        research_data = {
            "company_name": company_name,
            "news": self._extract_content(news_results),
            "about": self._extract_content(about_results),
            "tech_stack": self._extract_content(tech_results),
            "raw_sources": self._extract_sources(news_results, about_results, tech_results)
        }
        
        print(f"✅ Found {len(research_data['raw_sources'])} sources")
        return research_data
    
    def _extract_content(self, search_results: Dict) -> List[str]:
        """Extract clean content from Tavily results"""
        content = []
        if 'results' in search_results:
            for result in search_results['results']:
                if 'content' in result and result['content']:
                    content.append(result['content'])
        return content
    
    def _extract_sources(self, *result_sets) -> List[Dict]:
        """Extract source URLs and titles from all search results"""
        sources = []
        for result_set in result_sets:
            if 'results' in result_set:
                for result in result_set['results']:
                    sources.append({
                        'title': result.get('title', 'No title'),
                        'url': result.get('url', ''),
                        'snippet': result.get('content', '')[:200] + '...'
                    })
        return sources
