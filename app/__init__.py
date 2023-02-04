# Import the necessary packages from Flask
from flask import Flask, render_template, request

# Import SQLAlchemy for database integration
from flask_sqlalchemy import SQLAlchemy

# Create the Flask app
app = Flask(__name__)

# Enable debugging for the app (optional)
app.debug = True

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# Initialize the database with the app
db = SQLAlchemy(app)

# Import the routes for the app
from . import routes
