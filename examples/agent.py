from langchain_datura.agent import AgentExecutor,create_search_agent
from langchain_deepseek import ChatDeepSeek
from langgraph.store.memory import InMemoryStore  # Use InMemoryStore instead of MemoryStore
from langchain.schema import HumanMessage

# Example usage
if __name__ == "__main__":
    # Create a DeepSeek LLM instance
    llm = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0.7,
        max_tokens=None,
        timeout=None,
        max_retries=2
    )
    
    # Initialize an in-memory store for the agent
    store = InMemoryStore()

    # Initialize the search agent with the DeepSeek LLM and in-memory store
    search_agent = create_search_agent(llm=llm)
    
    # Use the agent to perform a task
    input_query = "Find the  news about AI yesterday"
    state = {
    "input_message": "What's the latest news on AI?",
}
    response = search_agent.invoke(state)  # Pass the state directly
    # print(response)
    print(f"Agent Response: {response['output']}")
