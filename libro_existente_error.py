from tiendalibros.modelo.libro_error import LibroError

class LibroExistenteError(LibroError):
    def __init__(self, titulo, isbn):
        super().__init__()
        self.titulo = titulo
        self.isbn = isbn

    def __str__(self):
        return f"El libro con titulo {self.titulo} y isbn: {self.isbn} ya existe en el catálogo"