import io
import pypdf

async def get_text(file) :
    await file.seek(0)
    pdf_bytes = await file.read()
    reader= pypdf.PdfReader(io.BytesIO(pdf_bytes))
    pdf_text = "\n".join([r.extract_text() for r in reader.pages if r.extract_text()])
    return pdf_text