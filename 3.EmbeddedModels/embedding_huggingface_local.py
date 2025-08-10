from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# text ="agra used to be the capital of india"

text =[
    "Tell me the plot of The movie notebook",
    "How many colleges are there in India",
    "who is narendra Modi"
]
vector=embedding.embed_documents(text)

print(str(vector))

#you need to install sentence-transformers package 
#run this command in the terminal 👇🏻
# pip install sentence-transformers

#in output we will get 384 dimensional vector