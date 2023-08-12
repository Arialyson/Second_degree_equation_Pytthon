#variaveis
a = int(input('Digite o valor de (a):' ))
b = int(input('Digite o valor de (b):' ))
c = int(input('Digite o valor de (c):' ))

#valor do descriminate
delta = (b**2)-4 *a *c
print('O valor de delta é {}'.format(delta))

#valor da primeira raíz, caso tenha*
x1 = (- b + (delta**(1/2)))/(2*a)
print('O valor de X1 é {}'.format(x1))

#valor da segunda raíz, caso tenha*
x2 = (- b - (delta**(1/2)))/(2*a)
print(') valor de x2 é {}'.format(x2))

#condições
if delta > 0:
    print('discriminante positivo (Δ > 0): duas soluções para a equação; ')
    print('O valor de X1 é {}'.format(x1))
    print(') valor de x2 é {}'.format(x2))
elif delta == 0:
    print('discriminante igual a zero (Δ = 0): as soluções da equação são repetidas;')
    print(') valor de X1 e x2 tem valores iguais a: {}'.format(x2))
elif delta < 0:
    print('discriminante negativo (Δ < 0): não admite solução real.')