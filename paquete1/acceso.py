# esto es la pre-entrega n1
# simula un login en el que se registra un usuario y contraseña, se almacena en un diccionario 
# tiene un sistema de chances y te devuelve el nombre de usario y contraseña, tambien se pueden agregar hasta que le digas "no"

perfil_de_usuario = {}

def registro():

    usuario = input("ingrese su usuario: ")
    contraseña = input("ingrese su contraseña: ")
    perfil_de_usuario[usuario] = contraseña
    mensaje_registro = "registracion realizada con éxito."

    return mensaje_registro

def ingreso():

    chance = 4
    while chance <= 5:
        print("") #espacio
        ingreso_usuario = input("ingrese la su usuario: ")
        ingreso_contraseña = input("ingrese la su contraseña: ")
        condicion_acceso = ingreso_usuario in perfil_de_usuario and perfil_de_usuario[ingreso_usuario] == ingreso_contraseña

        if condicion_acceso == True:
            print(f"la contraseña coincide, bienvenido, {ingreso_usuario}.")
            print("accediendo al sistema...")
            break
        else:
            print("no coincide, vuelva a intentar")
            print("intentos restantes",chance)
            print("") #espacio
            chance -= 1
            if chance == -1:
                print("Has intentado demasiadas veces")
                break
    return "" #espacio

def mostrar_datos():
    for usuario, contraseña in perfil_de_usuario.items():
        print(f"Usuario:{usuario}")
        print(f"Contraseña:{contraseña}")
    return "" #espacio


print(registro())
print(ingreso())
print(mostrar_datos())



while True:
    continuar = input("Registrar otro usuario (si/no)?")

    if continuar == "si":
        print(registro())
        print(ingreso())
        print(mostrar_datos())
    elif continuar == "no":
        print("saliendo del sistema...")
        break
    else:
        print("la opcion no es valida")