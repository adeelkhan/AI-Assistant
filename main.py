"""
Summary: 
A simple chatbot that would act as a helpful assistant... 
Assistant has access to search, math etc... one can add more
tools in tools file to add more tooling to chabot.

"""
from model_loader import llm
from tools import chatbot_tools, selected_tool
from langchain_core.messages import HumanMessage, SystemMessage

def weather_tool(tool_func, location: str): 
  tool_msg = tool_func(tool_call["args"]["location"])
  return tool_msg
  

messages = []
messages.append(SystemMessage("You are helpful Assistant"))
llm_with_tools = llm.bind_tools(chatbot_tools)

user_query = input("Please ask me anything? ")
messages.append(HumanMessage(user_query))
response = llm_with_tools.invoke(messages)

for tool_call in response.tool_calls:
  tool = selected_tool[tool_call["name"].lower()]
  if tool_call["name"] == "run": # used for weather tool integration
    tool_msg = weather_tool(tool, tool_call["args"]["location"])
  else:
    tool_msg = tool.invoke(tool_call) # invoking the tools
  messages.append(tool_msg)  

response = llm.invoke(messages) # invoking llm 
print("Response: \n", response.content)
