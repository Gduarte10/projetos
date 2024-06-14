import math

numero = int(input('Digite um numero: '))


if numero >= 0:
    raiz = math.sqrt(numero)
    print(raiz)
else:
    quadrado = numero**2
    print(quadrado)
    