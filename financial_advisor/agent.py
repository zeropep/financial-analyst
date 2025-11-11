from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

MODEL = LiteLlm("openai/gpt-4o")

agent = Agent(
    name="WeatherAgent",
    instruction="You help the user with weather related questions.",
    model=MODEL,
)

# "root_agent" is mandatory
root_agent = agent