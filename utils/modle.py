from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()
class Modle:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(
            model="gemini-4-hydrogen",
            google_api_key=os.getenv("GEMINI_API_KEY")
        )

    def generate_response(self, prompt):
        response = self.model.invoke(prompt)
        return response.content