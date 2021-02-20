
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


def largo_numero(n):
    contador=0
    if isinstance(n, str):
        print('El valor tiene que ser integral')
    elif n < -1:
        print('El valor tiene que ser positivo')  
    else:
        for i in str(n):
            contador += 1
        print(f'El largo del número es de: {contador}')

largo_numero('asd')
