from flask import Flask, render_template, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

# Initialize Groq client
client = Groq(api_key="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")

def generate_response(prompt):
    try:
        stream = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "you are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_completion_tokens=1024,
            top_p=1,
            stream=True,
        )
        
        # Collect all chunks into a single response
        full_response = ""
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
        
        return full_response
    except Exception as e:
        print(f"Error generating response: {str(e)}")
        return "Sorry, I encountered an error while processing your request."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Generate response using Groq
        response = generate_response(user_message)
        
        return jsonify({'response': response})
    
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)