## Clase para productos de una tienda
class producto (object):
    '''
    clase para definir los productos de una tienda
    '''
    expirado = False
    def __init__(self,precio,codigo,stock):
        self.__precio = precio
        self.codigo = codigo
        self.stock = stock
        self.importado = codigo%2 == 1

    def vender (self,dinero):
        if dinero > self.precio:
            if self.stock > 0:
                s_cambio = dinero - self.precio
                print('su cambio es: ', s_cambio)
                self.stock -= 1
                return s_cambio
            else:
                print('Producto sin stock')
                return dinero
        else:
            print ('No es suficiente para comprar el producto')
            return dinero

    def darPrecio (self):
        return self.__precio

    def cambiarPrecio(self,precioNuevo):
        self.__precio = precioNuevo

    def darExpirado(self):
        return self.expirado

class lacteos(producto):
    Nevera = True
    temp = 15
    def sacarDeNevera (self):
        if self.stock > 0:
            self.Nevera = False
            self.temp += 1
        else:
            print('Producto no encontrado')

    def expiro (self):
        if self.temp > 20:
            self.expirado = True
        if self.expirado:
            print('El producto ha expirado')

    def incrTemp (self):
        self.temp += 1

####################################
### Codigo principal de la tienda###
####################################

## Crear la lista de productos
# Se crean los productos de la tienda
papas = producto(1000,10,100)
pasta = producto(1500,11,100)

leche = lacteos(1500,12,50)

# TODO: explrorar las disntintas funciones que se tienen en una clase