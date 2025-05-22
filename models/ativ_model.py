from database import db

class Atividades(db.Model):
    __tablename__ = 'atividades'

    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    data_entrega = db.Column(db.String(20), nullable=False)
    titulo = db.Column(db.String(10), nullable=False)
    descricao = db.Column(db.String(10), nullable=False)
    
