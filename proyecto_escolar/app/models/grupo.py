from app import db

class Grupo(db.Model):
	__tablename__ = 'grupos'

	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(50), nullable=False)
	semestre = db.Column(db.Integer)
	aula = db.Column(db.String(50))
	turno_id = db.Column(db.Integer, db.ForeignKey('turnos.id'))
	activo = db.Column(db.Boolean, default=True)

	def __repr__(self):
		return f"<Grupo {self.nombre} (sem {self.semestre})>"
