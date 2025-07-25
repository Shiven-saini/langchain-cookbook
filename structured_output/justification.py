from langchain_deepseek import ChatDeepSeek
from langchain_ollama import ChatOllama
from pydantic import BaseModel
from dotenv import load_dotenv, find_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
import os

# Find and load the environment variables
load_dotenv(find_dotenv())

api_key=os.getenv("DEEPSEEK_API_KEY")


# Creating the chat interface with Deepseek-v3
model_deepseek = ChatDeepSeek(
    model="deepseek-chat",
    api_key=api_key
)


# Defining the Pydantic desired output schema.
class BooleanWithJustification(BaseModel):
    '''A single word TRUE or FALSE answer to the user question.'''
    answer: bool
    '''The single word answer to the user's query: TRUE or FALSE'''
    justification: str
    '''Justification about your answer.'''


structured_llm = model_deepseek.with_structured_output(BooleanWithJustification)


response = structured_llm.invoke("Stephen Hawking was a greatest athletic to have ever walked on this planet.")
print(response.model_dump_json())