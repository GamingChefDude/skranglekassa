from flask import Flask, request, jsonify
import bcrypt
from db.dataBase import *



app = Flask(
    __name__,
    template_folder='../SRC/HTML/',
    static_folder='../SRC/'
)


loggedIn = False

@app.route("/signup", methods=["POST"])
def signup():
	#get user info from request
	firstName = request.json.get("fname", "")
	lastName = request.json.get("lname", "")
	email = request.json.get("email", "")
	birthdate = request.json.get("birthdate", "")
	password = request.json.get("password", "")

	#check if email already exists
	if get_user_by_email(email) is not None:
		return jsonify({"message": "Email already in use, Try again"}), 409 
	
	hashedPassword = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

	add_user(firstName, lastName, email, birthdate, hashedPassword)
	
	return jsonify({"message": "User created successfully"}), 200


@app.route("/login", methods=["POST"])
def login():
	global loggedIn
	email = request.json.get("email", "")
	password = request.json.get("password", "")

	# check email in database
	user = get_user_by_email(email)

	# check if email exists
	if user is None:
		return jsonify({"message": "Login failed"}), 401

	storedhash = user[4]
	
	# handle DB returning memoryview or str
	if isinstance(storedhash, memoryview):
		storedhash = storedhash.tobytes()

	if isinstance(storedhash, str):
		storedhash = storedhash.encode("utf-8")

	if not bcrypt.checkpw(password.encode("utf-8"), storedhash):
		return jsonify({"message": "Login failed"}), 401

	loggedIn = True
	return jsonify({"message": "Login successful"}), 200
