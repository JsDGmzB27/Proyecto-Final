from pymongo import MongoClient 

client = MongoClient("mongodb+srv://manolo_Buritica:miguelito890@usuarioscasino.rxkscni.mongodb.net/?appName=usuariosCasino")

db = client["usuarios_casino"]
coleccion = db["usuarios"]
    

#conectar con la interfaz grafica
def agregar_usuario(usuario, contraseña, correo):
    nuevo = {
        "usuario": usuario,
        "contraseña": contraseña,
        "correo": correo,
        "presupuesto": 0.0,
        "dinero_perdido": 0.0,
        "dinero_ganado": 0.0,
    }
    try:
        coleccion.insert_one(nuevo)
    except Exception as e:
        raise ValueError("Error al agregar usuario")

def validar_usuario(nombre_usuario, contraseña):
    usuario = coleccion.find_one({"usuario": nombre_usuario, "contraseña": contraseña})
    if usuario:
        return usuario
    else:
        raise ValueError("Usuario o contraseña incorrectos")

def buscar_usuario(nombre_usuario):
    usuario = coleccion.find_one({"usuario": nombre_usuario})
    if usuario:
        return usuario
    else:
        return "Usuario no encontrado"
    
def editar_usuario(nombre_usuario, nuevos_datos: dict): #recibe diccionario de los campos que se quieren editar
    resultado = coleccion.update_one(
        {"usuario": nombre_usuario},
        {"$set": nuevos_datos}
    )
    if resultado.modified_count > 0:
        print("Usuario actualizado")
    else:
        print("No se encontró o no hubo cambios")


#ganancias que sea la resta de lo ganado con lo perdido 
def actualizar_dinero(nombre_usuario, ganado=0.0, perdido=0.0):
    coleccion.update_one(
        {"usuario": nombre_usuario},
        {"$inc": {  #suma al valor actual
            "presupuesto": (perdido * -1), #En caso de que pierda se una apuesta se resta al presupuesto pa apostar
            "dinero_ganado": ganado,
            "dinero_perdido": perdido
        }}
    )

def actualizar_presupuesto(nombre_usuario, presupuesto=0.0):
    coleccion.update_one(
        {"usuario": nombre_usuario},
        {"$set": {"presupuesto": presupuesto}}
    )


def eliminar_usuario(nombre_usuario):
    resultado = coleccion.delete_one({"usuario": nombre_usuario})
    if resultado.deleted_count > 0:
        print("Usuario eliminado")
    else:
        print("Usuario no encontrado")