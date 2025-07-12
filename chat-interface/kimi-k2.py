from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="moonshotai/kimi-k2-instruct",
    api_key="sk_EHrdHHP2o_fqvtVIAujtUJH_2YfOF4B7IW_zHxBSjvU",
    base_url="https://api.novita.ai/v3/openai"
)

response = model.invoke("Tell me about Moon. Especially about it's far side.")

print(response.content)