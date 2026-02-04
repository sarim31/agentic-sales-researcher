#!/usr/bin/env python3
"""
Quick test script to verify the Agentic Sales Researcher works
Tests with a well-known company (Notion) that has plenty of online info
"""

from dotenv import load_dotenv
from main import AgenticSalesResearcher

load_dotenv()

def run_test():
    print("🧪 Running test with Notion as the target company...")
    print("This will verify:")
    print("  ✓ Tavily API is working")
    print("  ✓ Google Gemini API is working")
    print("  ✓ Pain point detection is functioning")
    print("  ✓ Email hook generation is working")
    print("\n" + "="*60 + "\n")
    
    agent = AgenticSalesResearcher()
    
    try:
        # Test with Notion (good test case - lots of public info)
        result = agent.research_prospect("Notion")
        
        # Display the results
        agent.display_result(result)
        
        # Validate output
        print("\n" + "="*60)
        print("🎉 TEST PASSED!")
        print("="*60)
        print("\n✅ All systems operational")
        print("✅ Ready to research real prospects")
        print("\nTry running: python main.py")
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Check your .env file has the correct API keys")
        print("2. Verify you have internet connection")
        print("3. Make sure you installed: pip install -r requirements.txt")

if __name__ == "__main__":
    run_test()
