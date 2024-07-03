from flask import Blueprint

addition_bp = Blueprint('maths_operation_addition', __name__)

@addition_bp.route('/add')
def add():
    a = 10
    b = 20
    result = a + b
    return f"Addition Result: {result}"
