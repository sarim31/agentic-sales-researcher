# 🤖 Agentic Sales Researcher

> An autonomous AI agent that performs deep prospect research and generates hyper-personalized sales hooks in 30 seconds.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 What It Does

Traditional sales research takes **20+ minutes per prospect**. This AI agent does it in **30 seconds** and generates email hooks that prove you did real research.

**Input:** Company name  
**Output:** 3 pain points + personalized 3-sentence email hook

### Example Output

**Company:** Notion

**Generated Hook:**
> "I read about your February launch of Notion Mail and the new AI-powered 'search across platforms' capability. Pushing out so many distinct AI features so rapidly often creates a new wave of internal manual tasks and operational bottlenecks for teams trying to keep up. We've helped similar fast-growing companies automate away much of that internal chaos – happy to briefly outline a workflow that might resonate if you're feeling the same pressure."

**No generic BS.** Every hook references specific, recent company news.

---

## 🚀 Features

- ✅ **Autonomous Research**: Searches web for recent news, funding, tech stack
- ✅ **AI Pain Point Detection**: Identifies problems your product can solve
- ✅ **Personalized Hooks**: Generates email openers that reference real events
- ✅ **Batch Processing**: Research 10+ companies at once
- ✅ **Source Tracking**: Every claim is backed by actual sources
- ✅ **100% Free Tier**: Uses Google Gemini + Tavily (1,500 requests/day FREE)

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Google Gemini 2.5 Flash** - AI analysis & generation
- **Tavily API** - AI-optimized web search
- **Modular Architecture** - Easy to extend & customize

---

## ⚡ Quick Start

### 1. Install Dependencies

```bash
pip install tavily-python google-genai python-dotenv requests beautifulsoup4
```

### 2. Set Up API Keys

Create a `.env` file:
```bash
TAVILY_API_KEY=your_tavily_key_here
GEMINI_API_KEY=your_gemini_key_here
```

**Get Free API Keys:**
- Tavily: https://tavily.com (1,000 searches/month FREE)
- Google Gemini: https://ai.google.dev (1,500 requests/day FREE)

### 3. Run It

```bash
python test.py        # Test with Notion
python main.py        # Research any company
```

---

## 💰 Cost Analysis

**Free Tier (Current Setup):**
- Tavily: 1,000 searches/month FREE
- Google Gemini: 1,500 requests/day FREE
- **Cost per research: $0.00**

**Paid Tier (if you scale):**
- ~$0.004 per prospect (less than half a cent)
- 1,000 prospects/month = **$4/month**

---

## 📊 Real Results

**Traditional Sales Research:**
- ⏱️ 20 minutes per prospect
- 📧 Generic email templates
- 📉 Low response rates

**With This Agent:**
- ⚡ 30 seconds per prospect
- 🎯 Hyper-personalized hooks
- 📈 Provably better response rates

**ROI:** If this gets you ONE extra meeting per week, it pays for itself 1000x over.

---

## 🎨 Project Structure

```
agentic-sales-researcher/
├── main.py              # Main orchestrator
├── researcher.py        # Tavily web search
├── analyzer.py          # Gemini pain point detection
├── email_generator.py   # Gemini hook writer
├── test.py             # Quick test script
├── batch_research.py   # Batch processing
├── companies.txt       # Company list for batch mode
└── .env               # API keys (gitignored)
```

---

## 🔥 Usage Examples

### Single Company Research

```bash
python main.py
```

```
Company name: Stripe
[30 seconds later...]
✉️ EMAIL HOOK:
I saw Stripe expanded into 15 new markets last month...
```

### Batch Processing

```bash
# Edit companies.txt with your targets
python batch_research.py
```

Processes multiple companies with auto-delays to respect API limits.

---

## 🚧 Roadmap

- [ ] HubSpot CRM integration (auto-update contact notes)
- [ ] CSV import/export for bulk processing
- [ ] LinkedIn profile enrichment
- [ ] Slack bot interface
- [ ] Custom pain point templates per industry

---

## 🤝 Contributing

Contributions welcome! This is an open-source project built to help salespeople work smarter.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

MIT License - feel free to use this for personal or commercial projects.

---

## 🙏 Acknowledgments

Built by the founder of **[IntellColabs](https://intellcolabs.com)** to demonstrate practical AI agent applications for sales automation.

**Why I Built This:**
- Sales research is painfully manual
- Generic email templates don't work anymore
- AI agents can do this 40x faster with better results

If this saves you time or helps you close deals, consider:
- ⭐ Starring this repo
- 🐦 Sharing on social media
- 💼 Hiring IntellColabs for custom AI automation

---

## 📬 Contact

**IntellColabs** - [intellcolabs.com](https://intellcolabs.com)

**Questions?** Open an issue or reach out on LinkedIn.

---

**⭐ Star this repo if it helped you close more deals!**
