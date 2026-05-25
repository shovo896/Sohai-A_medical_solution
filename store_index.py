from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
import os 
from dotenv import load_dotenv



load_dotenv()

from src.helper import load_pdf_files, filter_to_minimal_docs, text_split, download_embeddings


