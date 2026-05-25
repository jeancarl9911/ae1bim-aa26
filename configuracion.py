
import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative 

#conexion sqlite
engine = sqlalchemy.create_engine('sqlite:///universidad.db')

#sesion 
session = sqlalchemy.orm.sessionmaker(bind=engine)
session = session()

#base orm
Base = sqlalchemy.ext.declarative.declarative_base()
