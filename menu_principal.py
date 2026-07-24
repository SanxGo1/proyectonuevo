from Proyecto_instructor import Menu
from guardar_datos import cargar_json, guardar_json
from menu_clientes import menuClientes

def inicio():
    datos_vehiculos = cargar_json("vehiculos.json", {
            "carros": {
                "ABC123": {"nombre": "Carro A", "disponibilidad": "Disponible"},
                "BII678": {"nombre": "Carro B", "disponibilidad": "Disponible"},
                "WTF101": {"nombre": "Carro C", "disponibilidad": "Disponible"}
            },
            "motos": {
                "BOF12C": {"nombre": "Moto A", "disponibilidad": "Disponible"},
                "NVO57B": {"nombre": "Moto B", "disponibilidad": "Disponible"},
                "OJO158I": {"nombre": "Moto C", "disponibilidad": "Disponible"}
            }
        })
    guardar_json("vehiculos.json", datos_vehiculos)
    while True:
        print("\n" + "*"*50)
        print(" BIENVENIDO AL SISTEMA DRIVESAFE ")
        print("*"*50)
        print("1. Entrar como Instructor")
        print("2. Entrar como Alumno")
        print("3. Apagar sistema")
        
        try:
            opcion = int(input("Seleccione su perfil (1-3): "))
            
            if opcion == 1:
                Menu()
            elif opcion == 2:
                menuClientes()
            elif opcion == 3:
                print("Apagando el sistema... ¡Hasta luego!")
                break
            else:
                print("Opción incorrecta.")
        except ValueError:
            print("Por favor, ingrese un número.")


if __name__ == "__main__":
    inicio()