from src.agents.agents import build_search_agent

agent = build_search_agent()

print("Agent created")

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Latest AI news"
            }
        ]
    }
)

print(response)