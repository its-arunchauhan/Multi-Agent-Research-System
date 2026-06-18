from src.tools.tools import web_search, scrape_url

print("="*50)
print("Testing web_search")
print("="*50)

search_result = web_search.invoke({
    "query": "Latest AI news"
})

print(search_result[:1000])

print("\n" + "="*50)
print("Testing scrape_url")
print("="*50)

url = "https://blog.google/innovation-and-ai/"

scrape_result = scrape_url.invoke({
    "url": url
})

print(scrape_result[:1000])