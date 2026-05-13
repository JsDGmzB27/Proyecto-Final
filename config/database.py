from pymongo import MongoClient

client = MongoClient("mongodb+srv://manolo_Buritica:miguelito890@usuarioscasino.rxkscni.mongodb.net/?appName=usuariosCasino")

db = client["usuarios_casino"]
coleccion = db["usuarios"]
    


def agregar_usuario(usuario, contraseña, correo, presupuesto=0.0):
    nuevo = {
        "usuario": usuario,
        "contraseña": contraseña,
        "correo": correo,
        "presupuesto": presupuesto,
        "dinero_perdido": 0.0,
        "dinero_ganado": 0.0
    }
    resultado = coleccion.insert_one(nuevo)
    print(f"Usuario creado con ID: {resultado.inserted_id}")

# Uso:
agregar_usuario("maria123", "clave456", "maria@gmail.com", 1000.0)