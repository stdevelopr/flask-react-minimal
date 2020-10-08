from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db


class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key=True)
    primeiro_nome = db.Column(db.String(255))
    ultimo_nome = db.Column(db.String(255))
    email = db.Column(db.String(255))