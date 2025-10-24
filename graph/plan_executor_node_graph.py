from langgraph.graph import StateGraph, END
from typing import Literal
from single_task_execute_graph import create_single_task_execute_graph
from state import RagState, PlanExecState
from agents import StepDefinerAgent



def single_task_execute_node():
    single_task_execute_graph = create_single_task_execute_graph()
    result = single_task_execute_graph.invoke(RagState)
    return result

def exit_router(state: PlanExecState) -> bool:
    return state["stop"]


def create_plan_executor_node_graph():

    plan_executor_node_graph = StateGraph()
    
    plan_executor_node_graph.add_node("task_definer", StepDefinerAgent)
    plan_executor_node_graph.add_node(
        "single_task_execute_node", single_task_execute_node
    )
    
    
    plan_executor_node_graph.add_conditional_edges(
        "task_definer",
        exit_router,
        {
            False: "plan_executor_node_graph",
            True : END,
        }
    )
    

    

    return plan_executor_node_graph.compile()


def decide_next_node(state):
    if state["some_condition"]:
        return "back to task_definer"
    else:
        return "finish"
