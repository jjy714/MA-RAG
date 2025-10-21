from typing import TypedDict

class RagState(TypedDict): 
    question: str 
    documents: List[str] 
    doc_ids: List[str] 
    notes: List[str] 
    final_raw_answer: QAAnswerState
    