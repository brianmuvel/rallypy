
# def largo_numero(n):
#     contador = 0
#     if  isinstance(n, int):
#         if n < -1:
#             print('El valor tiene que ser positivo')
#         elif n >=0:
#             for i in str(n):
#                 contador += 1
#             print(f'El largo del número es de: {contador} caracteres')
#     elif isinstance(n, str):
#         print('El valor tiene que ser integral')
# largo_numero(1234)


def largo_numero(numero):
    contador=0
    if isinstance(numero, str):
        return None , 'El valor tiene que ser integral'
    elif numero < -1:
        return None, 'El valor tiene que ser positivo'
    else:
        for i in str(numero):
            contador += 1
        return 'El largo del numero es:', contador

largo_numero('100000000')
