from langchain_ollama import ChatOllama

model = ChatOllama(
    model="gemma3:4b"
)

response = model.invoke("HI, there")
print(response)