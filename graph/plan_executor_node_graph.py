from langgraph.graph import StateGraph
from single_task_execute_graph import create_single_task_execute_graph
from agents import StepDefinerAgent

def create_plan_executor_node_graph():
    
    plan_executor_node_graph = StateGraph()
    single_task_execute_graph = create_single_task_execute_graph()
    
    plan_executor_node_graph.add_node("task_definer", StepDefinerAgent)
    plan_executor_node_graph.add_node("single_task_execute_graph", single_task_execute_graph)
    
    
    
def decide_next_node(state):
    if state["some_condition"]:
        return "back to task_definer"
    else:
        return "finish"

    
def single_task_router(satet):
    

     graph.add_conditional_edges(
        "source_node",  # Source node
        decide_next_node,  # Routing function
        {
            "node_A": "node_A",  # Map routing function output to node name
            "node_B": "node_B",
            # Optionally, map to END to terminate
            # "terminate_condition": END
        }
    )
    plan_executor_node_graph.add_conditional_edges(
        "task_definer",
        decide_next_node,
        {
            "back to task_definer": "task_definer", 
            "END"
        }
        
        
        
    )
    
    return plan_executor_node_graph.compile()