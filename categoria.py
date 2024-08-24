class Categoria:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def __str__(self):
        return f"Categoría: {self.nombre}, Descripción: {self.descripcion}, Productos: {[p.nombre for p in self.productos]}"