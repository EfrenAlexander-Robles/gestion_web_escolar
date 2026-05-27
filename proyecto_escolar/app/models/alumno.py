from app import db


class Alumno(db.Model):
	__tablename__ = 'alumnos'

	id = db.Column(db.Integer, primary_key=True)
	matricula = db.Column(db.String(50), unique=True, nullable=False)
	nombre = db.Column(db.String(100), nullable=False)
	apellido = db.Column(db.String(100), nullable=False)
	grupo_id = db.Column(db.Integer, db.ForeignKey('grupos.id'), nullable=True)
	activo = db.Column(db.Boolean, default=True)
	creado_en = db.Column(db.DateTime, server_default=db.func.now())
	actualizado_en = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

	grupo = db.relationship('Grupo', backref='alumnos')

	def __repr__(self):
		return f"<Alumno {self.matricula} {self.nombre} {self.apellido}>"
