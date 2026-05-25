from flask import Flask, request, jsonify, render_template
from src.helper import download_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
from src.prompt import *

app=Flask(__name__)
load_dotenv()

# load api key from .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY


embeddings=download_embeddings()
index_name = "medical-chatbot"
docsearch=PineconeVectorStore(embedding_function=embeddings, index_name=index_name)


retriever=docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})








