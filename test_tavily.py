from src.tools.tools import web_search

result = web_search.invoke({
    "query": "Latest AI news"
})

print(result)