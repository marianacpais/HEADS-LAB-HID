import pytest
from unittest.mock import Mock, patch
from prompter.pico_prompter import PICOPrompter
from prompter.pico_prompt import PICOPrompt

mock_response = {
  "choices": [{
    "message": {
      "content": {
        "P": "patients with chronic diseases",
        "I": "integration of digital health monitoring devices",
        "C": "standard patient care",
        "O": "management of chronic diseases and improvement of patient outcomes",
        "comment": "The research question is well-defined and directly relates to the impact of digital health integration."
      }
    }
  }]
}

@patch('prompter.pico_prompter.OpenAI')
def test_picoprompter(mock_openai):
  mock_client_instance = mock_openai.return_value
  mock_client_instance.chat.completions.create.return_value = mock_response

  pico_prompt = PICOPrompt("How does the integration of digital health monitoring devices into routine patient care influence the management of chronic diseases and improve patient outcomes?")

  pico_prompter = PICOPrompter()

  response = pico_prompter.prompt(pico_prompt)

  assert mock_client_instance.chat.completions.create.called
  assert response == mock_response
