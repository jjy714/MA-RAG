from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()


OPENAI_URL=os.getenv("OPENAI_URL")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
AGENT_PROMPT=Path("Prompts/PlannerAgent.txt")

def PlannerAgent(state):
    
    if not state: 
        assert(not state)
    
    _state = state.get("original_question", "")
    
    with open(str(AGENT_PROMPT), "r") as f:
        sys_prompt=f.read()
    
    model = ChatOpenAI(
        name="Name",
        base_url=OPENAI_URL,
        api_key=OPENAI_API_KEY
    )
    response = model.invoke(
        input=[
            SystemMessage(),
            HumanMessage(sys_prompt.format("Question"))
        ]
    )

    return {"plan": response}