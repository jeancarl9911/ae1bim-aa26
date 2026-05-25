from configuracion import session

from crear_base_entidades import Facultad
from crear_base_entidades import Carrera
from crear_base_entidades import Profesor
from crear_base_entidades import RecursoAcademico

from sqlalchemy import or_
from sqlalchemy import and_


# =============
# ALL
# =============

print("\nCONSULTA ALL")

facultades = session.query(Facultad).all()

for f in facultades:
    print(f)


# =============
# FILTER
# =============

print("\nCONSULTA FILTER")

profesores = session.query(Profesor).filter(
    Profesor.especialidad == "Bases de Datos"
).all()

for p in profesores:
    print(p)


# =============
# ORDER BY
# =============

print("\nCONSULTA ORDER BY")

carreras = session.query(Carrera).order_by(
    Carrera.nombre
).all()

for c in carreras:
    print(c)


# =============
# OR
# =============

print("\nCONSULTA OR")

recursos = session.query(RecursoAcademico).filter(
    or_(
        RecursoAcademico.tipo == "Libro",
        RecursoAcademico.tipo == "Video"
    )
).all()

for r in recursos:
    print(r)


# =============
# AND
# =============

print("\nCONSULTA AND")

profesores_and = session.query(Profesor).filter(
    and_(
        Profesor.especialidad == "Bases de Datos",
        Profesor.nombres == "Juan"
    )
).all()

for p in profesores_and:
    print(p)
