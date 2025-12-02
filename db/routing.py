from flask import jsonify, render_template, url_for
from db.functions import app, loggedIn

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
		return jsonify({"message": "How are you here?"}), 418 # I'm a teapot
