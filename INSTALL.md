# 🚀 INSTALLATION GUIDE

## Quick Start (5 minutes)

### Step 1: Download the Project
You should have these files:
- main.py
- researcher.py
- analyzer.py
- email_generator.py
- requirements.txt
- .env
- README.md
- test.py

### Step 2: Install Python (if needed)
Check if you have Python:
```bash
python --version
```

Need Python? Download from: https://www.python.org/downloads/
(Get Python 3.8 or higher)

### Step 3: Install Dependencies

Open terminal/command prompt in the project folder:

**On Mac/Linux:**
```bash
pip3 install -r requirements.txt
```

**On Windows:**
```bash
pip install -r requirements.txt
```

### Step 4: Run the Test

```bash
python test.py
```

If it works, you'll see research results for Notion!

### Step 5: Start Using It

```bash
python main.py
```

## Troubleshooting

### "No module named 'dotenv'"
```bash
pip install python-dotenv
```

### "No module named 'tavily'"
```bash
pip install tavily-python
```

### "No module named 'google.generativeai'"
```bash
pip install google-generativeai
```

### API Key Errors
- Open `.env` file
- Make sure your API keys are correct
- No spaces around the `=` sign

### "Rate limit exceeded"
You hit the free tier limit. Wait an hour or upgrade your API plan.

## What Each File Does

- **main.py**: The main program (run this)
- **researcher.py**: Handles web searching with Tavily
- **analyzer.py**: AI analyzes pain points
- **email_generator.py**: Creates personalized hooks
- **test.py**: Quick test to verify everything works
- **.env**: Your API keys (keep this secret!)
- **requirements.txt**: List of dependencies

## Next Steps After Installation

1. Run `python test.py` to verify setup
2. Run `python main.py` to start researching real companies
3. Test with 5-10 companies you're actually targeting
4. Compare the AI-generated hooks to your current templates
5. Measure response rate improvements

## Pro Tips

**Batch Processing:**
Create a file called `companies.txt`:
```
Stripe
Notion
Salesforce
HubSpot
Zoom
```

Then modify main.py to read from that file instead of manual input.

**CRM Integration:**
Once you validate this works, we can add HubSpot API integration to automatically update contact notes.

**Cost Optimization:**
- Gemini free tier: 1,500 requests/day
- Tavily free tier: 1,000 searches/month
- You can research ~300 companies/month for FREE

## Support

If you run into issues:
1. Check the error message carefully
2. Verify your API keys in .env
3. Make sure you have internet connection
4. Try the test.py script first

---

**You're ready to go!** Run `python test.py` to start.
