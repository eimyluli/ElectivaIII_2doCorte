from db.connection import Session
from core.models import Cliente, FichaCliente, Manicurista, Servicio
import datetime

session = Session()

# ----------- CREAR DATOS DE LA BASE DE DATOS -----------

def create_cliente_view():
    nombre_completo = input("Nombre completo del cliente: ")
    cedula = input("Cédula del cliente: ")
    telefono = input("Teléfono: ")
    notas = input("Notas adicionales: ")
    cliente = Cliente(nombre_completo=nombre_completo, cedula=cedula, telefono=telefono)
    ficha = FichaCliente(notas=notas, cliente=cliente)
    session.add(cliente)
    session.add(ficha)
    session.commit()
    print("Cliente registrado con éxito.")

def create_manicurista_view():
    nombre_completo = input("Nombre completo de la manicurista: ")
    cedula = input("Cédula de la manicurista: ")
    fecha_ingreso_input = input("Fecha de ingreso (YYYY-MM-DD) (dejar vacío para hoy): ")
    if fecha_ingreso_input.strip():
        fecha_ingreso = datetime.datetime.strptime(fecha_ingreso_input, "%Y-%m-%d").date()
    else:
        fecha_ingreso = datetime.date.today()
    m = Manicurista(nombre_completo=nombre_completo, cedula=cedula, fecha_ingreso=fecha_ingreso)
    session.add(m)
    session.commit()
    print("Manicurista registrada con éxito.")

def create_servicio_view():
    tipo = input("Tipo de servicio (ej. uñas acrílicas): ")
    precio = float(input("Precio: "))
    id_manicurista = int(input("ID de la manicurista: "))
    servicio = Servicio(tipo=tipo, precio=precio, id_manicurista=id_manicurista)

    agregar_clientes = input("¿Asignar clientes a este servicio? (s/n): ").lower()
    if agregar_clientes == "s":
        ids = input("IDs de los clientes separados por coma: ")
        for cid in ids.split(","):
            cliente = session.get(Cliente, int(cid.strip()))
            if cliente:
                servicio.clientes.append(cliente)

    session.add(servicio)
    session.commit()
    print("Servicio creado con éxito.")

# ----------- LEER TODOS -----------

def read_all_clientes_view():
    clientes = session.query(Cliente).all()
    for c in clientes:
        print(f"{c.id}. {c.nombre_completo} - {c.cedula} - {c.telefono}")

def read_all_manicuristas_view():
    manis = session.query(Manicurista).all()
    for m in manis:
        print(f"{m.id}. {m.nombre_completo} - {m.cedula} - {m.fecha_ingreso}")

def read_all_servicios_view():
    servicios = session.query(Servicio).all()
    for s in servicios:
        print(f"{s.id}. {s.tipo} - ${s.precio}")

# ----------- LEER POR ID  DE LA BASE DE DATOS -----------

def read_cliente_by_id_view():
    cid = int(input("ID del cliente: "))
    c = session.get(Cliente, cid)
    if c:
        print(c)
        print(f"Ficha: {c.ficha}")
        print(f"Servicios: {c.servicios}")
    else:
        print("Cliente no encontrado.")

def read_manicurista_by_id_view():
    mid = int(input("ID de la manicurista: "))
    m = session.get(Manicurista, mid)
    if m:
        print(m)
        print(f"Servicios: {m.servicios}")
    else:
        print("Manicurista no encontrada.")

def read_servicio_by_id_view():
    sid = int(input("ID del servicio: "))
    s = session.get(Servicio, sid)
    if s:
        print(s)
        print(f"Manicurista: {s.manicurista}")
        print(f"Clientes: {s.clientes}")
    else:
        print("Servicio no encontrado.")

# ----------- ACTUALIZAR DATOS DE LA BASE DE DATOS-----------

def update_cliente_view():
    cid = int(input("ID del cliente a actualizar: "))
    c = session.get(Cliente, cid)
    if c:
        c.nombre_completo = input(f"Nuevo nombre completo ({c.nombre_completo}): ") or c.nombre_completo
        c.cedula = input(f"Nueva cédula ({c.cedula}): ") or c.cedula
        c.telefono = input(f"Nuevo teléfono ({c.telefono}): ") or c.telefono
        session.commit()
        print("Cliente actualizado.")
    else:
        print("Cliente no encontrado.")

def update_manicurista_view():
    mid = int(input("ID de la manicurista a actualizar: "))
    m = session.get(Manicurista, mid)
    if m:
        m.nombre_completo = input(f"Nuevo nombre completo ({m.nombre_completo}): ") or m.nombre_completo
        m.cedula = input(f"Nueva cédula ({m.cedula}): ") or m.cedula
        fecha_ingreso_input = input(f"Nueva fecha de ingreso ({m.fecha_ingreso}): ")
        if fecha_ingreso_input.strip():
            m.fecha_ingreso = datetime.datetime.strptime(fecha_ingreso_input, "%Y-%m-%d").date()
        session.commit()
        print("Manicurista actualizada.")
    else:
        print("Manicurista no encontrada.")

def update_servicio_view():
    sid = int(input("ID del servicio a actualizar: "))
    s = session.get(Servicio, sid)
    if s:
        s.tipo = input(f"Nuevo tipo ({s.tipo}): ") or s.tipo
        nuevo_precio = input(f"Nuevo precio ({s.precio}): ")
        if nuevo_precio:
            s.precio = float(nuevo_precio)
        session.commit()
        print("Servicio actualizado.")
    else:
        print("Servicio no encontrado.")

# ----------- ELIMINAR DATOS DE LA BASE DE DATOS-----------

def delete_cliente_view():
    cid = int(input("ID del cliente a eliminar: "))
    c = session.get(Cliente, cid)
    if c:
        session.delete(c)
        session.commit()
        print("Cliente eliminado.")
    else:
        print("Cliente no encontrado.")

def delete_manicurista_view():
    mid = int(input("ID de la manicurista a eliminar: "))
    m = session.get(Manicurista, mid)
    if m:
        session.delete(m)
        session.commit()
        print("Manicurista eliminada.")
    else:
        print("Manicurista no encontrada.")

def delete_servicio_view():
    sid = int(input("ID del servicio a eliminar: "))
    s = session.get(Servicio, sid)
    if s:
        session.delete(s)
        session.commit()
        print("Servicio eliminado.")
    else:
        print("Servicio no encontrado.")
