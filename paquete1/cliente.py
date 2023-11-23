from datetime import datetime 


class Cliente():
    def __init__(self,cliente,email,edad,forma_de_pago):
        self.cliente = cliente
        self.email = email
        self.edad = edad
        self.pago = forma_de_pago
        
    def __str__(self):
        cliente_creado = f"se ha creado el cliente {self.cliente}"
        return cliente_creado
    
    def compra(self,objeto,tienda):
        dt = datetime.now()
        compra_cliente = f"el cliente {self.cliente} compró {objeto} en {tienda}"
        momento_compra = dt.strftime("%A %d %B %Y %I:%M")
        resultado  = f"{compra_cliente}  el  {momento_compra}"
        return resultado
    
    def alternativa_de_pago(self):
        if self.pago == "efectivo":
            lo_que_paso = "se ha aplicado un descuento de 10% en la compra de su producto"
            
        elif self.pago == "targeta de credito":
            lo_que_paso = "tiene la opcion de 3 o 6 cuotas"
            
        return lo_que_paso
    
    def confirmacion_de_pago(self):
        confirmacion = f"su compra ha sido confirmada, se mandara la factura con los detalles al siguente mail: {self.email}" 
        return confirmacion
    
    

        