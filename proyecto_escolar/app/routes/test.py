from flask import Blueprint, render_template, jsonify
from app import db
from app.models.usuario import Usuario

bp = Blueprint('test', __name__, url_prefix='/test')

@bp.route('/')
def test():
    """Ruta de prueba para verificar la conexión a la base de datos"""
    try:
        usuarios = Usuario.query.all()
        total = len(usuarios)
        primer_usuario = usuarios[0] if usuarios else None
        nombres = [u.nombre for u in usuarios]
        
        return jsonify({
            'status': 'success',
            'message': 'Conexión a base de datos exitosa',
            'total_usuarios': total,
            'primer_usuario': primer_usuario.to_dict() if primer_usuario else None,
            'todos_los_nombres': nombres
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
