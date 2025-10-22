from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
from agents.load_prompt import load_yaml_system_prompt
import os

load_dotenv()


OPENAI_URL=os.getenv("OPENAI_URL")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
AGENT_PROMPT="Prompts/PlannerAgent.txt"

def PlannerAgent(state):
    
    if not state: 
        assert(not state)
    
    prompt = load_yaml_system_prompt(AGENT_PROMPT)
    system_prompt = prompt['messages'][0].get("content","")
    user_prompt = prompt['messages'][1].get("content","")


    model = ChatOpenAI(
        name="Name",
        base_url=OPENAI_URL,
        api_key=OPENAI_API_KEY
    )
    
    response = model.invoke(
        input=[
            SystemMessage(system_prompt),
            HumanMessage(user_prompt.format(question="question" ))
        ]
    )

    return {"plan": response}