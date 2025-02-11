from typing import List, TypedDict

class GraphState(TypedDict): # typeddict ile sözlük olarak tanımlamış oluyoruz
    question: str
    generation: str
    web_search: bool
    documents: List[str]