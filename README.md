# 🚗 DriveSafe - Sistema de Gestión para Escuela de Conducción

**DriveSafe** es una aplicación de consola desarrollada en Python para gestionar las operaciones diarias de una escuela de manejo. El sistema divide sus funciones en dos portales principales: uno para los **Alumnos** y otro para los **Instructores**, permitiendo un control completo sobre el registro de usuarios, asignación de vehículos, programación de citas y control de asistencia.

---

## 🛠️ Características Principales

El sistema está dividido en dos perfiles de usuario con funcionalidades específicas:

### 🎓 Portal de Alumnos (`menu_clientes.py`)
* **Registro de Alumnos:** Los usuarios pueden registrarse en el sistema utilizando su nombre completo y documento de identidad.
* **Agendamiento de Citas:** Permite a los alumnos registrados agendar prácticas seleccionando el tipo de vehículo (Moto o Carro), eligiendo un vehículo disponible, y asignando una fecha y hora.
* **Consulta de Citas:** Los alumnos pueden consultar en cualquier momento su cronograma de prácticas programadas ingresando su documento.

### 🚦 Portal de Instructores (`Proyecto_instructor.py`)
* **Registro de Perfil:** El instructor debe registrar su nombre y su especialidad (MOTO o CARRO) antes de realizar cualquier acción. El sistema cuenta con validación estricta de nombres (no permite números).
* **Asignación de Vehículos:** Los instructores pueden ver una lista de vehículos de su especialidad y asignarse uno que esté "Disponible". El sistema bloquea el registro si el vehículo ya está en uso.
* **Liberación de Vehículos:** Permite al instructor devolver el vehículo al estado "Disponible" una vez terminada su jornada. (Incluye medidas de seguridad para que un instructor no pueda liberar el vehículo de otro compañero).
* **Consulta de Citas:** Permite al instructor buscar por nombre del alumno y ver qué prácticas tiene programadas.
* **Control de Asistencia:** El instructor puede registrar si el alumno asistió ("Presente" o "Ausente") y añadir observaciones de la clase.
* **Historial de Prácticas:** Permite consultar todas las asistencias y observaciones pasadas de un alumno específico.

---

## 📂 Estructura del Proyecto

El proyecto está modularizado en los siguientes archivos Python:

* `menu_principal.py`: Es el archivo principal que se debe ejecutar. Contiene el menú raíz que redirige al portal de alumnos o al de instructores.
* `menu_clientes.py`: Contiene toda la lógica y menús correspondientes a las acciones de los alumnos.
* `Proyecto_instructor.py`: Contiene toda la lógica, menús, validaciones y manejo de errores correspondientes a los instructores.
* `guardar_datos.py`: Módulo utilitario que contiene las funciones `cargar_json` y `guardar_json`, encargadas de la lectura y escritura segura de datos.

### 💾 Almacenamiento de Datos
El sistema no requiere una base de datos externa; utiliza archivos locales en formato **.json** que se crean y actualizan dinámicamente:
* `clientes.json`: Almacena los datos de los alumnos registrados.
* `vehiculos.json`: Almacena el inventario de carros y motos, su estado de disponibilidad y qué instructor los tiene asignados.
* `citas.json`: Guarda el registro de las clases programadas (alumno, fecha, hora, vehículo e instructor).
* `asistencias.json`: Guarda el historial de asistencia y observaciones de las clases tomadas.

---

## 🚀 Cómo ejecutar el proyecto

**Requisitos:**
* Python 3.x instalado en el sistema.

**Instrucciones:**
1. Descarga o clona todos los archivos `.py` en una misma carpeta.
2. Abre una terminal o consola de comandos en esa carpeta.
3. Ejecuta el archivo principal con el siguiente comando:
   ```bash
   python menu_principal.py
