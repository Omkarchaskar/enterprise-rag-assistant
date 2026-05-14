from pypdf import PdfReader


def load_pdf(file_path: str) -> str:
    """
    Load and extract text from PDF
    """

    pdf_reader = PdfReader(file_path)

    extracted_text = ""

    for page in pdf_reader.pages:
        text = page.extract_text()

        if text:
            extracted_text += text + "\n"

    return extracted_text