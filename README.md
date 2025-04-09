# 📚 Proyecto CRUD para Biblioteca con MongoDB y Flask

_Este proyecto es un sistema de gestión de biblioteca que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre las colecciones:._
**Usuarios, Libros, Ejemplares, Reservas, Préstamos e Historial,** utilizando:

- **Backend:** Python + Flask
- **Base de datos:** MongoDB
- **Frontend:** HTML + Bootstrap

## 🛠️ Tecnologías Utilizadas

| **tecnologia**  |**funcion**   |
| ------------ | ------------ |
| Python 3  |Lenguaje principal del backend   |
| Flask  | Framework web para rutas y lógica  |
| PyMongo  | Conexión con MongoDB  |
| MongoDB  |  Base de datos NoSQL |
| Bootstrap 5  | Diseño responsive de las plantillas  |
|Git  |Control de versiones   |


### 📋 Pre-requisitos
- Python 3.8+
- MongoDB
- Pip

### 🚀 Instalación y Configuración
**1. Clona el repositorio**

   ``git clone https://github.com/tu-usuario/Proyecto_BaseDeDatos_Mongodb.git  
cd Proyecto_BaseDeDatos_Mongodb  ``

**2. Crear un entorno virtual**

``python -m venv venv  
source venv/bin/activate  # Linux/macOS  
venv\Scripts\activate     # Windows  ``

**3. Instalar dependencias**

``pip install -r requirements.txt  ``

**4. Configurar MongoDB**

- Asegúrate de tener MongoDB instalado y el servicio en ejecución (en el cmd "mongod").
- La aplicación se conecta por defecto a mongodb://localhost:27017/biblioteca.

5. Ejecutar la aplicación

``python app.py  ``

### 📂 Estructura del Proyecto

```Proyecto_BaseDeDatos_Mongodb/  
├── app.py                # Backend (rutas y lógica)  
├── requirements.txt      # Dependencias  
├── templates/            # Plantillas HTML  
│   ├── base.html         # Plantilla común  
│   ├── usuario.html      # CRUD Usuarios  
│   ├── libro.html        # CRUD Libros  
│   ├── ejemplar.html     # CRUD Ejemplares  
│   ├── reserva.html      # CRUD Reservas  
│   ├── prestamo.html     # CRUD Préstamos  
│   └── historial.html    # CRUD Historial  
└── README.md             # Este archivo
```
### Diagrama de casos de uso
![diagrama](Diagrama_mejorado_crud.png)

### 🔍 Funcionalidades

**Operaciones CRUD para cada colección:**

- Crear registros (usuarios, libros, etc.).
- Leer/visualizar datos en tablas Bootstrap.
- Actualizar registros existentes.
- Eliminar registros.

**Interfaz intuitiva**

- Menú de navegación entre secciones.

- Formularios integrados en las tablas.

- Diseño responsive gracias a Bootstrap.

### 📬 Contacto
✉️ Email: gomezhiguitajuan@gmail.com

<p align="center"> ✨ **¡Gracias por usar este proyecto!** ✨ </p>
