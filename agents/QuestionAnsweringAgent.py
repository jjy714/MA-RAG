from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from pathlib import Path
from dotenv import load_dotenv
from agents.load_prompt import load_yaml_system_prompt
import os

load_dotenv()


OPENAI_URL = os.getenv("OPENAI_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AGENT_PROMPT = "Prompts/QuestionAnsweringAgent.yaml"


def QuestionAnsweringAgent(state):

    if not state:
        assert not state

    _state = state.get("original_question", "")

    prompt = load_yaml_system_prompt(AGENT_PROMPT)
    chat_template = ChatPromptTemplate(prompt["messages"])

    model = ChatOpenAI(name="Name", base_url=OPENAI_URL, api_key=OPENAI_API_KEY)
    response = model.invoke(
        input=[SystemMessage(system_prompt), HumanMessage(user_prompt.format())]
    )

    return {"plan": response}
