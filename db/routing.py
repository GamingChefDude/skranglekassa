from flask import jsonify, render_template, url_for
import db.appCore as core
from db.appCore import app


@app.route("/contact")
def contactPage():
	print("Contact page")

	return render_template("contact.html")


@app.route("/login")
def loginPage():
	print("Login page")

	return render_template("login.html")


@app.route("/signup")
def signupPage():
	print("Signup page")

	return render_template("signup.html")


@app.route("/allproducts")
def allProductsPage():
	print("All products")

	return render_template("allproducts.html")


@app.route("/newproduct")
def newProductPage():
	print("New product page")

	return render_template("newproduct.html")


@app.route("/product")
def productPage():
	print("Product page")

	return render_template("product.html")


@app.route("/productimage")
def productImage():
	print("Image page")

	return render_template("productimage.html")

@app.route("/user")
def userPage():
	print("user page")
	if loggedIn == True:
		return render_template("user.html")
	else: 
		return jsonify({"message": "Login to view page"}), 401


@app.route("/logout")
def logoutPage():
	core.loggedIn = False

	return render_template("logout.html")

@app.route("/")
def home():
	print(f"User logged in: {core.loggedIn}, routing.py")
	if core.loggedIn == False:
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
	
	elif core.loggedIn == True:
		return render_template("home.html")
	else:
		return jsonify({"message": "How are you here?"}), 418 # I'm a teapot
