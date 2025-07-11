from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import chain


template = ChatPromptTemplate.from_messages(

    [
        ('system', "You are a helpful assistant."),
        ('human', "{question}")
    ]

)

model = ChatOllama(
    model="gemma3:4b",
    temperature=0.8
)

# Combine them using a chain decorator in langchain
@chain
def chatbot(values):
    prompt = template.invoke(values)
    for token in model.invoke(prompt):
        yield token


for token in chatbot.stream(

    {
        "question": "How are you doing?"
    }

):
    print(token)