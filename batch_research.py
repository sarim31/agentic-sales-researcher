#!/usr/bin/env python3
"""
Batch Research Mode
Research multiple companies from a list and save all results
"""

from dotenv import load_dotenv
from main import AgenticSalesResearcher
import json
import time
from datetime import datetime

load_dotenv()

def batch_research(companies: list, delay_seconds: int = 5):
    """
    Research multiple companies with a delay between each
    to avoid hitting API rate limits
    """
    agent = AgenticSalesResearcher()
    results = []
    
    print(f"\n🚀 Starting batch research for {len(companies)} companies")
    print(f"⏱️  Delay between companies: {delay_seconds} seconds")
    print("="*60 + "\n")
    
    for i, company in enumerate(companies, 1):
        print(f"\n[{i}/{len(companies)}] Researching: {company}")
        
        try:
            result = agent.research_prospect(company)
            results.append(result)
            
            # Display brief summary
            print(f"✅ Complete - Found {len(result['sources'])} sources")
            
            # Save individual result
            agent.save_result(result)
            
            # Delay before next company (except for last one)
            if i < len(companies):
                print(f"⏳ Waiting {delay_seconds} seconds before next research...")
                time.sleep(delay_seconds)
                
        except Exception as e:
            print(f"❌ Error researching {company}: {str(e)}")
            results.append({
                "company_name": company,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            })
    
    # Save combined batch results
    batch_filename = f"batch_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(batch_filename, 'w') as f:
        json.dump(results, indent=2, fp=f)
    
    print("\n" + "="*60)
    print("📊 BATCH RESEARCH COMPLETE")
    print("="*60)
    print(f"✅ Successfully researched: {len([r for r in results if 'error' not in r])}")
    print(f"❌ Errors: {len([r for r in results if 'error' in r])}")
    print(f"💾 Batch results saved to: {batch_filename}")
    
    return results

def load_companies_from_file(filename: str) -> list:
    """Load company names from a text file (one per line)"""
    with open(filename, 'r') as f:
        companies = [line.strip() for line in f if line.strip()]
    return companies

def main():
    """Main entry point for batch processing"""
    print("\n🤖 Agentic Sales Researcher - Batch Mode")
    print("="*60)
    
    print("\nOptions:")
    print("1. Enter companies manually")
    print("2. Load from file (companies.txt)")
    
    choice = input("\nChoice (1 or 2): ").strip()
    
    if choice == "2":
        try:
            companies = load_companies_from_file("companies.txt")
            print(f"\n📄 Loaded {len(companies)} companies from file")
        except FileNotFoundError:
            print("\n❌ Error: companies.txt not found")
            print("Create a file called 'companies.txt' with one company name per line")
            return
    else:
        companies = []
        print("\nEnter company names (one per line, empty line to finish):")
        while True:
            company = input("> ").strip()
            if not company:
                break
            companies.append(company)
    
    if not companies:
        print("No companies to research!")
        return
    
    print(f"\n📋 Companies to research:")
    for i, company in enumerate(companies, 1):
        print(f"  {i}. {company}")
    
    confirm = input("\nProceed with batch research? (y/n): ").strip().lower()
    
    if confirm == 'y':
        # Run batch research with 5-second delays
        batch_research(companies, delay_seconds=5)
    else:
        print("Batch research cancelled")

if __name__ == "__main__":
    main()
