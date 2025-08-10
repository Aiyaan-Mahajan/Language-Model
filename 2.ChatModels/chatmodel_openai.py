from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model= 'gpt-4o-mini')
result = model.invoke("What is the national animal of India")
print(result.content)

#OPEN_API_KEY is paid so you need to add credits by having a recharge of at least 5 dollars
#  and the code is completely fine it is just you need to have a paid api unlike gemini