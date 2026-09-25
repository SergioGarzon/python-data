class Producto:
    
    def __init__(self, codigo, descripcion, precio, stock):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        
    def hay_stock(self):        
        return (self.stock > 0)
            
    def valor_stock(self):
        return (self.precio * self.stock)
        
    def __str__(self):
        return (
            "\n{ Código: " + str(self.codigo) + 
            ", descripción: " + str(self.descripcion) +
            ", precio: " + str(self.precio) + 
            ", stock: " + str(self.stock) +
            " }"
        )