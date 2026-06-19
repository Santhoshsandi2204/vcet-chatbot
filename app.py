import os
import json
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai

# Import database and fallback engine
from database import VCET_DATA, match_fallback_response

# Load environment configurations
load_dotenv()

# Initialize Flask application
app = Flask(__name__)
# Enable CORS so the frontend (running on Live Server port 5500) can talk to the backend (port 5000)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Retrieve and configure Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")
is_ai_active = False

if API_KEY:
    try:
        genai.configure(api_key=API_KEY)
        logging.info("Google Generative AI successfully configured using GEMINI_API_KEY.")
        is_ai_active = True
    except Exception as e:
        logging.error(f"Error configuring Google GenAI: {e}. Defaulting to local parser.")

# System Context Prompt for Gemini
SYSTEM_INSTRUCTION = f"""
You are the official Virtual Assistant for Velammal College of Engineering & Technology (VCET), Madurai (Autonomous, NBA accredited, NAAC 'A' Grade).
Your job is to assist prospective students, parents, and current staff by answering queries about the college.

Strictly use the following VCET Institutional Database to formulate your answers:
{json.dumps(VCET_DATA, indent=2)}

Rules:
1. Provide concise, friendly, and professional responses.
2. Format your responses using clean Markdown (bold text, lists, headers).
3. If the user asks for contacts, list the relevant numbers.
4. If a query is unrelated to the college, gently redirect the user back to asking about VCET.
5. If the database does not contain the answer, tell the user to contact the general enquiry landline (0452-2465289) or email principal@vcet.ac.in.
"""

@app.route("/api/info", methods=["GET"])
def get_info():
    """Returns the full VCET data to populate frontend directory views."""
    return jsonify(VCET_DATA)

@app.route("/api/chat", methods=["POST"])
def chat():
    """Handles chat queries from the frontend."""
    data = request.json or {}
    user_message = data.get("message", "").strip()
    
    if not user_message:
        return jsonify({"error": "Empty message"}), 400
        
    logging.info(f"Received user query: '{user_message}'")
    
    # Check if Gemini API is configured and should be utilized
    if is_ai_active:
        try:
            # Setup model with the system instruction
            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                system_instruction=SYSTEM_INSTRUCTION
            )
            response = model.generate_content(user_message)
            ai_response = response.text.strip()
            
            logging.info("Generated reply using Gemini AI model.")
            return jsonify({
                "response": ai_response,
                "engine": "Gemini AI"
            })
        except Exception as e:
            logging.error(f"Gemini API call failed: {e}. Reverting to fallback local parser.")
            # Fallback to local rule engine if API call errors out
            fallback_response = match_fallback_response(user_message)
            return jsonify({
                "response": fallback_response,
                "engine": "Local Engine (Fallback)"
            })
    else:
        # Local keyword-matching fallback response
        fallback_response = match_fallback_response(user_message)
        logging.info("Generated reply using Local Engine (No Gemini API Key specified).")
        return jsonify({
            "response": fallback_response,
            "engine": "Local Engine"
        })

if __name__ == "__main__":
    # Run the server on port 5000
    app.run(host="127.0.0.1", port=5000, debug=True)
