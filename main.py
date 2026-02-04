#!/usr/bin/env python3
"""
Agentic Sales Researcher
Built for IntellColabs by the founder
Performs autonomous research on prospects and generates personalized sales hooks
"""

import os
from dotenv import load_dotenv
from researcher import WebResearcher
from analyzer import PainPointAnalyzer
from email_generator import EmailHookGenerator
import json
from datetime import datetime
from typing import Dict

# Load environment variables
load_dotenv()

class AgenticSalesResearcher:
    def __init__(self):
        self.researcher = WebResearcher()
        self.analyzer = PainPointAnalyzer()
        self.email_generator = EmailHookGenerator()
    
    def research_prospect(self, company_name: str) -> Dict:
        """
        Main orchestration method - runs the full research pipeline
        """
        print("\n" + "="*60)
        print(f"🚀 AGENTIC SALES RESEARCHER - IntellColabs")
        print("="*60)
        
        # Step 1: Web Research
        research_data = self.researcher.research_company(company_name)
        
        # Step 2: Pain Point Analysis
        analysis = self.analyzer.analyze_pain_points(research_data)
        
        # Step 3: Generate Email Hook
        email_hook = self.email_generator.generate_hook(analysis)
        
        # Compile final output
        result = {
            "company_name": company_name,
            "timestamp": datetime.now().isoformat(),
            "pain_points": analysis["analysis"],
            "email_hook": email_hook,
            "sources": research_data["raw_sources"]
        }
        
        return result
    
    def save_result(self, result: Dict, filename: str = None):
        """Save research results to JSON file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"research_{result['company_name'].replace(' ', '_')}_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(result, indent=2, fp=f)
        
        print(f"\n💾 Results saved to: {filename}")
    
    def display_result(self, result: Dict):
        """Pretty print the research results"""
        print("\n" + "="*60)
        print("📊 RESEARCH RESULTS")
        print("="*60)
        print(f"\nCompany: {result['company_name']}")
        print(f"Researched: {result['timestamp']}")
        
        print("\n" + "-"*60)
        print("🎯 IDENTIFIED PAIN POINTS:")
        print("-"*60)
        print(result['pain_points'])
        
        print("\n" + "-"*60)
        print("✉️  PERSONALIZED EMAIL HOOK:")
        print("-"*60)
        print(result['email_hook'])
        
        print("\n" + "-"*60)
        print(f"📚 SOURCES ({len(result['sources'])} found):")
        print("-"*60)
        for i, source in enumerate(result['sources'][:5], 1):
            print(f"\n{i}. {source['title']}")
            print(f"   {source['url']}")
        
        print("\n" + "="*60)

def main():
    """Main entry point"""
    agent = AgenticSalesResearcher()
    
    # Example usage
    print("\n🤖 Welcome to the Agentic Sales Researcher!")
    print("Enter a company name to research (or 'quit' to exit)\n")
    
    while True:
        company_name = input("Company name: ").strip()
        
        if company_name.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Thanks for using Agentic Sales Researcher!")
            break
        
        if not company_name:
            print("Please enter a valid company name")
            continue
        
        try:
            # Run the research
            result = agent.research_prospect(company_name)
            
            # Display results
            agent.display_result(result)
            
            # Ask if they want to save
            save = input("\n💾 Save results to file? (y/n): ").strip().lower()
            if save == 'y':
                agent.save_result(result)
            
            print("\n" + "-"*60)
            
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("Please try again with a different company name")
            continue

if __name__ == "__main__":
    main()
