from flask import Blueprint

# Creating a Blueprint named 'maths_operation_addition'
addition_bp = Blueprint('maths_operation_addition', __name__)
#maths_operation_addition helps you and others understand what functionality or operation this Blueprint represents. This naming convention improves clarity and organization within your Flask application
#__name__ does refers to the current module

@addition_bp.route('/add')
def add():
    a = 10
    b = 20
    result = a + b
    return f"Addition Result: {result}"
