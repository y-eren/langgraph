from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Literal

class Rooter(BaseModel):
    """
    Route a user query to the most relevant datasource
    """

    datasource : Literal["vectorstore", "websearch"] = Field(..., description="Given a user question choose to route it to web search or vectorstore")


llm = ChatOpenAI(temperature=0)
structured_llm_router = llm.with_structured_output(Rooter) # böylelikle llm'in verdiği cevabı belirli bir şablonda alması sağlanmış oluyor

system_prompt = """
You are an expert at routing a user question to a vectorstore or web search. 
The vectorstore contains documents related to agents, prompt engineering and adversarial attacks on llms.
Use the vectorstore for questions on these topics. For all else, use web-search.
"""

route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system",  system_prompt),
        ("human", "{question}")

    ]
)

question_router = route_prompt | structured_llm_router

