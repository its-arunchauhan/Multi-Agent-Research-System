from src.agents.agents import writer_chain

result = writer_chain.invoke(
    {
        "topic": "AI in Healthcare",
        "research": """
AI improves diagnostics.
AI helps doctors analyze medical images.
AI accelerates drug discovery.
"""
    }
)

print(result)