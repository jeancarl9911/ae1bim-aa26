from configuracion import session
from crear_base_entidades import Carrera

carreras = session.query(Carrera).order_by(
    Carrera.nombre
).all()

for c in carreras:
    print(c)
    