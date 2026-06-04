from pypdf import PdfReader

def extract_text_from_pdfs(pdf_files):

    text = ""
    total_pages = 0

    for pdf in pdf_files:

        reader = PdfReader(pdf)

        total_pages += len(reader.pages)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text, total_pages