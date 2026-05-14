from langchain_text_splitters import RecursiveCharacterTextSplitter

#/function tayar kela text to chunk mdhe divide kryala //
def chunk_text(text: str):
    """
    Split text into smaller chunks
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    
    chunks = text_splitter.split_text(text)

    return chunks