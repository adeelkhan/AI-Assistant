from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool

# searching via duckduckgo
duck_search = DuckDuckGoSearchRun()

@tool
def add(a: int, b: int) -> int: 
  """Add two integers

  Args: 
    a: First integer 
    b: Second integer
  """
  return a + b

@tool
def multiply(a: int, b: int) -> int: 
  """Multiply two integers, 
  Args:
    a: First integer 
    b: Second integer
  """
  return a * b


selected_tool = {"add": add, "multiply": multiply, "duckduckgo_search": duck_search}
chatbot_tools = [add, multiply, duck_search]





