from configuracion import session
from crear_base_entidades import Profesor

profesores = session.query(Profesor).filter(
    Profesor.especialidad == "Bases de Datos"
).all()

for p in profesores:
    print(p)
    