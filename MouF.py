s=input('escreva aqui M ou F para seu sexo: ').upper()
while s!='M' and s!='F':
    print('voce digitou errado')
    s = input('escreva APENAS M ou F para seu sexo: ').upper()
print ('seu sexo é {}'.format(s))