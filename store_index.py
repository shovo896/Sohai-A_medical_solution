from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
import os 
from dotenv import load_dotenv



load_dotenv()

from src.helper import load_pdf_files, filter_to_minimal_docs, text_split, download_embeddings
# load api key from .env file
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

dextracted_data=load_pdf_files(data="data/")
filter_data=filter_to_minimal_docs(dextracted_data)
texts_chunk=text_split(filter_data)

embeddings=download_embeddings()
# initialize pinecone client





