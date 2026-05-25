from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from configuracion import Base, engine


class Facultad(Base):

    __tablename__ = 'facultades'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    ubicacion = Column(String)
    decano = Column(String)

    carreras = relationship("Carrera", back_populates="facultad")

    def __str__(self):
        return f"{self.nombre} - {self.decano}"


class Carrera(Base):

    __tablename__ = 'carreras'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    codigo = Column(String)

    facultad_id = Column(Integer, ForeignKey('facultades.id'))

    facultad = relationship("Facultad", back_populates="carreras")

    profesores = relationship("Profesor", back_populates="carrera")

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"


class Profesor(Base):

    __tablename__ = 'profesores'

    id = Column(Integer, primary_key=True)

    nombres = Column(String)
    apellidos = Column(String)
    correo = Column(String)
    especialidad = Column(String)

    carrera_id = Column(Integer, ForeignKey('carreras.id'))

    carrera = relationship("Carrera", back_populates="profesores")

    recursos = relationship("RecursoAcademico", back_populates="profesor")

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class RecursoAcademico(Base):

    __tablename__ = 'recursos'

    id = Column(Integer, primary_key=True)

    titulo = Column(String)
    fecha_publicacion = Column(Date)
    tipo = Column(String)
    url = Column(String)

    profesor_id = Column(Integer, ForeignKey('profesores.id'))

    profesor = relationship("Profesor", back_populates="recursos")

    def __str__(self):
        return f"{self.titulo} - {self.tipo}"


Base.metadata.create_all(engine)

print("Base de datos creada correctamente")