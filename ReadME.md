# 🧠 RAG-MVP — Retrieval Augmented Generation (Step-by-Step Build)

This repository contains the **step-by-step implementation** of a Retrieval-Augmented Generation (RAG) system built completely **from scratch** without using pre-made frameworks like LangChain or LlamaIndex.

This README reflects **only the work completed up to Step 2**:

- Environment setup
- OCR setup and testing
- PDF/Text/Image extraction
- Chunking
- Embeddings
- FAISS vector storage

More steps will be added later as the project grows.

---

## 🚀 Completed so far (Step 1 & Step 2)

### ✔ Step 1 — Environment + OCR Setup

- Created a Python virtual environment (`.venv`)
- Installed all required Python packages
- Installed **Tesseract OCR** (Windows)
- Verified:
  - PyMuPDF working
  - OpenCV working
  - SentenceTransformers working
  - Tesseract command accessible
- Successfully ran `test_OCR.py`

---

### ✔ Step 2 — Document Ingestion Pipeline

We built a fully working ingestion system that performs:

#### **1. PDF Text Extraction**

Using **PyMuPDF** (`fitz`):

- Extracts text page-by-page
- Supports scanned PDFs via OCR fallback

#### **2. Image OCR Extraction**

Using:

- Tesseract OCR
- OpenCV preprocessing
- Pillow for image loading

Supports:

- `.png`
- `.jpg`
- `.jpeg`

#### **3. Chunking**

- Splits extracted text into manageable chunks
- Default size: **300 words per chunk**

#### **4. Embedding Generation**

Using:

- `all-MiniLM-L6-v2` (SentenceTransformers)
- Outputs 768-dimensional embeddings

#### **5. FAISS Vector Index**

- Stores embeddings in a local FAISS index
- Saved as: `vector.index`

---

## 📁 Project Structure (Current)
