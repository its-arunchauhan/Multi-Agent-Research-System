# from src.pipelines.pipeline import run_research_pipeline
from src.tools.tools import web_search, scrape_url

result = scrape_url(" https://www.nytimes.com/spotlight/artificial-intelligence")
print(result)
# topic = "The impact of AI on the job market in 2026"
# run_research_pipeline(topic)