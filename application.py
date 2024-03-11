import os
from flask import Flask, request, render_template, jsonify
import logging

from prompter.pico_prompter import PICOPrompter
from prompter.pico_prompt import PICOPrompt


application = Flask(__name__)
application.logger.setLevel(logging.DEBUG)

logging.basicConfig(level=logging.DEBUG)

@application.route('/', methods=['GET', 'POST'])
def index():
  response = None
  if request.method == 'POST':
    openai_api_key = os.getenv('OAI_TOKEN')
    if not openai_api_key:
      raise EnvironmentError("OAI_TOKEN environment variable not set.")

    pico_prompter = PICOPrompter(openai_api_key=openai_api_key)
    user_input = request.form['query']
    pico_prompt = PICOPrompt(research_question=user_input)


    chat_completion = pico_prompter.prompt(pico_prompt)
    message_content = chat_completion.choices[0].message.content if chat_completion.choices else "No content"
    return jsonify({"message": message_content})

  return render_template('form.html', response=response)

@application.route('/index2')
def index2():
    return render_template('form.html')

@application.route('/prompt', methods=['POST'])
def prompt():
    openai_api_key = os.getenv('OAI_TOKEN')

    if not openai_api_key:
        raise EnvironmentError("OAI_TOKEN environment variable not set.")

    pico_prompter = PICOPrompter(openai_api_key=openai_api_key)
    user_input = request.form['query']
    pico_prompt = PICOPrompt(research_question=user_input)
    response = pico_prompter.prompt(pico_prompt)
    return jsonify(response)

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000, debug=True)
