from db import db

class Carro(db.Model):
    __tablename__ = 'carros'

    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(80), nullable=False)
    marca = db.Column(db.String(80), nullable=False)
    ano = db.Column(db.Integer, nullable=False)

    def json(self):
        return {
            'id': self.id,           
            'modelo': self.modelo,    
            'marca': self.marca,      
            'ano': self.ano           
        }
