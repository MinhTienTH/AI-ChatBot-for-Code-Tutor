import os
import traceback
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class CodeAssistantModel:
    def __init__(self):
        # Predefined system prompts for different contexts
        self.context_prompts = {
            'code_explanation': "You are an expert code explanation assistant. Provide detailed, clear explanations of programming concepts and code snippets.",
            'language_basics': "You are an expert programming language instructor. Provide comprehensive overviews of programming language fundamentals.",
            'implementation_guide': "You are a technical implementation guide specialist. Offer step-by-step, practical guidance for programming tasks.",
            'general': "You are a helpful AI assistant specializing in programming and software development."
        }
        # Chat history to maintain context
        self.chat_history = []

    def generate_response(self, input_user, context='general'):
        try:
            # Prepare system prompt
            system_prompt = self.context_prompts.get(context, self.context_prompts['general'])
            
            # Maintain chat history
            self.chat_history.append({"role": "user", "content": input_user})
            
            # Include system prompt only in the first message
            if len(self.chat_history) == 1:
                self.chat_history.insert(0, {"role": "system", "content": system_prompt})

            client = OpenAI(
                base_url="http://localhost:11434/v1",
            )

            # Generate response with correct message format
            response = client.chat.completions.create(
                model="llama3.2:1b",  # or your specific model
                messages=self.chat_history
            )
            
            # Add the assistant's response to the chat history
            assistant_message = response.choices[0].message.content.split(".")[0]+"."
            self.chat_history.append({"role": "assistant", "content": assistant_message})
            
            return assistant_message
        
        except Exception as e:
            logger.error(f"Model error: {str(e)}")
            logger.error(traceback.format_exc())
            return f"Model generation error: {str(e)}"


# Flask Application Setup
app = Flask(__name__)
CORS(app)

# Error handler
@app.errorhandler(500)
def handle_500(error):
    logger.error(f"500 error occurred: {str(error)}")
    return jsonify({'error': 'Internal Server Error', 'details': str(error)}), 500

# Initialize model
code_assistant = CodeAssistantModel()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data received'}), 400
            
        message = data.get('message', '')
        context = data.get('context', 'general')
        
        # Get the user agent with flush=True
        user_agent = request.headers.get('User-Agent', 'Unknown')
        print(f"Request from User-Agent: {user_agent}", flush=True)  # Added flush=True
        
        response = code_assistant.generate_response(message, context)
        return jsonify({
            'response': response,
            'user_agent': user_agent
        })
    
    except Exception as e:
        print(f"Error in chat route: {str(e)}", flush=True)  # Added flush=True
        return jsonify({
            'error': 'Internal server error',
            'details': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)