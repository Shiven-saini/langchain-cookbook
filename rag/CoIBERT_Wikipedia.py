from ragatouille import RAGPretrainedModel
import requests


RAG = RAGPretrainedModel.from_pretrained("pylate/colbertv2.0")

def get_wikipedia_page(title: str):
    """
    Retrieve the full text content of a Wikipedia page.

    :param title: str - Title of the Wikipedia page.
    :return: str - Full text content of the page as raw string.
    """
    # Wikipedia API endpoint
    URL = "https://en.wikipedia.org/w/api.php"

    # Parameters for the API request
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "extracts",
        "explaintext": True,
    }

    # Custom User-Agent header to comply with Wikipedia's best practices
    headers = {"User-Agent": "RAGatouille_tutorial/0.0.1"}

    response = requests.get(URL, params=params, headers=headers)
    data = response.json()

    # Extracting page content
    page = next(iter(data["query"]["pages"].values()))
    return page["extract"] if "extract" in page else None


user_query = input("Enter the topic you want to explore about => ")
full_document = get_wikipedia_page(user_query)

## Create an index
RAG.index(
    collection=[full_document],
    index_name="wiki-123",
    max_document_length=180,
    split_documents=True,
)


# results = RAG.search(query="What animation studio did Miyazaki found?", k=3)


#utilize langchain retriever
retriever = RAG.as_langchain_retriever(k=3)
while True:
    user_query = input("Enter your query => ")
    response = retriever.invoke(user_query)
    print(response)