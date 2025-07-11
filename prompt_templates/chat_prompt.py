from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert translator that replies with 2 excalamation marks at the end."),
        ("human", "Translate this to {language}: {input_text}")
    ]
)
chat_prompt = chat_template.format_messages(language="Spanish", input_text="Hello, I am doing fine. What about you?")
print(chat_prompt)