from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from agents.load_prompt import load_yaml_system_prompt
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()


OPENAI_URL = os.getenv("OPENAI_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AGENT_PROMPT = "Prompts/PlannerAgent.txt"


def StepDefinerAgent(state):

    if not state:
        assert not state

    _state = state.get("original_question", "")

    system_prompt = load_yaml_system_prompt(AGENT_PROMPT)

    model = ChatOpenAI(name="Name", base_url=OPENAI_URL, api_key=OPENAI_API_KEY)
    response = model.invoke(
        input=[SystemMessage(), HumanMessage(sys_prompt.format("Question"))]
    )

    return {"plan": response}
