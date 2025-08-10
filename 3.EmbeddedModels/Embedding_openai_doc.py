from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

# Load environment variables (make sure GOOGLE_API_KEY is in your .env)
load_dotenv()

# Create the embeddings object for Gemini
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
documents =[
    "Delhi is the capital of india",
    "Kolkata is the capital of West bengal"
    "Paris is the capital of France"
]

# Generate embeddings for a query
result = embedding.embed_documents(documents)#embed_documents function has the capability to generate vectors of multiple queries

print(result)
#2d list of vectors output mai aayega
