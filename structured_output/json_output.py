from langchain_ollama import ChatOllama
from pydantic import BaseModel

# class AnswerWithJustification(BaseModel):
#     '''An answer to the user's question along with justification for the answer'''
#     answer: str
#     '''The answer to the user's question'''
#     justification: str
#     '''Justification for the answer'''


class AnswerWithJustification(BaseModel):
    '''An answer to the user's topic along with a rhyming poem of the answer'''
    answer: str
    '''The answer to the user's query'''
    poem: str
    '''Poem on the user's query answer'''


model = ChatOllama(
    model="gemma3:4b"
)

structured_llm = model.with_structured_output(AnswerWithJustification)

response = structured_llm.invoke("Tell me about Mars.")

with open('poem.json', 'w+') as f:
    f.write(response.model_dump_json())
