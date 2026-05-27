from app import db


class Planeacion(db.Model):
	__tablename__ = 'planeaciones'

	id = db.Column(db.Integer, primary_key=True)
	grupo_id = db.Column(db.Integer, db.ForeignKey('grupos.id'), nullable=False)
	materia_id = db.Column(db.Integer, db.ForeignKey('materias.id'), nullable=False)
	docente_id = db.Column(db.Integer, db.ForeignKey('docentes.id'), nullable=False)
	dia_semana = db.Column(db.Enum('Lunes','Martes','Miercoles','Jueves','Viernes','Sabado'), nullable=False)
	hora_inicio = db.Column(db.Time, nullable=False)
	hora_fin = db.Column(db.Time, nullable=False)
	aula = db.Column(db.String(50))
	periodo_escolar = db.Column(db.String(50))
	observaciones = db.Column(db.Text)

	def __repr__(self):
		return f"<Planeacion {self.id} grupo:{self.grupo_id} materia:{self.materia_id}>"
