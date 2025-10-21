from langgraph.graph import START, END, StateGraph




def create_single_task_execute_graph(state):
    
    single_task_execute_graph = StateGraph()
    
    single_task_execute_workflow = single_task_execute_graph.compile()
    
    result = single_task_execute_workflow.invoke(state)
    
    return result 