
def largo_numero(n):
    contador = 0
    if  isinstance(n, int):
        if n < -1:
            print('El valor tiene que ser positivo')
        elif n >=0:
            for i in str(n):
                contador += 1
            print(contador)
    elif isinstance(n, str):
        print('El valor tiene que ser integral')
largo_numero(1234)
