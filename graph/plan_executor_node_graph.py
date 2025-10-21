from langgraph.graph import StateGraph
from agent import Task

def create_plan_executor_node_graph(state):
    
    plan_executor_node_graph = StateGraph()
    plan_executor_node_graph.add_node("task_definer", )
    plan_executor_node_workflow = plan_executor_node_graph.compile()
    
    result = plan_executor_node_workflow.invoke(state)
    
    return result 