from langchain_core.output_parsers import CommaSeparatedListOutputParser

parser = CommaSeparatedListOutputParser()

items = parser.invoke("Apple,Banana,Cherry,Tomato")
print(items)

"""
USECASE =>
Where the LLM provides some kind of json with CSV Values? We can parse it into a list object
and then apply logic programmatically.
"""