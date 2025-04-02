
# Sistema de Biblioteca con MongoDB 🍃

_Aplicación Flask para gestionar una biblioteca usando MongoDB como base de datos NoSQL. Ideal para manejar datos flexibles como historiales de préstamos, reservas y ejemplares._

## 🚀 Comenzando

### 📋 Pre-requisitos
- Python 3.8+
- MongoDB (local o Atlas)
- Pip

### 🔧 Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/biblioteca_mongodb.git
   cd biblioteca_mongodb
### Instala dependencias:
pip install -r requirements.txt
### Configura MongoDB en app.py:
app.config["MONGO_URI"] = "mongodb://localhost:27017/biblioteca"
### Ejecuta:
python app.py
###🗂️ Estructura

biblioteca_crud/
├── templates/
│   ├── base.html
│   ├── ejemplar.html   # CRUD ejemplares (MongoDB)
│   ├── historial.html  # Historial (MongoDB)
│   └── ...
├── app.py              # Lógica con PyMongo
└── requirements.txt    # Flask + PyMongo
###🛠️ Tecnologías
Flask: Framework web.

PyMongo: Driver para MongoDB.

MongoDB Atlas: Base de datos en la nube.

###📌 Ejemplo de Datos
// Colección "prestamos"
{
  "usuario_id": "001",
  "ejemplar_id": "101",
  "fecha": "2023-10-05",
  "estado": "activo"
}
