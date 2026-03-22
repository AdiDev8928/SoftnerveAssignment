# 📖 AI-Powered Book Chapter Rewriter with HITL & RL Retrieval

An agentic AI pipeline that scrapes a classic book chapter from the web, rewrites it for modern readers using **Google Gemini**, incorporates **Human-in-the-Loop (HITL)** review, stores versions in **ChromaDB**, and retrieves the best version using an **epsilon-greedy Reinforcement Learning** strategy.

Built as a pre-internship assignment for **Softnerve**.

---

## 🧠 How It Works

```
Web Scrape (Playwright)
        ↓
Multi-Agent AI Pipeline (Gemini)
   ├── DraftingAgent   → Rewrites for clarity
   ├── StyleAgent      → Improves tone & engagement
   └── ComplianceAgent → Ensures ethical standards
        ↓
Save Draft → spun_chapter.txt
        ↓
HITL Review Loop (Writer → Reviewer → Editor)
        ↓
Store Versions in ChromaDB
        ↓
RL-Based Retrieval (Epsilon-Greedy)
```

---

## ✨ Features

- 🌐 **Web Scraping** — Uses Playwright to scrape and screenshot a live web page
- 🤖 **Multi-Agent Pipeline** — Three sequential AI agents each refine the chapter
- 👨‍💼 **Human-in-the-Loop (HITL)** — Writer, Reviewer, and Editor each get a manual review pass
- 🗄️ **ChromaDB Version Control** — Every AI and human-approved version is stored with timestamps
- 🎯 **RL Retrieval** — Epsilon-greedy strategy selects the best stored version on query
- ⚡ **Powered by Gemini** — Uses Google's `gemma-3n-e2b-it` model via the Generative AI SDK

---

## 📂 Project Structure

```
ai-chapter-rewriter/
├── scrape.py                      # Scrapes chapter text & screenshot via Playwright
├── llm_spinner.py                 # Standalone Gemini-based chapter spinner
├── hitl_chromadb_agentic_flow.py  # Main pipeline: agents + HITL + ChromaDB + RL
├── chapter1.txt                   # Scraped raw chapter text
├── spun_chapter.txt               # AI-generated & human-reviewed output
├── screenshot.png                 # Full-page screenshot of the scraped page
└── requirements.txt               # Project dependencies
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-chapter-rewriter.git
cd ai-chapter-rewriter
```

### 2. Set Up a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

### 4. Add Your API Key

In both `llm_spinner.py` and `hitl_chromadb_agentic_flow.py`, replace the placeholder with your actual Gemini API key:

```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

> ⚠️ Never hardcode API keys in production. Use environment variables or a `.env` file.

### 5. Run the Pipeline

**Step 1 — Scrape the chapter:**
```bash
python scrape.py
```

**Step 2 — Run the full agentic pipeline:**
```bash
python hitl_chromadb_agentic_flow.py
```

The HITL loop will open `spun_chapter.txt` for manual review by each role (Writer → Reviewer → Editor). Press `Enter` after each review to proceed.

---

## 📦 Requirements

```
google-generativeai
chromadb
playwright
```

---

## ⚠️ Important Note

This project contains a **hardcoded API key** for demonstration purposes. Before pushing to GitHub:

1. Revoke the existing key at [Google AI Studio](https://aistudio.google.com/)
2. Generate a new key
3. Store it securely using environment variables:

```python
import os
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
```

---

## 🛠️ Built With

- [Google Generative AI SDK](https://ai.google.dev/) — Gemini LLM backend
- [ChromaDB](https://www.trychroma.com/) — Vector database for version storage
- [Playwright](https://playwright.dev/python/) — Headless browser for web scraping

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
