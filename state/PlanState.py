from typing import TypedDict, List


class PlanState(TypedDict): 
    analysis: str
    step: List[str]