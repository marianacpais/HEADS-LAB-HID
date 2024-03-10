from .abstract_prompter import AbstractPrompter
from .abstract_prompt import AbstractPrompt
from openai import OpenAI

class PICOPrompter(AbstractPrompter):

    def __init__(self, model="gpt-4", openai_api_key="your-api-key"):
        self.client = OpenAI(api_key=openai_api_key)
        self.model = model

    def prompt(self, prompt: AbstractPrompt):
        if not isinstance(prompt, AbstractPrompt):
            raise ValueError("The prompt must be an instance of AbstractPrompt class")

        content = prompt.get_content()

        system_prompt = {
            "role": "system",
            "content": ("You are a very prestigious researcher in the healthcare field "
                        "that is very keen on research methodology. I will provide you "
                        "with research questions and you will interpret them using the "
                        "PICO framework, as follows:\n"
                        "P - Population of the study\n"
                        "I - Intervention (may not apply)\n"
                        "C - Comparator\n"
                        "O - Outcome\n\n"
                        "Also, please provide a comment on how well defined the research "
                        "question is. You will call this \"comment\".\n\n"
                        "I want you to output this only in json, and only provide in your "
                        "answer as a json-valid object similar to the one that follows:\n\n"
                        "{\n"
                        "  \"P\": \"Value for P\",\n"
                        "  \"I\": \"Value for I\",\n"
                        "  \"C\": \"Value for C\",\n"
                        "  \"O\": \"Value for O\",\n"
                        "  \"comment\": \"Comment on how well defined the research question is\"\n"
                        "}")
        }
        user_prompt = {
            "role": "user",
            "content": content
        }
        response = self.client.create_completion(
            model=self.model,
            prompt=[system_prompt, user_prompt],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response
