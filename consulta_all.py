from configuracion import session
from crear_base_entidades import Facultad

facultades = session.query(Facultad).all()

for f in facultades:
    print(f)
    