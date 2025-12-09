from flask import jsonify, request
import bcrypt
import db.dataBase as dataBase
import db.appCore as core
from db.appCore import app


@app.route("/signup", methods=["POST"])
def signup():
	#get user info from request
	firstName = request.json.get("fname", "")
	lastName = request.json.get("lname", "")
	email = request.json.get("email", "")
	birthdate = request.json.get("birthdate", "")
	password = request.json.get("password", "")

	#check if email already exists
	if dataBase.get_user_by_email(email) is not None:
		return jsonify({"message": "Email er i bruk. Prøv igjen"}), 409 
	
	hashedPassword = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

	dataBase.add_user(firstName, lastName, email, birthdate, hashedPassword)
	
	return jsonify({"message": "Bruker lagt til"}), 200


@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", "")
    password = request.json.get("password", "")

	# check email in database
    user = dataBase.get_user_by_email(email)
	# check if email exists
    if user is None:
        return jsonify({"message": "Bruker navn eller passord er feil. Prøv igjen"}), 401

    storedhash = user[4]

	# handle DB returning memoryview or str
    if isinstance(storedhash, memoryview):
        storedhash = storedhash.tobytes()
    if isinstance(storedhash, str):
        storedhash = storedhash.encode("utf-8")

    if not bcrypt.checkpw(password.encode("utf-8"), storedhash):
        return jsonify({"message": "Bruker navn eller passord er feil. Prøv igjen"}), 401

    core.loggedIn = True
    print(f"User logged in: {core.loggedIn}, functions.py")
    return jsonify({"message": "Velkommen"}), 200


@app.route("/newproduct", methods=["POST"])
def newproduct():
	name = request.json.get("name", "")
	price = request.json.get("price", "")
	description = request.json.get("description", "")
	specs = request.json.get("specs", "")

	if core.loggedIn == False: # make sure only logged in users can add products
		return jsonify({"message": "Logg in for å legge til product"}), 401
      
	dataBase.add_product(name, price, description, specs)
	print("Adding new product")
	return jsonify({"message": "Product lagt til"}), 200
