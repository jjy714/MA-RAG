from typing import TypedDict, List, Annotated
from QAanswerState import QAAnswerState
from StepTasksState import StepTaskState
from PlanSummaryState import PlanSummaryState
import operator



class PlanExecState(TypedDict): 
    original_question: str 
    plan: List[str] 
    step_question: Annotated[List[StepTaskState], operator.add] 
    step_output: Annotated[List[QAAnswerState], operator.add] 
    step_docs_ids: Annotated[List[List[str]], operator.add] 
    step_notes: Annotated[List[List[str]], operator.add] 
    plan_summary: PlanSummaryState 
    stop: bool = False