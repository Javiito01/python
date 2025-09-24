lista_colores = ["rojo", "verde", "azul", "amarillo"]
print("colores: ",lista_colores)
borrar = input("cual quieres eliminar: ")
if borrar in lista_colores:
    lista_colores.remove(borrar)
print("lista actualizada: ",lista_colores)
