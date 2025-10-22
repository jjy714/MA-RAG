from graph import create_MA_RAG_graph
from state import GraphState





def main():
    
    main_graph = create_MA_RAG_graph()
    result = main_graph.invoke(GraphState)
    
    print(f"RESULT: {result}")
    return result

if __name__ == "__main__":
    main()
