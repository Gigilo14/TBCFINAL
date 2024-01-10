from flask import render_template, redirect
from flask_login import login_user, logout_user, login_required
from forms import AddProductForm, RegistrationForm, EditProductForm, LoginForm
from os import path
from models import Product, User
from ext import app, db


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/second")
def about():
    return render_template("second.html")

@app.route("/register", methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        new_user.create()
    return render_template("register.html", form=form)

@app.route("/avtor", methods=['GET', 'POST'])
def authorization():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)

    return render_template("avtor.html", form=form)

@app.route("/edit_product/<int:product_id>", methods=["POST", "GET"])
@login_required
def edit_product(product_id):
    chosen_product = Product.query.get(product_id)
    if not chosen_product:
        return render_template("three.html")

    form = AddProductForm(name=chosen_product.name, color=chosen_product.color, length=chosen_product.length,  price=chosen_product.price)
    form = EditProductForm(name=chosen_product.name, color=chosen_product.color, length=chosen_product.length,  price=chosen_product.price)
    if form.validate_on_submit():
        chosen_product.name = form.name.data
        chosen_product.color = form.color.data
        chosen_product.length = form.length.data
        chosen_product.price = form.price.data

        if form.img.data != None:
            chosen_product.img = form.img.data.filename
            file_directory = path.join(app.root_path, "static", form.img.data.filename)
            form.img.data.save(file_directory)


        db.session.commit()

    return render_template("product.html", form=form)

@app.route("/delete_product/<int:product_id>")
@login_required
def delete_product(product_id):
    chosen_product = Product.query.get(product_id)
    if not chosen_product:
        return render_template("three.html")

    db.session.delete(chosen_product)
    db.session.commit()
    return redirect("/three")

@app.route("/add_product", methods=["POST", "GET"])
@login_required
def add_product():
    form = AddProductForm()
    print(app.root_path + "/static")
    if form.validate_on_submit():
        new_product = Product(name=form.name.data, color=form.color.data, length=form.length.data, img=form.img.data.filename, price=form.price.data)
        db.session.add(new_product)  #ჩვენ თუ გვინდა რომ ჩვენი ბაზა გაეშვას მარტო დაწერა არ არი საკმარისი უნდა დავასეივოთ
        db.session.commit()

        file_directory = path.join(app.root_path, "static", form.img.data.filename)
        form.img.data.save(file_directory)
        return redirect("/three")


    return render_template("product.html", form=form)


@app.route("/three")
def images():
    products = Product.query.all()
    return render_template("three.html", products=products)

@app.route("/four")
def magazine():
    return render_template("four.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")