from graph.chains.generation import generation_chain
from graph.state import GraphState
from typing import Dict, Any


def generate(state : GraphState) -> Dict[str, Any]:

    print("------GENERATE----")

    question = state["question"]
    documents = state["documents"]
    generation = generation_chain.invoke({
       "context" : documents,
       "question" : question
    })

    return {"question" : question, "generation" : generation, "documents" : documents}