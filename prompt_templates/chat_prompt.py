from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama


model = ChatOllama(model="deepseek-r1:latest")
chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage("You are a professional helpful translator assistant."),
        HumanMessagePromptTemplate.from_template("Translate this sentence into {language} : {input_text}")
    ]
)
chat_prompt = chat_template.format_messages(language="Spanish", input_text="Hello, I am doing fine. What about you?")

response = model.invoke(chat_prompt)
print(response.content)