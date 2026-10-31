from langchain.agents import create_agent
from langgraph.checkpoint.postgres import PostgresSaver

from app.agent import SYSTEM, llm
from app.config import DB_URI
from app.tools import get_today_date


def main() -> None:
    if not DB_URI:
        raise SystemExit("DB_URI is missing. Add it to your .env file.")

    with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
        checkpointer.setup()
        agent = create_agent(
            model=llm,
            tools=[get_today_date],
            system_prompt=SYSTEM,
            checkpointer=checkpointer,
        )

        thread_id = input("Conversation name: ").strip()
        thread_config = {"configurable": {"thread_id": thread_id}}

        while True:
            query = input("You: ").strip()
            if query.lower() in ("quit", "exit", "bye"):
                break

            result = agent.invoke(
                {"messages": [{"role": "user", "content": query}]},
                config=thread_config,
            )
            print("Draft-Pilot:", result["messages"][-1].text)


if __name__ == "__main__":
    main()