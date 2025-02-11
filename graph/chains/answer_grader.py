from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field



class AnswerGrader(BaseModel):

    binary_score : str = Field(
        description="The binary score of the answer.",
    )

llm = ChatOpenAI(temperature=0)
structured_llm_grader = llm.with_structured_output(AnswerGrader)

system = """
You are a grader assessing whether an answer addresses / resolves a question \n 
     Give a binary score 'yes' or 'no'. Yes' means that the answer resolves the question.
"""

answer_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "User question: \n\n {question} \n\n LLM generation: {generation}"),
    ]
)

answer_grader = answer_prompt | structured_llm_grader