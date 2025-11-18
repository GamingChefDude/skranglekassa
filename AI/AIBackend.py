from flask import request, jsonify
from flask_cors import CORS
from db.functions import app
from db.dataBase import *

CORS(app)

try:
	import AI.AILogic as AI
	print("Is ai yes")
	noai = False
except:
	print("Ai not working")
	noai = True

database = fetch_all_products()  # Fetch products from the database

@app.route("/chat", methods=["POST"])
def chat():

	# check if ai is available
	if not noai:
		data = request.json
		userInput = data.get("userInput", "") # Get user input from request

		# Validate user input
		if not userInput:
			return jsonify({"error": "No input provided"}), 400 
		AIOutput = AI.get_ai_response(userInput, database) # Get AI response using the function from ai_logic.py
		return jsonify({"aiOutput": AIOutput})# Return AI response as JSON
	else:
		return jsonify({"aiOutput": "Beklager! Ai fungerer foreløpig ikke grunnet serverfeil."}), 503 # Service Unavailable error