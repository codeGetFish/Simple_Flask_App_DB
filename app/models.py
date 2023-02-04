# Import the database from the main app
from app import db

# Create the User model for the database
class User(db.Model):
    # The primary key for the User model
    id = db.Column(db.Integer, primary_key=True)

    # The username for the User, must be unique and not null
    username = db.Column(db.String(80), unique=True, nullable=False)

    # The email for the User, must be unique and not null
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Representation of the User model
    def __repr__(self):
        return '<User %r>' % self.username
