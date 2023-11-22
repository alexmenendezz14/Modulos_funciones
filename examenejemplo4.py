from enum import Enum

class Color(Enum):
    AZUL = "azul"
    ROJO = "rojo"
    VERDE = "verde"
    # Agrega más colores según sea necesario

class Mueble:
    def __init__(self, color, precio):
        self.color = color
        self.precio = precio

class Mesa(Mueble):
    pass

class Silla(Mueble):
    pass

class Lampara(Mueble):
    pass


def imprimir_detalles_mueble(mueble):
    print(f"Color: {mueble.color.value}")
    print(f"Precio: ${mueble.precio}\n")

if __name__ == "__main__":
    try:
        # Crear dos sillas, una azul y otra roja, ambas con precio de 9.95
        silla_azul = Silla(color=Color.AZUL, precio=9.95)
        silla_roja = Silla(color=Color.ROJO, precio=9.95)

        # Imprimir detalles de las sillas
        print("Detalles de la silla azul:")
        imprimir_detalles_mueble(silla_azul)

        print("Detalles de la silla roja:")
        imprimir_detalles_mueble(silla_roja)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error inesperado: {e}")
