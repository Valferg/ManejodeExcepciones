class ItemCompra:
    
    def __init__(self, libro, cantidad):
        self.libro = libro
        self.cantidad: libro = cantidad 

    def cantidad_subtotal(self):
        return self.libro.precio * self.cantidad
    
    





