from guardar_datos import cargar_json, guardar_json

def Menu():
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
    
    carros = datos_vehiculos["carros"]
    motos = datos_vehiculos["motos"]
    asistencias_por_cliente = cargar_json("asistencias.json", {})
    
    nombre_instructor = ""
    registro_especialidad = ""

    while True:
        print("\n" + "="*40)
        print("Menu para el instructor")
        print("1. Para registrar su especialidad y su nombre")
        print("2. Para registrar el vehiculo")
        print("3. Para consultar las citas con clientes y la fecha")
        print("4. Registrar asistencia y observaciones del cliente")
        print("5. Consultar historial de practicas del cliente")
        print("6. Liberar vehiculo")
        print("7. Cerrar sesion")
        
        try:
            opcion = int(input("Ingrese la opcion que desea realizar: "))
        except ValueError as e:
            print("\n" + "="*50)
            print(f"❌ TIPO DE ERROR: {type(e).__name__}")
            print(f"Detalles técnicos: {e}")
            print("Solución: Por favor, ingrese un número entero válido.")
            print("="*50 + "\n")
            continue

        if opcion == 1:
            while True:
                try:
                    nombre_instructor = input("Ingrese su nombre, instructor: ").strip()

                    if nombre_instructor.isdigit():
                        raise ValueError("No se permiten valores numéricos para el nombre del instructor.")
                    break 
                except ValueError as e:
                    print("\n" + "="*50)
                    print(f"❌ TIPO DE ERROR: {type(e).__name__}")
                    print(f"Detalles técnicos: {e}")
                    print("Solución: Debe ingresar un nombre válido con letras (no un número).")
                    print("="*50 + "\n")
                    
            while True:
                a = input("Su especialidad (moto o carro): ").strip().upper()
                if a in ["MOTO", "CARRO"]:
                    registro_especialidad = a
                    print(f"Instructor {nombre_instructor} registrado con especialidad en {registro_especialidad}")
                    break    
                else:
                    print("Error: Digite Moto o Carro, no un número o decimal o palabra ajena (carro o moto).")
                    
        elif opcion == 2:
            if not nombre_instructor or not registro_especialidad:
                print("Error: Primero debe registrar su nombre y especialidad (Opción 1).")
                continue

            print(f"\n--- LISTA DE VEHÍCULOS ({registro_especialidad}S) ---")
            
            vehiculos_mostrar = carros if registro_especialidad == "CARRO" else motos
            
            for p, info in vehiculos_mostrar.items():
                estado = info.get("disponibilidad", "Desconocido")
                instructor = info.get("instructor_asignado", "Sin asignar")
                print(f"Placa: {p} | Vehículo: {info['nombre']} | Estado: {estado} | Instructor actual: {instructor}")
            print("-" * 40)
                
            placa = input("\nIngrese la placa del vehiculo que desea registrar a su nombre: ").strip() 
            
            if registro_especialidad == "CARRO":
                if placa in carros:
                    if carros[placa].get("disponibilidad") == "No Disponible":
                        print(f" ❌ Error: El carro con placa {placa} ya está asignado a otro instructor y no está disponible.")
                    else:
                        carros[placa]["disponibilidad"] = "No Disponible"
                        carros[placa]["instructor_asignado"] = nombre_instructor
                        guardar_json("vehiculos.json", datos_vehiculos)
                        print(f"✅ Éxito: El {carros[placa]['nombre']} ha sido asignado al instructor {nombre_instructor}.")
                        
                        citas = cargar_json("citas.json", [])
                        citas_modificadas = False
                        for cita in citas:
                            if cita.get("placa") == placa and cita.get("instructor") == "Sin asignar":
                                cita["instructor"] = nombre_instructor
                                citas_modificadas = True
                        if citas_modificadas:
                            guardar_json("citas.json", citas)
                            print(f"✅ Sistema: Cita(s) vinculada(s) a la placa {placa} actualizadas con el instructor {nombre_instructor}.")

                else:
                    print("Error: El carro no está registrado en el sistema.")
            elif registro_especialidad == "MOTO":
                if placa in motos:
                    if motos[placa].get("disponibilidad") == "No Disponible":
                        print(f"❌ Error: La moto con placa {placa} ya está asignada a otro instructor y no está disponible.")
                    else:
                        motos[placa]["disponibilidad"] = "No Disponible"
                        motos[placa]["instructor_asignado"] = nombre_instructor
                        guardar_json("vehiculos.json", datos_vehiculos) 
                        print(f"✅ Éxito: La {motos[placa]['nombre']} ha sido asignada al instructor {nombre_instructor}.")
                        citas = cargar_json("citas.json", [])
                        citas_modificadas = False
                        for cita in citas:
                            if cita.get("placa") == placa and cita.get("instructor") == "Sin asignar":
                                cita["instructor"] = nombre_instructor
                                citas_modificadas = True
                        if citas_modificadas:
                            guardar_json("citas.json", citas)
                            print(f"✅ Sistema: Cita(s) vinculada(s) a la placa {placa} actualizadas con el instructor {nombre_instructor}.")

                else:
                    print("Error: La moto no está registrada en el sistema.")
            
        elif opcion == 3:
            citas = cargar_json("citas.json", [])
            
            if not citas:
                print("No hay citas registradas en el sistema actualmente.")
                continue
                
            nombre_cliente = input("Registre el nombre del cliente para consultar la cita y la fecha: ").strip().upper()
            citas_encontradas = [cita for cita in citas if cita["alumno"].upper() == nombre_cliente]
            
            if citas_encontradas:
                print(f"\n--- Citas encontradas para el cliente: {nombre_cliente} ---")
                for i, cita in enumerate(citas_encontradas, 1):
                    print(f"Cita {i}: Fecha: {cita['fecha']} | Hora: {cita['hora']} | Instructor asignado: {cita['instructor']} | Vehículo: {cita['placa']} ({cita['tipo']})")
            else:
                print(f"No se encontró ninguna cita registrada a nombre de {nombre_cliente}.")
        elif opcion == 4:
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip().upper()
            
            if nombre_cliente not in asistencias_por_cliente:
                asistencias_por_cliente[nombre_cliente] = []
                
        
        
            while True:
                asistencia = input(f"Ingrese la asistencia de {nombre_cliente} ('Presente' o 'Ausente'): ").strip().upper()
                
                if asistencia == "PRESENTE" or asistencia == "AUSENTE":
                    break  
                else:
                    print("❌ Error: Entrada inválida. Solo se admite escribir 'Presente' o 'Ausente'.\n")

            observacion = input("Ingrese si tiene alguna observación del cliente: ").strip()
            
            registro = {"estado": asistencia, "observacion": observacion}
            asistencias_por_cliente[nombre_cliente].append(registro)
    
            guardar_json("asistencias.json", asistencias_por_cliente) 
            print(f"✅ Asistencia guardada con éxito para {nombre_cliente}.")
            
        elif opcion == 5:
            cliente_buscar = input("Ingrese el nombre del cliente para ver su historial: ").strip().upper()
            if cliente_buscar in asistencias_por_cliente:
                print(f"\n--- Historial de {cliente_buscar} ---")
                for i, registro in enumerate(asistencias_por_cliente[cliente_buscar], 1):
                    print(f"Clase {i}: Asistencia: {registro['estado']} | Observaciones: {registro['observacion']}")
            else:
                print("El cliente no tiene historial registrado.")

        elif opcion == 6:
            if not nombre_instructor or not registro_especialidad:
                print("Error: Primero debe registrar su nombre y especialidad (Opción 1).")
                continue
            print(f"\n--- LISTA DE VEHÍCULOS ({registro_especialidad}S) ---")
            vehiculos_mostrar = carros if registro_especialidad == "CARRO" else motos
            
            for p, info in vehiculos_mostrar.items():
                estado = info.get("disponibilidad", "Desconocido")
                instructor = info.get("instructor_asignado", "Sin asignar")
                print(f"Placa: {p} | Vehículo: {info['nombre']} | Estado: {estado} | Instructor actual: {instructor}")
            print("-" * 40)
            
            placa_liberar = input("Ingrese la placa del vehículo que desea liberar: ").strip()
            
            if placa_liberar in vehiculos_mostrar:
                vehiculo = vehiculos_mostrar[placa_liberar]
                
                if vehiculo.get("disponibilidad") == "Disponible":
                    print(f"❌ Error: El vehículo con placa {placa_liberar} ya se encuentra 'Disponible', no es necesario liberarlo.")
                 
                elif vehiculo.get("instructor_asignado") != nombre_instructor:
                    instructor_actual = vehiculo.get('instructor_asignado')
                    print(f"❌ Error Acceso Denegado: No puedes liberar este vehículo porque está asignado a '{instructor_actual}'. (Tu nombre registrado es '{nombre_instructor}').")
                
                else:
                    vehiculo["disponibilidad"] = "Disponible"
                    vehiculo["instructor_asignado"] = "Sin asignar"
                    guardar_json("vehiculos.json", datos_vehiculos)
                    print(f"✅ Éxito: El vehículo {placa_liberar} ha sido devuelto y ahora está Disponible para otros instructores.")
            else:
                print(f"❌ Error: La placa {placa_liberar} no está registrada en el sistema de {registro_especialidad}S.")
        
        elif opcion == 7:
            print("Saliendo del menú del instructor.")
            break
            
        else:
            print("Opción inválida, ingrese una de las opciones disponibles en el menu")