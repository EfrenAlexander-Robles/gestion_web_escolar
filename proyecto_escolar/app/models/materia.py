from app import db


class Materia(db.Model):
	__tablename__ = 'materias'

	id = db.Column(db.Integer, primary_key=True)
	clave = db.Column(db.String(20), unique=True, nullable=False)
	nombre = db.Column(db.String(150), nullable=False)
	descripcion = db.Column(db.Text)
	creditos = db.Column(db.Integer, default=0)
	horas_semana = db.Column(db.Integer, default=0)
	activo = db.Column(db.Boolean, default=True)

	def __repr__(self):
		return f"<Materia {self.clave} - {self.nombre}>"
