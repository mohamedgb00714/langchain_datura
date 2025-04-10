import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser

from langchain_datura.tools import DesearchTool
from langchain_deepseek import ChatDeepSeek  # ✅ using DeepSeek

# Load environment variables
load_dotenv()

# Setup Desearch Tool
desearch_tool = DesearchTool()

# Template to wrap Desearch output
document_prompt = PromptTemplate.from_template("""
<source>
    <result>{result}</result>
</source>
""")

# Retrieval chain using DesearchTool
def get_desearch_context(prompt: str) -> str:
    return desearch_tool._run(prompt=prompt, tool="desearch_web", model="NOVA")

retrieval_chain = RunnableLambda(lambda query: {
    "result": get_desearch_context(query)
}) | document_prompt | (lambda docs: docs.text)

# Prompt for RAG generation
generation_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research assistant. You use xml-formatted context to research people's questions."),
    ("human", """
Please answer the following query based on the provided context. Please cite your sources at the end of your response.:

Query: {query}
---
<context>
{context}
</context>
""")
])

# Use DeepSeek for LLM
llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0.7,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

output_parser = StrOutputParser()

# Final chain
chain = RunnableParallel({
    "query": RunnablePassthrough(),
    "context": retrieval_chain,
}) | generation_prompt | llm | output_parser

# Run it!
if __name__ == "__main__":
    query = "Recent trends in AI safety research"
    print(f"🔍 Query: {query}\n")

    result = chain.invoke(query)
    print("📄 Result:\n")
    print(result)
