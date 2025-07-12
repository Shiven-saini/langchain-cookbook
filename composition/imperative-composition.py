from langchain_ollama import ChatOllama
from langchain_core.runnables import chain
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate


model = ChatOllama(model="gemma3:4b")

template = ChatPromptTemplate.from_messages(

    [
        ('system', "You are a helpful assistant."),
        ('user', "{question}")
    ]

)

# Combining the template and model together in a function
@chain
def process_input(value):
    prompt = template.invoke(value)
    return model.invoke(prompt)

response = process_input.invoke({"question" : "What is a quasar?"})

print(response.content)

