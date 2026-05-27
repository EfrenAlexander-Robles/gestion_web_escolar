from app import db


class Turno(db.Model):
    __tablename__ = 'turnos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    descripcion = db.Column(db.String(255))
    hora_inicio = db.Column(db.Time)
    hora_fin = db.Column(db.Time)
    activo = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<Turno {self.nombre}>"
