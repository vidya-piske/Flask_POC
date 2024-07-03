from flask import Blueprint

multiplication_bp = Blueprint('maths_operation_multiplication', __name__)

@multiplication_bp.route('/multiply')
def multiply():
    a = 10
    b = 20
    result = a * b
    return f"Multiplication Result: {result}"


