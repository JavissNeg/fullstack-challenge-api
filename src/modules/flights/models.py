from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from src.core.database import Base

class Aerolinea(Base):
    __tablename__ = "aerolineas"
    
    id_aerolinea = Column(Integer, primary_key=True, index=True)
    nombre_aerolinea = Column(String(100), nullable=False)
    
    vuelos = relationship("Vuelo", back_populates="aerolinea")

class Aeropuerto(Base):
    __tablename__ = "aeropuertos"
    
    id_aeropuerto = Column(Integer, primary_key=True, index=True)
    nombre_aeropuerto = Column(String(100), nullable=False)
    
    vuelos = relationship("Vuelo", back_populates="aeropuerto")

class Movimiento(Base):
    __tablename__ = "movimientos"
    
    id_movimiento = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(50), nullable=False)
    
    vuelos = relationship("Vuelo", back_populates="movimiento")

class Vuelo(Base):
    __tablename__ = "vuelos"
    
    id_vuelo = Column(Integer, primary_key=True, index=True)
    id_aerolinea = Column(Integer, ForeignKey("aerolineas.id_aerolinea"), nullable=False)
    id_aeropuerto = Column(Integer, ForeignKey("aeropuertos.id_aeropuerto"), nullable=False)
    id_movimiento = Column(Integer, ForeignKey("movimientos.id_movimiento"), nullable=False)
    dia = Column(Date, nullable=False)
    
    aerolinea = relationship("Aerolinea", back_populates="vuelos")
    aeropuerto = relationship("Aeropuerto", back_populates="vuelos")
    movimiento = relationship("Movimiento", back_populates="vuelos")
