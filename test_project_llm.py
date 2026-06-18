from src.agents.agents import llm

response = llm.invoke(
    "What are AI agents?"
)

print(response.content)