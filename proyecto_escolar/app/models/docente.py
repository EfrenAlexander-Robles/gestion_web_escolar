from app import db


class Docente(db.Model):
    __tablename__ = 'docentes'

    id = db.Column(db.Integer, primary_key=True)
    numero_empleado = db.Column(db.String(30), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True)
    telefono = db.Column(db.String(20))
    especialidad = db.Column(db.String(150))
    activo = db.Column(db.Boolean, default=True)
    fecha_contratacion = db.Column(db.Date)

    def __repr__(self):
        return f"<Docente {self.numero_empleado} {self.nombre} {self.apellido}>"
