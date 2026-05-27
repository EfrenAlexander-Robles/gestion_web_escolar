from app import db


class Calificacion(db.Model):
    __tablename__ = 'calificaciones'

    id = db.Column(db.Integer, primary_key=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'), nullable=False)
    planeacion_id = db.Column(db.Integer, db.ForeignKey('planeaciones.id'), nullable=True)
    docente_id = db.Column(db.Integer, db.ForeignKey('docentes.id'), nullable=True)
    valor = db.Column(db.Numeric(5,2), nullable=False)
    tipo = db.Column(db.Enum('Parcial','Final','Tarea','Participacion'), default='Parcial')
    fecha = db.Column(db.Date)
    comentarios = db.Column(db.Text)
    creado_en = db.Column(db.DateTime, server_default=db.func.now())
    actualizado_en = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    alumno = db.relationship('Alumno', backref='calificaciones')
    planeacion = db.relationship('Planeacion', backref='calificaciones')

    def __repr__(self):
        return f"<Calificacion {self.id} alumno:{self.alumno_id} valor:{self.valor}>"
