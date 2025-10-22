from langgraph.graph import START, END, StateGraph

from agents import ExtractorAgent



def create_single_task_execute_graph(state):
    
    single_task_execute_graph = StateGraph()

    single_task_execute_graph.add_node("retrieve", )
    single_task_execute_graph.add_node("extract", ExtractorAgent),
    single_task_execute_graph.add_node("generate", )
    single_task_execute_graph.add_node("END", END)
    
    single_task_execute_graph.add_edge("retrieve", "extract")
    single_task_execute_graph.add_edge("extract", "generate")
    single_task_execute_graph.add_edge("generate", "END")
    
    return single_task_execute_graph.compile()