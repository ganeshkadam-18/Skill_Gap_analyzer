from __future__ import annotations
from pathlib import Path
from typing import Union
from PyPDF2 import PdfReader

PathLike = Union[str, Path]


def _read_txt(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def _read_pdf(path: Path) -> str:

    reader = PdfReader(str(path))
    pages_text: list[str] = []

    for page in reader.pages:
        text = page.extract_text() or ""
        pages_text.append(text)

    return "\n".join(pages_text)


def extract_text(path: PathLike) -> str:
    
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")

    ext = p.suffix.lower()

    if ext == ".txt":
        return _read_txt(p)
    if ext == ".pdf":
        return _read_pdf(p)

    raise ValueError(
        f"Unsupported file type '{ext}'. "
        "Supported extensions are: .txt, .pdf"
    )


__all__ = ["extract_text"]

