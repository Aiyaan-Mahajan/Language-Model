from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
#unlike other chatmodels we have to import 2 classes here ChatHuggingFace which is similar to other models, HuggingFaceEndpoint  this is included because we want to use HF api
from dotenv import load_dotenv
import os

# Load .env file for API keys
load_dotenv()

#llm parameter has to be added here by using HuggingFaceEndpoint
# Create LLM endpoint
llm=HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    
 )

model = ChatHuggingFace(llm=llm)


result = model.invoke("Who was the father of Jesus Christ")
print(result.content)