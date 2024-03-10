from abc import ABC, abstractmethod
from .abstract_prompt import AbstractPrompt

class AbstractPrompter(ABC):

    @abstractmethod
    def prompt(self, prompt: AbstractPrompt):
        pass
