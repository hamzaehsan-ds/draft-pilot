import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent



load_dotenv(".env")

llm = init_chat_model(
    model=os.environ.get("DRAFT-PILOT_LLM_MODEL"),
    temperature=0.3,
    api_key=os.environ.get("GOOGLE_GENAI_API_KEY"),
    thinking_level="medium",
)


agent = create_agent(
    model=llm,
    tools=[],
    system_prompt=""
)

q = input("Query:")
response = llm.invoke(q)
print(response.text)