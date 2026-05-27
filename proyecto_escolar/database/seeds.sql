USE control_escolar;

-- Insertar docentes de ejemplo
INSERT INTO docentes (numero_empleado, nombre, apellido, email, telefono, especialidad)
VALUES
('EMP001','Ana','Gomez','ana.gomez@school.local','555-1001','Matematicas'),
('EMP002','Luis','Perez','luis.perez@school.local','555-1002','Fisica');

-- Insertar materias
INSERT INTO materias (clave, nombre, descripcion, creditos, horas_semana)
VALUES
('MAT101','Matemáticas I','Álgebra y trigonometría',5,6),
('FIS101','Física I','Mecánica básica',5,6);

-- Insertar grupos
INSERT INTO grupos (nombre, semestre, aula, turno_id)
VALUES
('A',1,'101',1),
('B',1,'102',1);

-- Insertar alumnos
INSERT INTO alumnos (matricula, nombre, apellido, grupo_id)
VALUES
('A001','Carlos','Lopez',1),
('A002','María','Sanchez',1),
('A003','Jose','Martinez',2);

-- Insertar planeaciones
INSERT INTO planeaciones (grupo_id, materia_id, docente_id, dia_semana, hora_inicio, hora_fin, aula, periodo_escolar)
VALUES
(1,1,1,'Lunes','08:00:00','10:00:00','101','2026-1'),
(1,2,2,'Martes','10:00:00','12:00:00','101','2026-1');

-- Insertar calificación de ejemplo
INSERT INTO calificaciones (alumno_id, planeacion_id, docente_id, valor, tipo, fecha, comentarios)
VALUES
(1,1,1,8.5,'Parcial','2026-05-20','Buen desempeño');
