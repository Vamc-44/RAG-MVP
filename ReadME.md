# RAG-MVP — Retrieval Augmented Generation (Step-by-Step Build)

This repository contains the **step-by-step implementation** of a Retrieval-Augmented Generation (RAG) system built completely **from scratch** with a minimal help of AI.

I wanted this repo to display the step by step process I did to build a working RAG application that helps us to extract text from different sources of inputs(PDF,Image,etc).

Initially you need to set up the enivironment and install all the dependencies required.

### Install Pytesseract

1. Download the Tesseract installer from [https://github.com/UB-Mannheim/tesseract/wiki]
2. Run the installer and follow the setup instructions.
3. During installation, note the installation path (e.g., `C:\Program Files\Tesseract-OCR`).
4. After installation, add the Tesseract installation path to your system's PATH environment variable:
   - Open the Start Menu and search for "Environment Variables".
   - Click on "Edit the system environment variables".
   - In the System Properties window, click on the "Environment Variables" button.
   - In the Environment Variables window, under "System variables", find and select the "Path" variable, then click "Edit".
   - Click "New" and add the path to the Tesseract installation directory (e.g., `C:\Program Files\Tesseract-OCR`).
   - Click "OK" to close all windows.

### Environment Setup

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Install the required requirements

```bash
pip install -r requirements.txt
```

### Check Env + lib

```bash
python check_evn.py
```

### Test PDF extraction

```bash
python test_pdf_extraction.py
```

### Test OCR

```bash
python test_pOCR.py
```

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
