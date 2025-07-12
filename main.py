"""
Summary: 
A simple chatbot that would act as a helpful assistant... 
Assistant has access to search, math etc... one can add more
tools in tools file to add more tooling to chabot.

"""
from model_loader import llm
from tools import chatbot_tools, selected_tool
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from pprint import pprint

def weather_tool(tool_func, location: str): 
  tool_msg = tool_func(location)
  return tool_msg
  
messages = []
messages.append(SystemMessage("You are helpful Assistant"))
llm_with_tools = llm.bind_tools(chatbot_tools)

user_query = input("Please ask me anything? ")
messages.append(HumanMessage(user_query))
response = llm_with_tools.invoke(messages)
messages.append(response)

for tool_call in response.tool_calls:
  tool = selected_tool[tool_call["name"].lower()]
  if tool_call["name"] == "run":
    weather_result = weather_tool(tool, tool_call["args"]["location"])
    tool_msg = ToolMessage(
      name=tool_call["name"],
      tool_call_id=tool_call["id"],
      content=weather_result,
    )
  else:
    tool_msg = tool.invoke(tool_call) # invoking the tools
  messages.append(tool_msg) # appending tool message 

response = llm.invoke(messages) # invoking llm 
print("Response: \n", response.content)
