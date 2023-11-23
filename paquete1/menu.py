from paquete1.cliente import Cliente

cliente1 = Cliente("Juan","tupu@gmail.com",22,"efectivo")
# cliente2 = Cliente("Anatonella","antus@yahoo.com",32,"targeta de credito")

print(cliente1)
print(cliente1.compra("notebook","walmart"))
print(cliente1.alternativa_de_pago())

print(cliente1.confirmacion_de_pago())
mensaje_al_usuario = input("su mail es correcto? si/no: ")

if mensaje_al_usuario == "si":
    print("se han enviado los detalles de su compra")
elif mensaje_al_usuario == "no":
    nuevo_mail = input("ingrese el mail correcto: ")
    cliente1.email = nuevo_mail
    print(f"su nuevo mail {cliente1.email} ha sido guardado")

    