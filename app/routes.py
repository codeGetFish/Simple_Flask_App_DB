from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User

@app.route("/")
def hello():
    """Return a 'Hello World!' message."""
    return "Hello World!"

@app.route("/users")
def list_users():
    """Retrieve all users from the database and render them in the 'users.html' template."""
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route("/add-user", methods=["GET", "POST"])
def add_user():
    """Handle both GET and POST requests to add a user to the database."""
    if request.method == "POST":
        # Retrieve the user's input from the form
        username = request.form["username"]
        email = request.form["email"]

        # Create a new User object and add it to the database
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()

        # Redirect to the list of users
        return redirect(url_for("list_users"))

    # Return the 'add_user.html' template for a GET request
    return render_template("add_user.html")

@app.route("/delete-user/<int:user_id>", methods=["GET", "POST"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("list_users"))
    else:
        return "User not found", 404
    
@app.route("/edit-user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    user = User.query.get(user_id)
    if request.method == "POST":
        user.username = request.form["username"]
        user.email = request.form["email"]
        db.session.commit()
        return redirect(url_for("list_users"))
    return render_template("edit_user.html", user=user)