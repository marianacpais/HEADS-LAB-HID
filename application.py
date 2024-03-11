import os
from flask import Flask, request, render_template, jsonify
import logging

from prompter.pico_prompter import PICOPrompter
from prompter.pico_prompt import PICOPrompt


application = Flask(__name__)
application.logger.setLevel(logging.DEBUG)

# For debugging
message_content_example = '{"choices": [{"message": {"content": {"P": "patients with chronic diseases","I": "integration of digital health monitoring devices","C": "standard patient care","O": "management of chronic diseases and improvement of patient outcomes","comment": "The research question is well-defined and directly relates to the impact of digital health integration."}}}]}'

@application.route('/', methods=['GET', 'POST'])
def index():
  pico_prompt = PICOPrompt(research_question="")

  if request.method == 'POST':
    openai_api_key = os.getenv('OAI_TOKEN')
    if not openai_api_key:
      raise EnvironmentError("OAI_TOKEN environment variable not set.")

    pico_prompter = PICOPrompter(openai_api_key=openai_api_key)
    user_input = request.form['query']
    pico_prompt = PICOPrompt(research_question=user_input)
    chat_completion = pico_prompter.prompt(pico_prompt)
    message_content = str(chat_completion.choices[0].message.content if chat_completion.choices else "No content")
    pico_prompt.parse_response(response=message_content)

  return render_template('form.html', response=pico_prompt.get_content())

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000, debug=True)
