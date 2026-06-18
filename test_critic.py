from src.agents.agents import critic_chain

report = """
AI improves diagnostics.
AI helps doctors analyze medical images.
AI accelerates drug discovery.
"""

result = critic_chain.invoke(
    {
        "report": report
    }
)

print(result)