
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter   
from typing import List
from langchain.schema import Document
from langchain_community.embeddings import HuggingFaceEmbeddings




def load_pdf_files(data):
    loader = DirectoryLoader(data, glob="**/*.pdf", loader_cls=PyPDFLoader, show_progress=True)
    documents = loader.load()
    return documents


def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    """
    Given a list of documents objects return a new list of documents objects containing only the page_content and metadata fields.
    """
    minimal_docs: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source", "")
        minimal_docs.append(Document(page_content=doc.page_content, metadata={"source": src}))
    return minimal_docs

## text splitter to split the documents into smaller chunks to fit into the context window of the language model
    
    
def text_split(minimal_docs):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200)
    
    texts_chunk=text_splitter.split_documents(minimal_docs)
    return texts_chunk



