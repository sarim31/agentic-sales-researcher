# 🤖 Agentic Sales Researcher

An autonomous AI agent that performs deep research on prospects before sales calls. Built for **IntellColabs** to demonstrate AI-powered sales automation.

## What It Does

1. **Web Research**: Scrapes recent news, funding announcements, product launches
2. **Pain Point Detection**: Uses AI to identify specific problems your company can solve
3. **Email Hook Generation**: Creates hyper-personalized 3-sentence openers that prove you did research

## Features

✅ Completely autonomous - just provide a company name
✅ Uses Google Gemini (free tier) + Tavily search
✅ No generic BS - every hook is specific and researched
✅ Saves results to JSON for CRM integration later
✅ Built-in source tracking for credibility

## Tech Stack

- **Python 3.8+**
- **Google Gemini API** (LLM for analysis)
- **Tavily API** (AI-optimized web search)
- **Modular Architecture** (easy to extend)

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Keys

Your `.env` file is already configured with:
- Tavily API Key: ✅
- Google Gemini API Key: ✅

### 3. Run the Agent

```bash
python main.py
```

## Usage

### Interactive Mode

```bash
python main.py
```

Then enter any company name:
```
Company name: Stripe
Company name: Notion
Company name: Salesforce
```

### Sample Output

```
🎯 IDENTIFIED PAIN POINTS:
Pain Point 1: Stripe recently expanded payment processing into 15 new countries (Jan 2025), which means their support team is likely overwhelmed with timezone-specific merchant inquiries...

✉️  PERSONALIZED EMAIL HOOK:
I saw Stripe just expanded into 15 new markets last month, which usually means your support team is drowning in timezone-scattered merchant questions. We built an AI agent for a fintech company in a similar growth phase that automated 40% of their Tier-1 support tickets across APAC and LATAM. Want to see how we handled the multilingual routing without hiring 50 more support reps?
```

## Project Structure

```
agentic-sales-researcher/
├── main.py              # Orchestrator
├── researcher.py        # Tavily web search
├── analyzer.py          # Gemini pain point detection
├── email_generator.py   # Gemini hook writer
├── requirements.txt     # Dependencies
└── .env                 # API keys (gitignored)
```

## Extending the Project

### Phase 2 Ideas

1. **HubSpot Integration**: Auto-update CRM with research findings
2. **SQLite Database**: Store all researched companies
3. **Batch Mode**: Upload a CSV of 100 companies, get 100 personalized hooks
4. **LinkedIn Integration**: Pull company info from LinkedIn URLs
5. **Slack Bot**: Run research commands from Slack

### HubSpot Integration Example

```python
# In main.py, add this method:
def push_to_hubspot(self, result: Dict, contact_id: str):
    import requests
    
    url = f"https://api.hubapi.com/crm/v3/objects/contacts/{contact_id}"
    headers = {"Authorization": f"Bearer {os.getenv('HUBSPOT_API_KEY')}"}
    
    data = {
        "properties": {
            "notes": f"AI Research:\n{result['pain_points']}\n\nSuggested Hook:\n{result['email_hook']}"
        }
    }
    
    requests.patch(url, json=data, headers=headers)
```

## Cost Analysis

**Current Setup (Free Tier):**
- Tavily: 1,000 searches/month FREE
- Google Gemini: 1,500 requests/day FREE
- Cost per research: $0.00

**Production (Paid Tier):**
- Tavily: ~$0.001 per search
- Gemini: ~$0.0001 per request
- Cost per research: ~$0.004 (less than half a cent)

At 1,000 prospects/month = **$4/month**

## Why This Matters

Traditional sales research:
- 20 minutes per prospect
- Generic email templates
- Low response rates

With this agent:
- 30 seconds per prospect
- Hyper-personalized hooks
- Proves you did real research

**ROI**: If this gets you even ONE extra meeting per week, it pays for itself 1000x over.

## Next Steps

1. ✅ Test with 10 real companies
2. Measure response rate improvement
3. Add HubSpot integration
4. Build batch processing mode
5. Deploy as internal tool at IntellColabs

---

**Built by**: IntellColabs Founder
**Purpose**: Demonstrate AI agent capabilities for sales automation
**Status**: Production-ready prototype
