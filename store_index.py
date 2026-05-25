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

pinecone_api_key=PINECONE_API_KEY
pinecone = Pinecone(api_key=pinecone_api_key) 


index_name = "medical-chatbot"
pinecone_cloud = os.getenv("PINECONE_CLOUD", "aws")
pinecone_region = os.getenv("PINECONE_REGION", "us-east-1")

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud=pinecone_cloud, region=pinecone_region),
    )
index = pc.Index(index_name)





doc_search = PineconeVectorStore.from_documents(documents=text_chunks, embedding=embeddings, index_name=index_name)






