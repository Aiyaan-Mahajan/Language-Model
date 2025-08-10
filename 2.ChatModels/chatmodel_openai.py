from langchain_openai import ChatOpenAI  #basechatmodels class
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model= 'gpt-4o-mini')  #instance of basechatmodels class  and along with models you can also include temperature and max_token_limit .
#temperature should be 0 if you want things like code and if you want to do something creative it must be somewhere around 1.5 .
result = model.invoke("What is the national animal of India")
print(result.content)

#OPEN_API_KEY is paid so you need to add credits by having a recharge of at least 5 dollars
#  and the code is completely fine it is just you need to have a paid api unlike gemini
