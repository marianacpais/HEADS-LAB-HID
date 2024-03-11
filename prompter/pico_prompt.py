from .abstract_prompt import AbstractPrompt

class PICOPrompt(AbstractPrompt):

  def __init__(self, research_question, population=None, intervention=None, comparator=None, outcome=None, comment=None):
    self.research_question = research_question
    self.population = population
    self.intervention = intervention
    self.comparator = comparator
    self.outcome = outcome
    self.comment = comment

  def get_content(self):
    return {
      "research_question": self.research_question,
      "P": self.population,
      "I": self.intervention,
      "C": self.comparator,
      "O": self.outcome,
      "comment": self.comment
    }
