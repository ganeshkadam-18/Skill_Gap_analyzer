import PyPDF2
import docx2txt

def extract_text_from_pdf(file):
    """Parses PDF binary streams and aggregates text content from all pages."""
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + " "
    return text

def extract_text_from_docx(file):
    """Processes DOCX files and yields raw text content."""
    text = docx2txt.process(file)
    return text

def extract_text(file):
    """
    Entry point for document text extraction.
    Determines processing method based on file extension.
    """
    filename = file.name.lower()
    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif filename.endswith(".docx") or filename.endswith(".doc"):
        return extract_text_from_docx(file)
    else:
        # Fallback for plain text or unknown formats
        try:
            return file.read().decode("utf-8")
        except Exception:
            return ""
