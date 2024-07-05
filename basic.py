from flask import Flask, Blueprint, jsonify, request

# Import your mathematical operation blueprints
from addition import addition_bp
from multiplication import multiplication_bp
from substraction import subtraction_bp

# Create an instance of the Flask class
app = Flask(__name__)

# Register blueprints for mathematical operations with unique prefixes
app.register_blueprint(addition_bp, url_prefix="/maths/addition")
app.register_blueprint(multiplication_bp, url_prefix="/maths/multiplication")
app.register_blueprint(subtraction_bp, url_prefix="/maths/subtraction")

# Define a Blueprint for API endpoints
api_bp = Blueprint('api_bp', __name__, url_prefix="/api")

# Example data (can be replaced with a database or other data source)
posts = []

# Define API routes within the API Blueprint
@api_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()

    # Example: Assuming JSON data contains 'name' and 'surname'
    name = data.get('name')
    surname = data.get('surname')

    # Validation (you can add more complex validation as needed)
    if not name or not surname:
        return jsonify({'error': 'Please provide both name and surname'}), 400

    # Create a new post
    new_post = {
        'id': len(posts) + 1,
        'name': name,
        'surname': surname
    }

    posts.append(new_post)

    return jsonify(new_post), 201

# Register the API blueprint with the application
app.register_blueprint(api_bp, url_prefix="/api")

# Define route for the homepage
@app.route('/')
def home():
    return 'Welcome! Use /maths/addition, /maths/multiplication, /maths/subtraction ' \
           'to perform operations. Use /api/posts for API endpoint.'

# Only run the Flask application if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)
