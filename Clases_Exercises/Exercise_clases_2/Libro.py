class Libro:
    
    # título, autor, cantidad de páginas y estado de préstamo
    def __init__(self, titulo, autor, cant_paginas, estado_prestamo):
        self.titulo = titulo
        self.autor = autor
        self.cant_paginas = cant_paginas
        self.estado_prestamo = estado_prestamo
        
    def prestar(self):
        if self.estado_prestamo != "prestado":
            self.estado_prestamo = "prestado"
   
    def devolver(self):
        if self.estado_prestamo != "devuelto":
            self.estado_prestamo = "devuelto"
            
    def __str__(self):
        return (
            "{ Titulo: " + str(self.titulo) + 
            ", autor: " + str(self.autor) + 
            ", cantidad de paginas: " + str(self.cant_paginas) + 
            ", estado de prestamo: " + str(self.estado_prestamo) +
            " }"
        )