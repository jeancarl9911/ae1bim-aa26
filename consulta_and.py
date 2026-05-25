from configuracion import session
from crear_base_entidades import Profesor

from sqlalchemy import and_

profesores = session.query(Profesor).filter(
    and_(
        Profesor.nombres == "Juan",
        Profesor.especialidad == "Bases de Datos"
    )
).all()

for p in profesores:
    print(p)
    