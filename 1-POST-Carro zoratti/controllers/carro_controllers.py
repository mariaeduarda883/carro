from models.carro_models import Carro
from db import db
import json
from flask import make_response

def get_carros(): 
    carros =Carro.query.all() 
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de Carros.',
            'dados':[carro.json() for carro in carros ]
        },ensure_ascii=False, sort_keys=False)

    )
    response.headers['Content-Type'] = 'application/json' 
    return response
def create_carro(carro_data):
    if not all(key in  carro_data for key in ['modelo','marca', 'ano']):
        response = make_response(
            json.dumps({'mensagem': 'Dados invalidos. Modelo, marca e ano são obrigatorios,'}, ensure_ascii=False),
            400 
        )
        response.headers['Content-Type']= 'application/json'
        return response
    novo_carro = Carro(
        modelo=carro_data['modelo'],  
        marca=carro_data['marca'],    
        ano=carro_data['ano']         
    )
    db.session.add(novo_carro)
    db.session.commit()
    response = make_response(
        json.dumps({  
            'mensagem': 'Carro cadastrado com sucesso.',  
            'carro': novo_carro.json()  
        }, sort_keys=False)  
    )
    response.headers['content-Type'] = 'application/json'
    return response
