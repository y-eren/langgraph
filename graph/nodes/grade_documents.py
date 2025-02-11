from typing import Any, Dict
from graph.chains.retrieval_grader import retrieval_grade
from graph.state import GraphState


def grade_documents(state: GraphState) -> Dict[str, Any]:
    """
       Determines whether the retrieved documents are relevant to the question
       If any document is not relevant, we will set a flag to run web search

       Args:
           state (dict): The current graph state

       Returns:
           state (dict): Filtered out irrelevant documents and updated web_search state
       """
    print("----CHECK DOCUMENT RELEVANT TO QUESTİON")
    documents = state["documents"]
    question = state["question"]

    relevant_docs = []
    web_search  = False
    for d in documents:
        score = retrieval_grade.invoke({
            "question": question,
            "document": d.page_content
        })
        grade = score.binary_score

        if grade.lower() == "yes":
            print("---- GRADE DOCUMENT RELEVANT TO QUESTION")
            relevant_docs.append(d)
        else:
            print("---- DOCUMENT NOT RELEVANT TO QUESTION")
            web_search = True
            continue
    return {"documents": relevant_docs, "question": question, "web_search": web_search}