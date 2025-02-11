from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field


llm = ChatOpenAI(temperature=0)

class GradeDocuments(BaseModel):
    """Binary score for relevance check on retrieved documents"""

    binary_score : str = Field(
        description="Documents are relevant to the question, 'yes' or 'no' "
    )

structured_llm_router = llm.with_structured_output(GradeDocuments) # output gradedoucmentsa göre yapmaktadır

system_prompt = """
You are a grader assessing relevance of a retrieved document to a user question. \n 
If the document contains keyword(s) or semantic meaning related to the question, grade it as relevant. \n
Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question.
"""

grade_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "Retrieved document: {document} User question : {question}")
    ]
)

retrieval_grade = grade_prompt | structured_llm_router



# if __name__ == "__main__":
#     user_question = "what is prompt engineering?"
#     docs = retriever.get_relevant_documents(user_question)
#     retrieved_documents = docs[0].page_content
#     print(retrieval_grade.invoke({
#         "question": user_question, "document": retrieved_documents
#     }))