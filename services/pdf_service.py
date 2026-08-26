import pypdf
import io

def get_text(pdf_bytes) :
    reader= pypdf.PdfReader(io.BytesIO(pdf_bytes))
    pdf_text = "\n".join([r.extract_text() for r in reader.pages() if r.extract_text()])
    return pdf_text