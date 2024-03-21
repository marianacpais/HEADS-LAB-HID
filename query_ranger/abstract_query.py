from abc import ABC, abstractmethod

class AbstractQuery(ABC):
  DEFAULT_QUERY = ""
  DEFAULT_RESULTS = ""
  DEFAULT_SYS_MESSAGE = []

  def __init__(self, query=None, results=None, params=None):
    """
    """
    self.query_data = {
      'query': self.DEFAULT_QUERY if query is None else query,
      'results': self.DEFAULT_RESULTS if results is None else results
    }
    # TODO @mariana.pais add logic for when params are not dict
    self.params = {} if params is None else params
    self.sys_message = self.DEFAULT_SYS_MESSAGE

  def return_query(self):
    """
    """
    return self.query_data["query"]

  def return_results(self):
    """
    """
    return self.query_data["results"]

  @abstractmethod
  def get_results(self):
    """
    """
    pass
