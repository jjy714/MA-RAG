
from typing import TypedDict, List, Annotated
from PlanExecState import PlanExecState
import operator


class GraphState(TypedDict): 
    original_question: str 
    plan: List[str] 
    past_exp: Annotated[List[PlanExecState], operator.add] 
    final_answer: str