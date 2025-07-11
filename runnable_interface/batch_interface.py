from langchain_ollama import ChatOllama

model = ChatOllama(
    model="gemma3:4b"
)

completion = model.invoke("Hi there!")
completion_batch = model.batch(["Hi there!", "What's your name"])

for i in completion_batch:
    print(i.content)
    print('='*30)