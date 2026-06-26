from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_chunks(pdf_path):
    pdf = PdfReader(pdf_path)

    text = ""

    for page in pdf.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)

    print("Chunks:", len(chunks))

    return chunks