from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

model = ChatOllama(
    model="gemma3:4b"
)

# prompt = """Answer the question based only on the context below. If the question cannot be
# answered using the information & context provided even if you know, answer with "I don't know".

# Context: The most recent advancements in NLP are being driven by Large Language Models (LLMs). These models outperform their smaller counterparts and have
# become invaluable for developers who are creating applications with NLP 
# capabilities. Developers can tap into these models through Hugging Face's
# `transformers` library, or by utilizing OpenAI and Cohere's offerings through
# the `openai` and `cohere` libraries, respectively.

# Question: What is transformers library?

# Answer:

# """

#=======Above Prompt is hardcoded=========#


# template = PromptTemplate.from_template(

#     """Answer the question based only on the context below. If the question cannot be
#     answered using the information & context provided even if you know, answer with "I don't know".

#     Context: {context}

#     Question: {question}

#     Answer:
#     """
# )

# prompt = template.invoke(

#     {
#         'context' : """The most recent advancements in NLP are being driven by Large Language Models (LLMs). These models outperform their smaller counterparts and have
# become invaluable for developers who are creating applications with NLP 
# capabilities. Developers can tap into these models through Hugging Face's
# `transformers` library, or by utilizing OpenAI and Cohere's offerings through
# the `openai` and `cohere` libraries, respectively.""",

#         'question' : 'What became invaluable to developers?'

#     }

# )

# chain = template | model

# response = chain.invoke(

#     {
#         'context' : """The most recent advancements in NLP are being driven by Large Language Models (LLMs). These models outperform their smaller counterparts and have
# become invaluable for developers who are creating applications with NLP 
# capabilities. Developers can tap into these models through Hugging Face's
# `transformers` library, or by utilizing OpenAI and Cohere's offerings through
# the `openai` and `cohere` libraries, respectively.""",

#         'question' : 'What became invaluable to developers?'

#     }

# )


template = ChatPromptTemplate.from_messages(

    [
        ('system', "Answer the question based only on the context below. If the question cannot be answered using the information & context provided even if you know, answer with 'I don't know'"),
        ('human', "Context : {context}"),
        ('human', "Question: {question}")
    ]

)

# prompt = template.invoke(
    
#     {
#         "context" : """The most recent advancements in NLP are being driven by Large Language Models (LLMs). These models outperform their smaller counterparts and have become invaluable for developers who are creating applications with NLP 
# capabilities. Developers can tap into these models through Hugging Face's`transformers` library, or by utilizing OpenAI and Cohere's offerings through the `openai` and `cohere` libraries, respectively.""",
#     'question' : "What is Cohere?"
#     }

# )

chain = template | model

response = chain.invoke(
    
    {
        "context" : """The most recent advancements in NLP are being driven by Large Language Models (LLMs). These models outperform their smaller counterparts and have become invaluable for developers who are creating applications with NLP 
capabilities. Developers can tap into these models through Hugging Face's`transformers` library, or by utilizing OpenAI and Cohere's offerings through the `openai` and `cohere` libraries, respectively.""",
    'question' : "What is Cohere?"
    }

)

print(response.content)