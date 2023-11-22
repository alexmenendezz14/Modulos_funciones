from datetime import datetime

def calcular_descuento(subtotal, dia_del_mes):
    if dia_del_mes < 15:
        return subtotal * 0.05
    else:
        return 0

def calcular_total(unidades, precio):
    try:
        unidades = int(unidades)
        precio = float(precio)
    except ValueError:
        print("Error: Debes introducir valores numéricos válidos.")
        return None

    subtotal = unidades * precio
    dia_del_mes = datetime.now().day
    descuento = calcular_descuento(subtotal, dia_del_mes)
    total = subtotal - descuento

    print(f"Subtotal: ${subtotal}")
    print(f"Descuento aplicado: ${descuento}")
    print(f"Total a pagar: ${total}")

if __name__ == "__main__":
    while True:
        unidades = input("Introduce la cantidad de unidades: ")
        precio = input("Introduce el precio por unidad: ")

        calcular_total(unidades, precio)

        decision = input("¿Quieres repetir el programa? (s/n): ")
        if decision.lower() != 's':
            break
