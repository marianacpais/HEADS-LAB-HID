from abc import ABC, abstractmethod

class AbstractPrompt(ABC):

  @abstractmethod
  def get_content(self):
    pass
