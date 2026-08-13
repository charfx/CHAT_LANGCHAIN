from dotenv import load_dotenv
from langchain import agents
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
load_dotenv()
##the checkpointers need the configuration like the thread_id 
##remember that the agent need the tool even if they are empty 
## also define the LLM used not only the model
LLM=ChatOpenAI(model="o4-mini")
configurat={"configurable":{"thread_id":"1"}}
agent=create_agent(model=LLM,tools=[],checkpointer=InMemorySaver())


response=agent.invoke({"messages":[HumanMessage(content="my favorite color is red")]},configurat)
print(response["messages"][-1].content)

##second call to see the memory effect :
response2=agent.invoke({"messages":[HumanMessage(content="what is my favorite color")]},configurat)
print(response2["messages"][-1].content)