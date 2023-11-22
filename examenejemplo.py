def suma_cinco_numeros():
    numeros = []

    try:
        for _ in range(5):
            entrada = input(f"Introduce el número {_ + 1}: ")
            numero = float(entrada)
            numeros.append(numero)

    except ValueError:
        print("Error: Debes introducir un número válido.")
        return None

    suma = sum(numeros)
    print(f"La suma de los 5 números introducidos es: {suma}")

if __name__ == "__main__":
    while True:
        suma_cinco_numeros()

        decision = input("¿Quieres repetir el programa? (s/n): ")
        if decision.lower() != 's':
            break

