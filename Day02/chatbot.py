from openai import OpenAI   #python to access openAI SDK
from dotenv import load_dotenv  #lets python read variables from .env
import os   #used to retrieve api key

load_dotenv()   #this will load .env

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)   #this retrieves the value of API key

try:
    response = client.responses.create(
        model="gpt-5.6-luna",
        input="Explain Python functions to a beginner."
    )   #API request

    print(response.output_text)

except Exception as e:
    print("An error occurred:")
    print(e)