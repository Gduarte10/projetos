sexo = input('Digite seu sexo m ou f:')
altura = float(input('Digite sua altura:'))

pesoIdeal =0.0
if (sexo.upper () == 'M'): 
    pesoIdeal = round((72.7*altura)-58,2)
elif (sexo.upper () == 'F'):
    pesoIdeal = round((62.1*altura)-44.7,2)
else:
    print('O sexo informado deve ser M para masculino ou F para feminino.')

if(pesoIdeal>  0):
    print('O sexo informado foi:', sexo.upper())
    print('Seu peso ideal é:', pesoIdeal)

