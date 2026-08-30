from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

try:
    response = client.responses.create(
        model="gpt-5.6-luna",
        input="Explain Python functions to a beginner."
    )

    print(response.output_text)

except Exception as e:
    print("An error occurred:")
    print(e)