# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Personal portfolio website for **Gunal Hincal** (AI-Focused Business Analyst & Data/AI Specialist). The repository currently contains only source assets — the site itself has not been scaffolded yet. There are no build, lint, or test commands until a stack is chosen; update this file when one is added.

## Requirements

- Dark/light mode toggle (persist the user's choice, e.g. via `localStorage`).
- Smooth animations throughout (scroll reveals, transitions, hover states).
- No imposed style constraints — design decisions are left to the implementer.
- All site content comes from the CV; do not invent experience, projects, or claims not in it.

## Assets

- `assets/gh.JPG` — Gunal's photo (use for hero/about section).
- `assets/Gunal_Hincal_CV.pdf` — the canonical content source (3 pages). Offer it as a downloadable CV link on the site.

### Reading the CV PDF in this environment

The Read tool cannot render PDFs here (`pdftoppm` is unavailable). Extract text with pypdf instead (already installed; `-X utf8` avoids cp1254 encode errors from bullet characters):

```bash
python -X utf8 -c "
from pypdf import PdfReader
import sys
for p in PdfReader(r'assets/Gunal_Hincal_CV.pdf').pages:
    sys.stdout.write(p.extract_text() + '\n')
"
```

## CV content summary (verified against the PDF)

- **Name/title:** Gunal Hincal, MSc. — AI-Focused Business Analyst & Data&AI Specialist | Generative AI | LLM Systems | Strategic Analytics.
- **Contact:** hincalgunal@gmail.com · +90 534 378 3847 · WhatsApp +974 70993417 · linkedin.com/in/gunalhincal · github.com/GunalHincal · medium.com/@hincalgunal
- **Profile:** Designs GenAI solutions, LLM pipelines, RAG architectures, and multi-agent systems across banking, manufacturing, and enterprise; combines AI engineering with business analysis (requirements, stakeholder alignment, governance-aligned delivery). Currently at Akbank on GenAI product initiatives. Building **GunAI Solutions** (B2B AI automation for the Gulf market).
- **Experience:**
  - Specialist, Business Analyst – AI & GenAI Products, Akbank Technology via Etiya (Dec 2025–present)
  - Private AI Instructor, Independent/Remote (Aug 2025–present)
  - Enterprise Generative AI Solutions Architect, Skymod Technology, İzmir (Aug–Dec 2025)
  - AI/ML Solutions Architect, Practicus AI, Remote (Feb 2024–Jan 2025)
  - Teaching Assistant & Bootcamp Mentor, Miuul, Remote (Jan 2023–Nov 2025)
- **Projects (with live links in the CV):**
  - Document Intelligence SaaS (GunAI Solutions) — Flask + Claude Vision, invoice extraction, TR/EN dashboard, KVKK compliance — document-intelligence-vaqj.onrender.com
  - Book-Based RAG Chatbot (Megapik Yeniden) — Gemini API + ChromaDB + FastAPI — megapikyenidenchatbot-production.up.railway.app
  - Azure OCR API — github.com/GunalHincal/azure-ocr-api
  - Speech-to-Text Transcription App (FastAPI + Whisper), Text-to-Speech Tool (gTTS)
  - Client work: complaint automation (Chef Seasons), 553K-row retail demand forecasting (Cevher Wheel), CV quality-control pipeline (Dardanel)
- **Skills:** RAG, multi-agent systems, prompt engineering, function calling, vector DBs · Python, SQL, FastAPI, REST, Git · scikit-learn, TensorFlow, PyTorch, NLP, Pandas · Power BI, Matplotlib, Seaborn, Plotly · Azure (DP-900), Azure OpenAI, GCP, Docker, Render, Supabase · n8n, Power Automate, Zapier, Skystudio.
- **Education:** M.Sc. Management Information Systems, Sakarya University (Jan 2025–present, thesis on LLM fine-tuning); B.Sc. Physical Education and Sports Teaching, Hacettepe University (2006–2011).
- **Certifications:** DP-900 (Oct 2024); Miuul Data Analyst, Data Scientist, and Agile bootcamps; VBO Data Engineering mini bootcamp; GenAI Fundamentals with Gemini (2025); various Miuul course certificates.
- **Languages:** Turkish (native), English (professional working proficiency). Publishes technical content on Medium/LinkedIn.

## Architecture notes

- A static site (plain HTML/CSS/JS) is sufficient for this scope and deploys anywhere; only add a framework/build step if a feature genuinely requires it.
- The dark/light toggle should default to the user's `prefers-color-scheme` and respect `prefers-reduced-motion` for animations.
- The site is bilingual-friendly content-wise (TR/EN audience), but the CV is in English — build in English unless asked otherwise.
