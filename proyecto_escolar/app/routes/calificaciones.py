from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.calificacion import Calificacion
from app.models.alumno import Alumno
from app.models.planeacion import Planeacion

bp = Blueprint('calificaciones', __name__, url_prefix='/calificaciones')


@bp.route('/')
def index():
    try:
        califs = Calificacion.query.order_by(Calificacion.fecha.desc()).all()
    except Exception:
        califs = []

    return render_template('calificaciones/index.html', calificaciones=califs)


@bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        alumno_id = request.form.get('alumno_id')
        planeacion_id = request.form.get('planeacion_id') or None
        valor = request.form.get('valor')
        tipo = request.form.get('tipo')
        fecha = request.form.get('fecha') or None
        comentarios = request.form.get('comentarios')

        try:
            cal = Calificacion(
                alumno_id=alumno_id,
                planeacion_id=planeacion_id,
                valor=valor,
                tipo=tipo,
                fecha=fecha,
                comentarios=comentarios
            )
            db.session.add(cal)
            db.session.commit()
            flash('Calificación creada.', 'success')
            return redirect(url_for('calificaciones.index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al crear: {e}', 'danger')

    alumnos = Alumno.query.order_by(Alumno.apellido).all()
    planeaciones = Planeacion.query.limit(100).all()
    return render_template('calificaciones/form.html', alumnos=alumnos, planeaciones=planeaciones, calificacion=None)


@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    cal = Calificacion.query.get_or_404(id)
    if request.method == 'POST':
        cal.alumno_id = request.form.get('alumno_id')
        cal.planeacion_id = request.form.get('planeacion_id') or None
        cal.valor = request.form.get('valor')
        cal.tipo = request.form.get('tipo')
        cal.fecha = request.form.get('fecha') or None
        cal.comentarios = request.form.get('comentarios')
        try:
            db.session.commit()
            flash('Calificación actualizada.', 'success')
            return redirect(url_for('calificaciones.index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar: {e}', 'danger')

    alumnos = Alumno.query.order_by(Alumno.apellido).all()
    planeaciones = Planeacion.query.limit(100).all()
    return render_template('calificaciones/form.html', alumnos=alumnos, planeaciones=planeaciones, calificacion=cal)


@bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    cal = Calificacion.query.get_or_404(id)
    try:
        db.session.delete(cal)
        db.session.commit()
        flash('Calificación eliminada.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar: {e}', 'danger')
    return redirect(url_for('calificaciones.index'))
