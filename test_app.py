import mysql.connector
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tu_password"
    )
    print("¡Conexión exitosa!")
except Exception as e:
    print("Error:", e)