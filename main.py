from graph import create_MA_RAG_graph
from typing import List, Annotated
import operator
from state import GraphState, PlanExecState


def main():
    graph_input = create_input_payload(evaluation_request)
    input: GraphState = {
        "original_question": [],
        "plan": List[str],
        "past_exp": Annotated[List[PlanExecState], operator.add],
        "final_answer": str,
    }
    main_graph = create_MA_RAG_graph()
    result = main_graph.invoke(graph_input)

    print(f"RESULT: {result}")
    return result


if __name__ == "__main__":
    main()
