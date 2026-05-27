from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Configuracion')
    
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('mysql'):
        app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
            'connect_args': {
                'ssl': {
                    'ssl_mode': 'REQUIRED'
                }
            }
        }

    db.init_app(app)
    
    with app.app_context():
        # Import all models so SQLAlchemy create_all() sees every table metadata
        from app.models.alumno import Alumno
        from app.models.grupo import Grupo
        from app.models.materia import Materia
        from app.models.planeacion import Planeacion
        from app.models.calificacion import Calificacion
        from app.models.turno import Turno
        from app.models.docente import Docente
        from app.models.usuario import Usuario

        from app.routes.test import bp as test_bp
        from app.routes.usuarios import bp as usuarios_bp
        from app.routes.calificaciones import bp as calificaciones_bp
        app.register_blueprint(test_bp)
        app.register_blueprint(usuarios_bp)
        app.register_blueprint(calificaciones_bp)
        db.create_all()
    
    return app