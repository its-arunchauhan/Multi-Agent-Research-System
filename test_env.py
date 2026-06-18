from dotenv import load_dotenv
import os

load_dotenv()

print("OPENAI:", os.getenv("OPENAI_API_KEY"))
print("TAVILY:", os.getenv("TAVILY_API_KEY"))