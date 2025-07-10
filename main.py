"""
Summary: 
A simple chatbot that would act as a helpful assistant... 
Assistant has access to search, math etc... one can add more
tools in tools file to add more tooling to chabot.

"""
from model_loader import llm
from tools import chatbot_tools, selected_tool
from langchain_core.messages import HumanMessage, SystemMessage

messages = []
messages.append(SystemMessage("You are helpful chatbot"))

llm_with_tools = llm.bind_tools(chatbot_tools)

user_query = input("Please ask me anything?")
messages.append(HumanMessage(user_query))
response = llm_with_tools.invoke(messages)

for tool_call in response.tool_calls:
  tool = selected_tool[tool_call["name"].lower()] # finding the tool messages
  print("tool", tool)
  tool_msg = tool.invoke(tool_call) # invoking the tool messages
  messages.append(tool_msg)  

response = llm.invoke(messages) # invoking llm 
print("final output", response.content)
