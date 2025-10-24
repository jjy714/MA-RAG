from agents import PlannerAgent
from graph import create_plan_executor_node_graph
from state import PlanExecState, GraphState
from langgraph import START, END, StateGraph

# plan_executor_node_graph =

plan_execute_state = PlanExecState()


def plan_executor_node(state: GraphState):
    plan_executor_graph = create_plan_executor_node_graph(state["past_exp"])
    result = plan_executor_graph.invoke()
    return {"final_answer": result}

def create_MA_RAG_graph():

    MA_RAG_graph = StateGraph(GraphState)
    plan_executor_graph = create_plan_executor_node_graph()

    MA_RAG_graph.add_node("START", START)
    MA_RAG_graph.add_node("Planner Agent", PlannerAgent)
    MA_RAG_graph.add_node("plan_executor_graph", plan_executor_graph)

    MA_RAG_graph.add_edge("START", "Planner Agent")
    MA_RAG_graph.add_edge("Planner Agent", "plan_executor_graph")

    return MA_RAG_graph.compile()
