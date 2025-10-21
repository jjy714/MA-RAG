from langgraph.graph import START, END, StateGraph
from agent import PlannerAgent
from graph import create_plan_executor_node_graph, create_single_task_execute_graph



# plan_executor_node_graph = 

def create_MA_RAG_graph(state):
    
    MA_RAG_graph = StateGraph()
    
    MA_RAG_graph.add_node("START", START)
    MA_RAG_graph.add_node("Planner Agent", PlannerAgent)
    
    MA_RAG_graph.add_edge(START, PlannerAgent)
    
    
    MA_RAG_workflow = MA_RAG_graph.compile()
    
    result = MA_RAG_workflow.invoke(state)
    
    return result 