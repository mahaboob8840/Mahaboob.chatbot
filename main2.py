import os
from flask import Flask, request, render_template, jsonify
from google import genai

# Best practice: Replace with your actual key or use environment variables
API_KEY = "AIzaSyCH1-WVHOuQJHCd6r_WQXFrFTxbpUgfGPw"
client = genai.Client(api_key=API_KEY)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_msg = data.get("msg")
        
        if not user_msg:
            return "No message received", 400

        # Note: Using gemini-2.0-flash (stable)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_msg
        )
        
        return response.text
    
    except Exception as e:
        print(f"Error: {e}")
        return "System error. Please try again later.", 500

if __name__ == "__main__":
    # Port 5001 is safer for macOS/Linux users
    app.run(port=5001, debug=True)
