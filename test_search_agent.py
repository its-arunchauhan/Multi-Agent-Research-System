from src.agents.agents import build_search_agent

agent = build_search_agent()

response = agent.invoke(
    {
        "messages": [
            (
                "user",
                "Find recent information about AI agents"
            )
        ]
    }
)

for msg in response["messages"]:
    print(type(msg).__name__)
    print(msg)
    print("-"*80)