
def factorial(x):
    if x == 0 or x==1:
        resultado = 1
    elif x > 1:
        resultado = x * factorial(x-1)
    return resultado

factorial(3)
