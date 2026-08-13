import os 
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.messages import HumanMessage,AIMessage


load_dotenv()
## controlling the temperature helps to tell the model the way of creativity and rationnal te answer would be

agent=create_agent(model="o3-mini")

for token,metadata in agent.stream(
        {
            "messages": [HumanMessage(content="what could you say about capital of morroco")
                        ,AIMessage(content="capital RABAT if you need more info tell me ")]
        },
        stream_mode="messages",
    ):
    print(token.content ,end="",flush=True) # type: ignore
        


