import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv(".env")

llm = init_chat_model(
    model=os.getenv("DRAFT-PILOT_LLM_MODEL"),
    temperature=0.3,
    api_key=os.getenv("GOOGLE_GENAI_API_KEY"),
    thinking_level="medium",
)

system_prompt = "You are a helpful email assistant."
agent = create_agent(
    model=llm,
    tools=[],
    system_prompt=system_prompt,
    checkpointer=InMemorySaver(),
)

user_id = input("Conversation name: ")
thread_con = {"configurable": {"thread_id": user_id}}

while True:
    q = input("You: ")
    if q.lower() in ("quit", "bye", "exit"):
        break
    result = agent.invoke(
        {"messages": [{"role": "user", "content": q}]},
        config=thread_con,
    )
    print("Agent:", result["messages"][-1].text)
