from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage


model = ChatOllama(
    model="gemma3:4b"
)

prompt = [

    SystemMessage("You are a helpful assistant that responds to questions with three exclamation marks."),
    HumanMessage("Which person has won the most gold medals in olympic ?")

]

response = model.invoke(prompt)

print(response.content)