a = int(input('Digite o valor de (a):' ))
b = int(input('Digite o valor de (b):' ))
c = int(input('Digite o valor de (c):' ))
delta = (b**2)-4 *a *c
print('O valor de delta é {}'.format(delta))
x1 = (- b + (delta**(1/2)))/(2*a)
print('O valor de X1 é {}'.format(x1))
x2 = (- b - (delta**(1/2)))/(2*a)
print(') valor de x2 é {}'.format(x2))

