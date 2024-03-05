import openai
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.ChatCompletion()


# Set your OpenAI API key here
openai.api_key = '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'

# # Call the ChatGPT API with GPT-4.0
# response = openai.ChatCompletion.create(
#     model="gpt-4",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."}
#     ],
# )

# Print the response
# print(response.choices[0].message['content'])


@app.route('/')
def hello_world():
    return 'Ask Any Question..............'


@app.route('/<question>')
def ask_ai(question):
    # index = GPTVectorStoreIndex.load_from_disk('index.json')
    try:
        chat_completion = client.create(
            messages=[
                {
                    "role": "user",
                    # "content": "replye should more accurate and professional (dont provide The company name can be similar to the URL http://, do not provide: for more information,  like reples ), give me company name company name can be similer to url contain name " + base_url + "what does it do give services or product names , size, from which country and small description about company as paragraph, all of products and services it provides weather it is primary business or secondary, and what functions they perform, explain all with small discription, no need to add 1, 2 like sub disciption, remove all urls and / " + reduced_paragraph,
                    "content": "reply should more accurate"+ question
                }
            ],
            model="gpt-4",
            # model = "Top-Edge-Advisor",
        )
    except:
        t = "Update or Check your gtp API key"

    try:
        result = chat_completion.choices[0].message['content']
        print(result)
        return jsonify({"response": result})
    
    
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred while processing the request."}), 500


if __name__ == '__main__':
    app.run()

