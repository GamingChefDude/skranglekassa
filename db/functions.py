from flask import Flask, request, jsonify, render_template, url_for
import mysql.connector, bcrypt
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
	checkEmail = get_user_by_email(email)
	if checkEmail != None:
		print("Email already in use.")
		return jsonify({"message": "Email already in use, Try again"}), 409 
	else:
		add_user(firstName, lastName, email, birthdate, password)
		return jsonify({"message": "User created successfully"}), 200


@app.route("/login", methods=["POST"])
def login():
	email = request.json.get("email", "")
	password = request.json.get("password", "")

	# check email in database
	checkEmail = get_user_by_email(email)

	# check if email exists
	if checkEmail == None:
		print("No user found with that email.")
		return jsonify({"message": "Login failed"}), 401
	else:
		getPassword = checkEmail[4]

		# check password matches with emails password
		if password != getPassword:
			print("Incorrect password.")
			return jsonify({"message": "Login failed"}), 401
		else:
			print("logged in!")
			return jsonify({"message": "Login successful"}), 200


def connect(): # remove later when only using postgresql
	db = mysql.connector.connect(
	host = "127.0.0.1",		#
	user = "root",			# Change credentials
	password = "root",		#
	database = "skranglekassa",
	port = 3306
	)

	c = db.cursor()
	return db, c


def encrypt(password):
	hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
	print("password hashed", hashed)
	return hashed


def retrieve():
	global loggedIn
	data = request.get_json(force=True)
	print("Retrieved")
	return data

@app.route("/contact")
def contactPage():
	global loggedIn
	print("Contact page")

	return render_template("contact.html")


@app.route("/login")
def loginPage():
	global loggedIn
	print("Login page")

	return render_template("login.html")


@app.route("/signup")
def signupPage():
	global loggedIn
	print("Signup page")

	return render_template("signup.html")


@app.route("/allproducts")
def allProductsPage():
	global loggedIn
	print("All products")

	return render_template("allproducts.html")


@app.route("/newproduct")
def newProductPage():
	global loggedIn
	print("New product page")

	return render_template("newproduct.html")


@app.route("/product")
def productPage():
	global loggedIn
	print("Product page")

	return render_template("product.html")


@app.route("/productimage")
def productImage():
	global loggedIn
	print("Image page")

	return render_template("productimage.html")

@app.route("/user")
def userPage():
	global loggedIn
	print("user page")
	if loggedIn == True:
		return render_template("user.html")
	else: 
		return jsonify({"message": "Login to view page"}), 401


@app.route("/logout")
def logoutPage():
	global loggedIn
	loggedIn = False

	return render_template("logout.html")

@app.route("/")
def home():
	global loggedIn
	print(app.url_map, loggedIn)
	if loggedIn == False:
		return render_template(
			"index.html", 
			contactPage_url=url_for("contactPage"),
			signupPage_url=url_for("signupPage"),
			loginPage_url=url_for("loginPage"),
			allProductsPage_url=url_for("allProductsPage"),
			newProductPage_url=url_for("newProductPage"),
			image_url=url_for("productImage"),
			productPage_url=url_for("productPage"),
			userPage_url=url_for("userPage"),
			logoutPage_url=url_for("logoutPage")
			)
	
	elif loggedIn == True:
		return render_template("home.html")
	else:
		print("How are you here?")
		return jsonify({"message": "How are you here?"}), 418 # I'm a teapot
