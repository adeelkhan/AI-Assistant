from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

key = os.environ["GOOGLE_API_KEY"]
model = "gemini-2.0-flash"
llm = ChatGoogleGenerativeAI(model=model, temperature=0.9)