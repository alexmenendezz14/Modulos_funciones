
def sumar(i,j):
    return i+j

def sumar_default(i,j,k=15):
    return i+j+k


def sumar_variable(*args):
    total=0
    for i in args:
        total+=i
    return total

suma=sumar(4,5)
print(f"el total de la suma es {suma}")

sumar2=sumar_default(4,5)
print(f"el total de la suma es {sumar2}")

sumar3=sumar_variable(5,9,4,7)
print(f"la suma total de una funcion con argumentos variable es {sumar3}")

def factorial(n):
    if n==1:
        return n
    elif n<=0:
        print("no hay factorial para 0 o menor q 0")
    else:
        return n+factorial(n-1)

resultado_factorial=factorial(-3)
print(f"factorial es {resultado_factorial}")

