from graph.node_constants import RETRIEVE, GENERATE, WEBSEARCH, GRADE_DOCUMENTS
from graph.nodes import generate, grade_documents, web_search, retrieve
from graph.chains.rooter import question_router, Rooter
from graph.chains.halucination_grader import hallucination_grader
from graph.chains.answer_grader import answer_grader
from langgraph.graph import StateGraph, END
from dotenv import load_dotenv


from graph.state import GraphState

load_dotenv()

def decide_to_generate(state: GraphState):
    print("-----ASSESS GRADED DOCUMENTS-----")

    if state["web_search"]:
        print("Web Search")
        return WEBSEARCH

    else:
        return GENERATE

def grade_generation_grounded_in_documents_and_questions(state: GraphState):
    print("-----CHECK HALLUCINATION GRAPH-----")
    question = state["question"]
    generation = state["generation"]
    documents = state["documents"]

    score = hallucination_grader.invoke(
        {"documents": documents,"generation": generation}
    )

    if score.binary_score is not None:
        if score.binary_score.lower() == "yes":
            print("GENERATION IS GROUNDED ON DOCUMENT")
            score = answer_grader.invoke(
                {"question": question,"generation": generation}
            )
            if score.binary_score.lower() is not None:
                if score.binary_score == "yes":
                    print("GENERATION ADDRESSES QUESTION")
                    return "useful" #nodelar içinde ende götürmek için herhangi bir string döndürülmektedir
                else:
                    print("GENERATION DOES NOT GROUNDED ON DOCUMENT")
                    return "not useful"
            else:
                print("GENERATION DOES NOT GROUNDED ON DOCUMENT")
                return "not supported" # halüsinasyon görüyor

def route_question(state : GraphState) -> str:
    print("-----ROUTE QUESTION-----")
    question = state["question"]
    source = question_router.invoke({"question": question})

    if source.datasource == "websearch":
        return WEBSEARCH
    else:
        return RETRIEVE



workflow = StateGraph(GraphState)

workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node(GENERATE, generate)
workflow.add_node(WEBSEARCH, web_search)


workflow.set_conditional_entry_point(
    route_question,
    {
        WEBSEARCH : WEBSEARCH,
        RETRIEVE: RETRIEVE,
    }
)
workflow.add_edge(RETRIEVE, GRADE_DOCUMENTS)

workflow.add_conditional_edges(
    GRADE_DOCUMENTS,
    decide_to_generate,
    {WEBSEARCH : WEBSEARCH,
     GENERATE : GENERATE}

)

workflow.add_conditional_edges(
    GENERATE,
    grade_generation_grounded_in_documents_and_questions,
    {
        "not supported" : GENERATE,
        "useful" : END,
        "not useful" : WEBSEARCH
    }
)

workflow.add_edge(WEBSEARCH, GENERATE)
workflow.add_edge(GENERATE, END)

app = workflow.compile()
app.get_graph().draw_mermaid_png(output_file_path="graph.png")