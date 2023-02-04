# Import the Flask app object from the app module
from app import app, db
from app.models import User
# Check if the script is being run as the main module
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # Run the app with the debug mode set to True
    # This allows for easier debugging in case of any errors
    app.run(debug=True)