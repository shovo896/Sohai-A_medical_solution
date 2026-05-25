
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter   
from typing import List
from langchain.schema import Document
from langchain_community.embeddings import HuggingFaceEmbeddings




def load_pdf_files(data):
    loader = DirectoryLoader(data, glob="**/*.pdf", loader_cls=PyPDFLoader, show_progress=True)
    documents = loader.load()
    return documents



    
