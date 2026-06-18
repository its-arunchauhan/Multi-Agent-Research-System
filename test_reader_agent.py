from src.agents.agents import build_reader_agent

agent = build_reader_agent()

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Read and summarize https://blog.google/innovation-and-ai/"
            }
        ]
    }
)

print(response)
