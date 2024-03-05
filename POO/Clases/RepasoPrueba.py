# atributos:
# titulo: str
# precio: int
# cantidad: int
class Publicacion:

    # constructor: None -> Publicacion
    # crea un objeto de tipo Pulicacion
    # ej: publicacion = Publicacion()
    def __init__(self):
        self.titulo = ''
        self.precio = 0
        self.cantidad = 0

    # setTitulo: str -> None
    # Establece un titulo para la publicacion
    # ej: publicacion.setTitulo('Mi Lucha') establece el titulo en 'Mi Lucha'
    def setTitulo(self, titulo):
        self.titulo = titulo
    
    # setPrecio: int -> None
    # Establece el precio de una publicacion
    # ej: publicacion.setPrecio(1000) establece el precio en 1000
    def setPrecio(self, precio):
        self.precio = precio
    
    # setTitulo: str -> None
    # Establece el stock del libro en inventario
    # ej: publicacion.setCantidad(10000) establece el stock en 10000
    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    # getTitulo: None -> str
    # Obtiene el titulo de la publicacion
    # ej: publicacion.getTitulo() obtiene el titulo 'Mi Lucha'
    def getTitulo(self):
        return self.titulo
    
    # getPrecio: None -> int
    # Obtiene el precio de la publicacion
    # ej: publicacion.getPrecio() obtiene el precio 1000
    def getPrecio(self):
        return self.precio
    
    # getCantidad: None -> int
    # Obtiene el stock en el inventario de la publicacion
    # ej: publicacion.getCantidad() obtiene el stock en inventario de 'Mi Lucha'
    def getCantidad(self):
        return self.cantidad

# atributos:
# hereda de Publicacion
# autor: str
# isbn: int
class Libro(Publicacion):

    # constructor: None -> Libro
    # crea un objeto de tipo Libro
    # ej: libro = Libro()
    def __init__(self):
        Publicacion.__init__(self)
        self.autor = ''
        self.isbn = 0

    # setAutor: str -> None
    # Establece el autor de un libro
    # ej: setAutor('Diego') establece el autor del libro en 'Diego'
    def setAutor(self, autor):
        self.autor = autor
    
    # setAutor: int -> None
    # Establece el isnb de un libro
    # ej: setIsnb(123) establece el ibn del libro en 123
    def setIsbn(self, isnb):
        self.isbn = isnb

    # getAutor: None -> str
    # Obtiene el autor del libro
    # ej: libro.getAutor() obtiene el autor del libro
    def getAutor(self):
        return self.autor
    
    # getIsnb: None -> int
    # Obtiene el isnb del libro
    # ej: libro.getIsnb() obtiene el isnb del libro
    def getIsbn(self):
        return self.isbn

# atributos:
# hereda de Publicacion
# numeroEdicion: int
class Revista(Publicacion):

    # constructor: None -> Revista
    # crea un objeto de tipo Revista
    # ej: revista = Revista()
    def __init__(self):
        Publicacion.__init__(self)
        self.numeroEdicion = 0

    # setNumeroEdicion: int -> None
    # Establece el numero de la edicion de una revista
    # ej: setNumeroEdicion(1) establece el numerod e la edicion de la revista en 1
    def setNumeroEdicion(self, numero_edicion):
        self.numeroEdicion = numero_edicion

    # getNumeroEdicion: None -> int
    # Obtiene el numero de edicion de la revista
    # ej: revista.getNumeroEdicion() obtiene el numero de edicion de la revista
    def getNumeroEdicion(self):
        return self.numeroEdicion

# atributos:
# publicaciones: lista
class Inventario:

    # constructor: None -> Inventario
    # crea un objeto de tipo Inventario
    # ej: inv = Inventario()
    def __init__(self):
        self.publicaciones = []
    
    # agregarPublicaciones: Revista o Libro -> None
    # agrega una revista o un libro al inventario
    # ej: inv.agregarPublicacion(libro) agrega libro al inventario
    def agregarPublicacion(self, publicacion):
        self.publicaciones.append(publicacion)
    
    # buscarPublicacion: str -> Libro o Revista
    # busca un libro o una revista en el inventario, del caso contrario devuelve None
    # ej: inv.buscarPublicacion('El Manifiesto') devuelve el objeto tipo Libro con el titulo 'El Manifiesto'
    def buscarPublicacion(self, titulo):
        for publi in self.publicaciones:
            if publi.titulo == titulo:
                return publi
            else:
                return None

    # listarPublicacion: None -> None
    # Muestra todo el inventario de publicaciones, con titulo, precio y cantidad
    # inv.listarPublicacion() imprime en pantalla el inventario
    def listarPublicacion(self):
        for publi in self.publicaciones:
            print(f'Titulo: {publi.titulo} | Precio: {publi.precio} | Cantidad: {publi.cantidad}\n')

            

### USANDO ESTA CHUCHA ####

# Iniciando los libros y revistas y todas esas mrdas
libro1 = Libro()
libro2 = Libro()
revista1 = Revista()

#setiando el precio y todas esas mierdas
libro1.setTitulo('Condorito')
libro1.setPrecio(2500)
libro1.setCantidad(20)

libro2.setTitulo('Godzilla')
libro2.setPrecio(20000)
libro2.setCantidad(2)

revista1.setTitulo('Forbess')
revista1.setPrecio(1000)
revista1.setCantidad(100)

#iniciando el foking inventario
inventario = Inventario()
inventario.agregarPublicacion(libro1)
inventario.agregarPublicacion(libro2)
inventario.agregarPublicacion(revista1)

inventario.listarPublicacion()