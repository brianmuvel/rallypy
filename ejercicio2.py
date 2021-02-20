
def lista_multiplos(numeroInicial, numeroVeces):
    if numeroInicial <= -1 or numeroVeces <= -1:
        return None, 'El numero tiene que ser positivo'
    lista=[]
    for numero in range(1, numeroVeces + 1):
        operacion = numeroInicial * numero
        lista.append(operacion)
    print(lista)

lista_multiplos(2,-4)