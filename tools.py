from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
from langchain_community.tools.google_books import GoogleBooksQueryRun
from langchain_community.utilities.google_books import GoogleBooksAPIWrapper 


# searching via duckduckgo
duck_search = DuckDuckGoSearchRun()

# google books to search for book and its review
book_api_tool = GoogleBooksQueryRun(api_wrapper=GoogleBooksAPIWrapper())


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


selected_tool = {"add": add, "multiply": multiply, "duckduckgo_search": duck_search, "googlebooks": book_api_tool}
chatbot_tools = [add, multiply, duck_search, book_api_tool]





