from guardar_datos import cargar_json, guardar_json
from datetime import datetime
def registrar_alumno():
    try:
        print("\n--- Registro de Alumno ---")
        nombre = input("Ingrese su nombre completo: ").strip().upper()
        if nombre.isdigit():
            raise ValueError("Erorr: no puede haber numeros en el nombre")
        documento = input("Ingrese su documento de identidad: ").strip()
        if not documento.isdigit():
            raise  ValueError("Error no puede haber letras en el documento")
        clientes = cargar_json("clientes.json", {})
        
        if documento in clientes:
            print("¡Usted ya se encuentra registrado en el sistema!")
        else:
            clientes[documento] = {"nombre": nombre}
            guardar_json("clientes.json", clientes)
            print(f"¡Registro exitoso! Bienvenido a DriveSafe, {nombre}.")
    except ValueError as e:
        print(f"{e}")
    


def apartar_cita():
    try:
        print("\n--- Agendar Cita de Práctica ---")
        documento = input("Ingrese su documento de identidad para validar su registro: ").strip()
        if not documento.isdigit():
                raise  ValueError("Error no puede haber letras en el documento")
        clientes = cargar_json("clientes.json", {})
        if documento not in clientes:
            print("Error: No está registrado. Por favor, regístrese primero (Opción 1).")
            print("-"*30)
            return
            
        nombre_alumno = clientes[documento]["nombre"]
        
        datos_vehiculos = cargar_json("vehiculos.json", {"carros": {}, "motos": {}})
        tipo = input("¿Desea practicar en MOTO o CARRO?: ").strip().upper()
        
        if tipo == "CARRO":
            vehiculos = datos_vehiculos.get("carros", {})
        elif tipo == "MOTO":
            vehiculos = datos_vehiculos.get("motos", {})
        else:
            print("Error: Tipo de vehículo no válido.")
            print("-"*30)
            return

        print(f"\n--- {tipo}S DISPONIBLES ---")
        hay_opciones = False
        for placa, info in vehiculos.items():
            instructor = info.get("instructor_asignado", "Sin instructor asignado")
            print(f"Placa: {placa} | Vehículo: {info['nombre']} | Instructor: {instructor}")
            hay_opciones = True
            
        if not hay_opciones:
            print("No hay vehículos disponibles por el momento.")
            print("-"*30)
            return
            
        placa_elegida = input("\nIngrese la placa del vehículo con el que desea practicar: ").strip()
        
        if placa_elegida not in vehiculos:
            print("Error: La placa ingresada no existe en la lista.")
            print("-"*30)
            return
        while True:
            try:    
                fecha=datetime.strptime(input("Introduce la fecha (DD/MM/AAAA): "), "%d/%m/%Y").date()
                print("¡Fecha guardada con éxito!")
                print("Fecha registrada:", fecha.strftime("%d/%m/%Y"))
                print("-"*30)
                break
            except ValueError:
                print("¡Error! La fecha contiene letras, faltan números o el formato no es DD/MM/AAAA.")
                print("-"*30)
        while True:
            try:
                hora = datetime.strptime(input("Introduce la hora (HH:MM): "), "%H:%M").time()
                
                print("¡Hora guardada con éxito!")
                print("Hora registrada:", hora.strftime("%H:%M"))
                print("-"*30)
                break

            except ValueError:
                print("¡Error! Hora incorrecta. No uses letras y respeta el formato HH:MM (ej: 14:00).")
                print("-"*30)
        
    
        citas = cargar_json("citas.json", [])
        
        nueva_cita = {
            "documento": documento,
            "alumno": nombre_alumno,
            "tipo": tipo,
            "placa": placa_elegida,
            "instructor": vehiculos[placa_elegida].get("instructor_asignado", "Pendiente de asignar"),
            "fecha": fecha.strftime("%d/%m/%Y"),
            "hora": hora.strftime("%H:%M")
        }
        
        citas.append(nueva_cita)
        guardar_json("citas.json", citas)
        
        print("\n¡Cita agendada con éxito!")
        print(f"Detalles: {fecha} a las {hora} - Vehículo: {placa_elegida}")
        print("-"*30)
    except ValueError as e:
        print(f"{e}")
        print("-"*30)

def consultar_citas():
    print("\n--- Mis Citas Programadas ---")
    documento = input("Ingrese su documento de identidad: ").strip()
    if not documento.isdigit():
        print("No es un documento valido o ingrese correctamente su documento o si esta registrando alguna letra")
        print("-"*30)
        return
    citas = cargar_json("citas.json", [])
    
    citas_alumno = [cita for cita in citas if cita["documento"] == documento]
    
    if citas_alumno:
        for i, cita in enumerate(citas_alumno, 1):
            print(f"{i}. Fecha: {cita['fecha']} | Hora: {cita['hora']} | Vehículo: {cita['placa']} ({cita['tipo']}) | Instructor: {cita['instructor']}")
    else:
        print("Usted no tiene citas programadas actualmente.")
        print("-"*30)

def menuClientes():
    while True:
        try:
            print("\n==============================================================")
            print("          DRIVESAFE ---  Portal de Alumnos")
            print("==============================================================")
            print("Bienvenido al menu, ¿que deseas realizar el dia de hoy?:")
            print("Ingrese '1' para registrarse")
            print("Ingrese '2' para apartar una cita")
            print("Ingrese '3' para consultar proximas citas")
            print("Ingrese '4' para cerrar sesion")
            alter = int(input("Ingrese un numero para seleccionar una opcion: "))
            
            if alter == 4: 
                print("==============================================================")
                print("                      Hasta pronto"                            )
                print("==============================================================")
                break
            elif alter == 1:
                registrar_alumno()
            elif alter == 2:
                apartar_cita()
            elif alter == 3:
                consultar_citas()
            else:
                print("\nOpción fuera de rango. Ingrese un número entre 1 y 4.")
                
        except ValueError:
            print("\n==============================================================")
            print("No se ha podido registrar la opcion,ingrese un numero entero")
            print("==============================================================")