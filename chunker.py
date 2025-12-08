"""
chunker.py

Two chunking strategies:
  1) char_chunk_text: simple character-based chunking (fast, dependency-free)
  2) token_chunk_text: tokenizer-aware chunking using tiktoken (better for LLM token budgets)

Both return a list of dicts:
  {
    "id": "<file>-pX-cY",
    "source": "<file>",
    "page": X,           # optional (use None if not available)
    "text": "<chunk_text>",
    "start_char": <int>, # char offset in original text
    "end_char": <int>
  }
"""

from typing import List, Optional
import math

# Optional tokenizer-aware chunking (recommended if you use OpenAI or other token-based LLMs)
try:
    import tiktoken
    _HAS_TIKTOKEN = True
except Exception:
    _HAS_TIKTOKEN = False


def char_chunk_text(text: str,
                    source: str = "unknown",
                    page_num: Optional[int] = None,
                    chunk_size_chars: int = 2000,
                    overlap_chars: int = 200) -> List[dict]:

    if not text:
        return []

    text = text.strip()
    n = len(text)

    # Safety check
    if overlap_chars >= chunk_size_chars:
        raise ValueError("overlap_chars must be smaller than chunk_size_chars")

    step = chunk_size_chars - overlap_chars

    chunks = []
    start = 0
    chunk_idx = 0

    while start < n:
        end = min(start + chunk_size_chars, n)

        chunk_text = text[start:end].strip()

        chunks.append({
            "id": f"{source}-p{page_num}-c{chunk_idx}",
            "source": source,
            "page": page_num,
            "text": chunk_text,
            "start_char": start,
            "end_char": end
        })

        chunk_idx += 1

        # Move by STEP not by overlap
        start += step

        # Safety: stop if not progressing (avoid infinite loops)
        if start >= n:
            break

    return chunks


def token_chunk_text(text: str,
                     source: str = "unknown",
                     page_num: Optional[int] = None,
                     chunk_size_tokens: int = 400,
                     overlap_tokens: int = 50,
                     model: str = "cl100k_base") -> List[dict]:
    """
    Tokenizer-aware chunker using tiktoken (OpenAI tokenization).
    - chunk_size_tokens: tokens per chunk
    - overlap_tokens: tokens overlap between chunks
    - model: encoding name (default cl100k_base for recent OpenAI models)
    Returns same metadata format as char_chunk_text.
    """
    if not _HAS_TIKTOKEN:
        raise RuntimeError("tiktoken not installed. Install it with: pip install tiktoken")

    enc = tiktoken.get_encoding(model)
    tokens = enc.encode(text)
    n_tokens = len(tokens)
    chunks = []
    start_tok = 0
    idx = 0

    while start_tok < n_tokens:
        end_tok = start_tok + chunk_size_tokens
        if end_tok >= n_tokens:
            end_tok = n_tokens

        tok_span = tokens[start_tok:end_tok]
        # decode back to string for storage/context
        chunk_text = enc.decode(tok_span).strip()

        # compute approximate char offsets by decoding previous tokens
        # to get start_char and end_char — this is approximate but useful
        start_char = len(enc.decode(tokens[:start_tok]))
        end_char = start_char + len(chunk_text)

        chunks.append({
            "id": f"{source}-p{page_num}-c{idx}",
            "source": source,
            "page": page_num,
            "text": chunk_text,
            "start_char": start_char,
            "end_char": end_char
        })

        idx += 1
        start_tok = end_tok - overlap_tokens
        if start_tok < 0:
            start_tok = 0

    return chunks


# --------------------------
# small utility: paginate pages -> chunks
# --------------------------
def chunk_pages(pages: List[dict],
                method: str = "token",
                **kwargs) -> List[dict]:
    """
    pages: list of dicts with keys: {"file_name", "page_number", "content"}
    method: "token" (preferred) or "char"
    kwargs: passed to respective chunker
    """
    results = []
    for page in pages:
        file_name = page.get("file_name", "unknown")
        page_num = page.get("page_number", None)
        content = page.get("content", "") or ""

        if method == "char":
            c = char_chunk_text(content, source=file_name, page_num=page_num, **kwargs)
        else:
            # token method
            if not _HAS_TIKTOKEN:
                # fallback to char chunking but warn
                print("warning: tiktoken not installed, falling back to char chunker")
                c = char_chunk_text(content, source=file_name, page_num=page_num, **kwargs)
            else:
                c = token_chunk_text(content, source=file_name, page_num=page_num, **kwargs)

        results.extend(c)

    return results


# --------------------------
# quick test (run as script)
# --------------------------
if __name__ == "__main__":
    sample_text = ("This is a short demo paragraph. " * 80).strip()
    pages = [{"file_name": "demo.pdf", "page_number": 1, "content": sample_text}]

    print("CHAR chunker example (chunk_size=500 chars):")
    char_chunks = char_chunk_text(sample_text, source="demo.pdf", page_num=1, chunk_size_chars=500, overlap_chars=50)
    for c in char_chunks[:2]:
        print(c["id"], "len:", len(c["text"]))

    if _HAS_TIKTOKEN:
        print("\nTOKEN chunker example (chunk_size=100 tokens):")
        token_chunks = token_chunk_text(sample_text, source="demo.pdf", page_num=1,
                                        chunk_size_tokens=100, overlap_tokens=20)
        for c in token_chunks[:2]:
            print(c["id"], "approx len:", len(c["text"]))
    else:
        print("\nToken chunking not available (tiktoken not installed).")
