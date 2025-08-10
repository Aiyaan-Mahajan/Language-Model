from langchain_google_genai import ChatGoogleGenerativeAI #basechatmodels class
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-pro')#instance of basechatmodels class  and along with models you can also include temperature and max_token_limit .
#temperature should be 0 if you want things like code and if you want to do something creative it must be somewhere around 1.5 .
result = model.invoke('Who is the president of India')
print(result.content)
