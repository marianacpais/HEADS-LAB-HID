import json

from .abstract_prompt import AbstractPrompt

class PICOPrompt(AbstractPrompt):

  def __init__(self, research_question, population=None, intervention=None, comparator=None, outcome=None, comment=None):
    self.research_question = research_question
    self.population = population
    self.intervention = intervention
    self.comparator = comparator
    self.outcome = outcome
    self.comment = comment

  def parse_response(self, response):
    try:
      parsed_response = json.loads(response)
      self.population = parsed_response["P"]
      self.intervention = parsed_response["I"]
      self.comparator = parsed_response["C"]
      self.outcome = parsed_response["O"]
      self.comment = parsed_response["comment"]
    except:
      self.comment = f"Invalid response structure. Response: {response}"

  def get_content(self):
    return {
      "research_question": self.research_question,
      "P": self.population,
      "I": self.intervention,
      "C": self.comparator,
      "O": self.outcome,
      "comment": self.comment
    }
