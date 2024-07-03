from flask import Flask
from addition import addition_bp
from multiplication import multiplication_bp
#'substraction' is a filename and 'subtraction_bp' is a blueprint
from substraction import subtraction_bp

# Create an instance of the Flask class
app = Flask(__name__)

# Register blueprints
app.register_blueprint(addition_bp, url_prefix="/maths")
app.register_blueprint(multiplication_bp, url_prefix="/maths")
app.register_blueprint(subtraction_bp, url_prefix="/maths")

# Define route for the homepage
@app.route('/')
def home():
    return 'Welcome! Use /maths/add, /maths/multiply, /maths/subtract to perform operations.'

print(f"basic.py: __name__ is {__name__}")

# Only run the Flask application if this file is executed directly
if __name__ == "__main__":
    print("Running basic.py directly")
    app.run(debug=True)
else:
    print("Importing basic.py as a module")
