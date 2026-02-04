# ⚡ QUICK START - Get Running in 2 Minutes

## What You Got

A fully-functional AI sales research agent that:
- Searches the web for company info
- Identifies pain points using AI
- Generates personalized email hooks
- **All for FREE** using Google Gemini + Tavily

## 3 Steps to Launch

### 1️⃣ Install Python Packages

Open terminal in this folder and run:

```bash
pip install tavily-python google-generativeai python-dotenv requests beautifulsoup4
```

Or just:
```bash
pip install -r requirements.txt
```

### 2️⃣ Test It Works

```bash
python test.py
```

You should see research results for "Notion" in about 30 seconds.

### 3️⃣ Start Researching

```bash
python main.py
```

Enter any company name and watch the magic happen!

---

## What Each File Does

**Core Files:**
- `main.py` - Main program (run this!)
- `researcher.py` - Web search engine
- `analyzer.py` - AI pain point detector
- `email_generator.py` - Hook writer
- `.env` - Your API keys (already configured ✅)

**Utilities:**
- `test.py` - Quick test with Notion
- `batch_research.py` - Research 10+ companies at once
- `companies.txt` - Example company list

**Documentation:**
- `README.md` - Full documentation
- `INSTALL.md` - Detailed setup guide
- `QUICKSTART.md` - This file!

---

## Example Output

```
Company name: Stripe

🎯 PAIN POINTS:
Pain Point 1: Stripe expanded into 15 new countries in Q1 2025, 
creating timezone and localization challenges for merchant support...

✉️  EMAIL HOOK:
I saw Stripe just expanded payment processing into 15 new markets 
last month, which usually means your support team is drowning in 
timezone-scattered merchant questions. We built an AI agent for a 
fintech company in a similar growth phase that automated 40% of 
their Tier-1 support tickets across APAC and LATAM. Want to see 
how we handled the multilingual routing without hiring 50 more 
support reps?
```

---

## Common Issues

**"ModuleNotFoundError"**
→ Run: `pip install -r requirements.txt`

**"Invalid API key"**
→ Check `.env` file - keys should have no spaces

**"Rate limit exceeded"**
→ You hit the free tier limit. Wait 1 hour.

**No internet connection errors**
→ Check your network connection

---

## Pro Mode: Batch Processing

Research 10 companies at once:

1. Edit `companies.txt` - add your target companies
2. Run: `python batch_research.py`
3. Choose option 2 (load from file)
4. Get back all results in one JSON file

---

## Your APIs (Configured ✅)

---

## Next Steps

1. ✅ Run `python test.py`
2. ✅ Research 5 real companies you're targeting
3. ✅ Compare AI hooks vs your current templates
4. Add HubSpot integration (ask me how)
5. Deploy as internal IntellColabs tool

---

**Ready? Run:** `python test.py`

Then: `python main.py`

🚀 Happy researching!
