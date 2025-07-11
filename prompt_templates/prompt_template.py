from langchain_core.prompts import PromptTemplate

template = "Translate the following text to {language}:\n\n{input_text}"
prompt = PromptTemplate.from_template(template)

actual_prompt = prompt.format(
    language="french",
    input_text="Hello, how are you?"
)

print(actual_prompt)

"""
OUTPUT: 
Translate the following text to french:

Hello, how are you?
"""