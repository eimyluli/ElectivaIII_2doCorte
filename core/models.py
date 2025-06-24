from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, Date
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db.connection import Base
import datetime

# Tabla intermedia para relación muchos a muchos Cliente - Servicio
cliente_servicio = Table(
    'cliente_servicio',
    Base.metadata,
    Column('cliente_id', ForeignKey('clientes.id'), primary_key=True),
    Column('servicio_id', ForeignKey('servicios.id'), primary_key=True)
)

class Cliente(Base):
    __tablename__ = 'clientes'

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre_completo: Mapped[str] = mapped_column(String(100))
    cedula: Mapped[str] = mapped_column(String(20), unique=True)
    telefono: Mapped[str] = mapped_column(String(20))

    ficha = relationship("FichaCliente", back_populates="cliente", uselist=False)
    servicios = relationship("Servicio", secondary=cliente_servicio, back_populates="clientes")

    def __repr__(self):
        return f"<Cliente(nombre_completo={self.nombre_completo}, cedula={self.cedula}, telefono={self.telefono})>"

class FichaCliente(Base):
    __tablename__ = 'fichas'

    id: Mapped[int] = mapped_column(primary_key=True)
    fecha_registro: Mapped[datetime.date] = mapped_column(default=datetime.date.today)
    notas: Mapped[str] = mapped_column(String(200))
    cliente_id: Mapped[int] = mapped_column(ForeignKey('clientes.id'), unique=True)

    cliente = relationship("Cliente", back_populates="ficha")

    def __repr__(self):
        return f"<FichaCliente(fecha_registro={self.fecha_registro}, notas={self.notas})>"

class Manicurista(Base):
    __tablename__ = 'manicuristas'

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre_completo: Mapped[str] = mapped_column(String(100))
    cedula: Mapped[str] = mapped_column(String(20), unique=True)
    fecha_ingreso: Mapped[datetime.date] = mapped_column(default=datetime.date.today)

    servicios = relationship("Servicio", back_populates="manicurista")

    def __repr__(self):
        return f"<Manicurista(nombre_completo={self.nombre_completo}, cedula={self.cedula}, fecha_ingreso={self.fecha_ingreso})>"

class Servicio(Base):
    __tablename__ = 'servicios'

    id: Mapped[int] = mapped_column(primary_key=True)
    tipo: Mapped[str] = mapped_column(String(50))
    precio: Mapped[float] = mapped_column()

    id_manicurista: Mapped[int] = mapped_column(ForeignKey('manicuristas.id'))
    manicurista = relationship("Manicurista", back_populates="servicios")

    clientes = relationship("Cliente", secondary=cliente_servicio, back_populates="servicios")

    def __repr__(self):
        return f"<Servicio(tipo={self.tipo}, precio={self.precio})>"
