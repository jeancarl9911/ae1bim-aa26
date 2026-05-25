from configuracion import session
from crear_base_entidades import RecursoAcademico

from sqlalchemy import or_

recursos = session.query(RecursoAcademico).filter(
    or_(
        RecursoAcademico.tipo == "Libro",
        RecursoAcademico.tipo == "Video"
    )
).all()

for r in recursos:
    print(r)
    