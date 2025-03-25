from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
load_dotenv()
import os


if __name__ == '__main__':
    print('Hello World!')
    print(os.environ['OPENAI_API_KEY'])