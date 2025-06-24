import os
import time

from db.connection import engine
from core.models import Base
from core.views import *

OPT = {
    "1": create_cliente_view,
    "2": create_manicurista_view,
    "3": create_servicio_view,
    "4": read_all_clientes_view,
    "5": read_all_manicuristas_view,
    "6": read_all_servicios_view,
    "7": read_cliente_by_id_view,
    "8": read_manicurista_by_id_view,
    "9": read_servicio_by_id_view,
    "10": update_cliente_view,
    "11": update_manicurista_view,
    "12": update_servicio_view,
    "13": delete_cliente_view,
    "14": delete_manicurista_view,
    "15": delete_servicio_view,
}

def wait_and_clear(s: int) -> None:
    time.sleep(s)
    os.system("cls" if os.name == "nt" else "clear")

def main():
    while True:
        print("=== CRUD Estudio de Uñas ===\n")
        print("1. Crear Cliente")
        print("2. Crear Manicurista")
        print("3. Crear Servicio")
        print("4. Ver todos los Clientes")
        print("5. Ver todos los Manicuristas")
        print("6. Ver todos los Servicios")
        print("7. Ver Cliente por ID")
        print("8. Ver Manicurista por ID")
        print("9. Ver Servicio por ID")
        print("10. Actualizar Cliente")
        print("11. Actualizar Manicurista")
        print("12. Actualizar Servicio")
        print("13. Eliminar Cliente")
        print("14. Eliminar Manicurista")
        print("15. Eliminar Servicio")
        print("0. Salir")
        opt = input("\nSelecciona una opción: ").strip()

        if opt == "0":
            break
        elif opt in OPT:
            wait_and_clear(0)
            OPT[opt]()
            if int(opt) >= 4:
                input("\nPresiona cualquier tecla para continuar...")
                wait_and_clear(0)
            else:
                wait_and_clear(1)
        else:
            print("Opción inválida.")
            wait_and_clear(1)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    main()
