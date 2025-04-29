from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document

def setup_vectorstore():
    embedding = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en",
        model_kwargs={"device": "cuda"},
        encode_kwargs={"normalize_embeddings": True}
    )
    
    # Initialize with empty documents
    docs = [
        Document(page_content="Sample text about India and Pakistan tension.",
                 metadata={"title": "India-Pakistan Conflict", "link": "https://example.com"})
    ]
    return FAISS.from_documents(docs, embedding)