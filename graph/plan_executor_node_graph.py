from langgraph.graph import StateGraph
from single_task_execute_graph import create_single_task_execute_graph
from agents import StepDefinerAgent


def create_plan_executor_node_graph():

    plan_executor_node_graph = StateGraph()
    single_task_execute_graph = create_single_task_execute_graph()

    plan_executor_node_graph.add_node("task_definer", StepDefinerAgent)
    plan_executor_node_graph.add_node(
        "single_task_execute_graph", single_task_execute_graph
    )

    return plan_executor_node_graph.compile()


def decide_next_node(state):
    if state["some_condition"]:
        return "back to task_definer"
    else:
        return "finish"
