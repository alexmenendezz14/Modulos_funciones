def obtener_numeros_pares(inicial, final):
    try:
        inicial = int(inicial)
        final = int(final)
    except ValueError:
        print("Error: Debes introducir números enteros válidos.")
        return None

    numeros_pares = [num for num in range(inicial, final + 1) if num % 2 == 0]
    return numeros_pares

if __name__ == "__main__":
    while True:
        inicial = input("Introduce el número inicial: ")
        final = input("Introduce el número final: ")

        numeros_pares = obtener_numeros_pares(inicial, final)

        if numeros_pares:
            print(f"Lista de números pares entre {inicial} y {final}: {numeros_pares}")
        else:
            print("No se pudo generar la lista debido a errores en la entrada.")

        decision = input("¿Quieres repetir el programa? (s/n): ")
        if decision.lower() != 's':
            break

