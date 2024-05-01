from carro_compra import *
from libro import *
from libro_error import *
from libro_agotado_error import *



class TiendaLibros:
    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompras()

    def adicionar_libro_a_catalogo(self, isbn, titulo, precio, existencias):
        if isbn in self.catalogo:
            raise LibroExistenteError(titulo, isbn)
        libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = libro
        return libro

    def agregar_libro_a_carrito(self, isbn, cantidad):
        if isbn not in self.catalogo:
            raise LibroError(f"No se encontró el libro con ISBN {isbn}")
        libro = self.catalogo[isbn]
        if libro.existencias == 0:
            raise LibroAgotadoError(libro.titulo, libro.isbn)
        if cantidad > libro.existencias:
            raise ExistenciasInsuficientesError(libro.titulo, libro.isbn, cantidad, libro.existencias)
        self.carrito.agregar_item(libro, cantidad)

    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)



