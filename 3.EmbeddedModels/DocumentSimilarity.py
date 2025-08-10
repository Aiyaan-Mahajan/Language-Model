# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np


# load_dotenv()


# embedding = OpenAIEmbeddings(model = 'text-embedding-3-large' , dimensions=300 )


# document = [
# "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
# "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
# "Sachin Tendulkar, also known as the 'God of Crisket', holds many batting records.",
# "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
# "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
# ]
# query ='tell me about virat kohli'

# document_embeddings= embedding.embed_documents(document)
# #yahan hame 5 vector ki list milengi

# query_embeddings = embedding.embed_query(query)
# #yaha hame ek vector milega

# print(cosine_similarity([query_embeddings],document_embeddings))
# #  dono values 2d list banakar bhejo 

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

# Load API key from .env
load_dotenv()

# Initialize Gemini embeddings (this uses Google's API)
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Example documents
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "tell me about Rohit Sharma"

# Generate embeddings
document_embeddings = embedding.embed_documents(documents)
query_embeddings = embedding.embed_query(query)

# Compute cosine similarity
scores = cosine_similarity([query_embeddings], document_embeddings)[0]
# ab yeh 1d list dega aur isse enumerate funcn mai bhejo aur output ko list mai daaldo  

index,score=sorted(list(enumerate(scores)),key = lambda x:x[1])[-1]
#highest similarity score miljayega aur kis index par hai woh document woh bhi pata chaljayega
print(query)
print(documents[index])
print("similarity score is :",score)

#hum semantic search karke sabse similar documnet ai usko nikalkar laa rahe hain jab hum RAG BASED KAAM KARTE HAIN

#In the next lectures we will use vector database