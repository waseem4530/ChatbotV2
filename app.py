from flask import Flask, render_template, request, jsonify
import re

def generate_responses(user_query):
    from groq import Groq
    client = Groq(api_key="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")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a helpful assistant."
            },
            {
                "role": "user",
                "content": user_query,
            }
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.5,
        max_completion_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
    )
    return chat_completion.choices[0].message.content

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message']
    ai_response = generate_responses(user_message)
    
    # Format the response as bullet points if it contains multiple paragraphs
    formatted_response = ai_response
    if len(ai_response.split('\n\n')) > 1 or '- ' in ai_response:
        # Try to detect if there are already bullet points
        if not '- ' in ai_response and not '* ' in ai_response:
            paragraphs = ai_response.split('\n\n')
            formatted_response = '- ' + '\n- '.join(paragraphs)
    
    return jsonify({
        'response': formatted_response
    })

if __name__ == '__main__':
    app.run(debug=True)