from datetime import date

from configuracion import session

from crear_base_entidades import Facultad
from crear_base_entidades import Carrera
from crear_base_entidades import Profesor
from crear_base_entidades import RecursoAcademico


# =============
# FACULTADES
# =============

f1 = Facultad(
    nombre="Facultad de Ingeniería",
    ubicacion="Bloque A",
    decano="Carlos Perez"
)

f2 = Facultad(
    nombre="Facultad de Ciencias Sociales",
    ubicacion="Bloque B",
    decano="Maria Gomez"
)

session.add_all([f1, f2])
session.commit()


# =============
# CARRERAS
# =============

c1 = Carrera(
    nombre="Ingeniería en Sistemas",
    codigo="IS01",
    facultad=f1
)

c2 = Carrera(
    nombre="Ingeniería Civil",
    codigo="IC02",
    facultad=f1
)

c3 = Carrera(
    nombre="Psicología",
    codigo="PS03",
    facultad=f2
)

session.add_all([c1, c2, c3])
session.commit()


# =============
# PROFESORES
# =============

p1 = Profesor(
    nombres="Juan",
    apellidos="Lopez",
    correo="juan@uni.edu",
    especialidad="Bases de Datos",
    carrera=c1
)

p2 = Profesor(
    nombres="Ana",
    apellidos="Martinez",
    correo="ana@uni.edu",
    especialidad="Estructuras",
    carrera=c2
)

session.add_all([p1, p2])
session.commit()


# =============
# RECURSOS
# ============= 

r1 = RecursoAcademico(
    titulo="Manual SQL",
    fecha_publicacion=date(2024, 5, 10),
    tipo="Libro",
    url="https://ejemplo.com/sql",
    profesor=p1
)

r2 = RecursoAcademico(
    titulo="Video de Estructuras",
    fecha_publicacion=date(2024, 6, 15),
    tipo="Video",
    url="https://ejemplo.com/video",
    profesor=p2
)

session.add_all([r1, r2])
session.commit()

print("Datos ingresados correctamente")