from flask import Blueprint, request  
from controllers.carro_controllers import get_carros, create_carro

carro_routes = Blueprint('carro_routes', __name__)  

@carro_routes.route('/Carro', methods=['POST'])
def carros_post():
    carro_data = request.json
    return create_carro(request.json)
@carro_routes.route('/Carro', methods=['GET'])
def carros_get():
    return get_carros()