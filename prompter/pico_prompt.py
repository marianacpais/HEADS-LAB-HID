from .abstract_prompt import AbstractPrompt

class PICOPrompt(AbstractPrompt):

    def __init__(self, population, intervention, comparator, outcome, comment):
        self.population = population
        self.intervention = intervention
        self.comparator = comparator
        self.outcome = outcome
        self.comment = comment

    def get_content(self):
        return {
            "P": self.population,
            "I": self.intervention,
            "C": self.comparator,
            "O": self.outcome,
            "comment": self.comment
        }
