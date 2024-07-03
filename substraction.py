from flask import Blueprint

subtraction_bp = Blueprint('maths_operation_subtraction', __name__)

@subtraction_bp.route('/substract')
def substract():
    a = 10
    b = 20
    result = b - a  # Perform subtraction directly here
    return f'Subtraction Result: {result}'

#When you define a route in Flask using a blueprint, Flask's routing system automatically calls the associated function This defines a route /substract within the maths_operation_subtraction blueprint.
#The substract function will be called when the /substract URL is accessed.