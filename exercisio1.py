# Essa parte e para conseguir achar o pesso ideal
try:
 sexo = input('Digite seu sexo m ou f:')
 altura = float(input('Digite sua altura:'))
except Exception as e:
    print('houve algum erro', e)
else:
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

    # Essa parte serva para informar o IMC 

    peso = float(input('Digite o seu peso:'))
    imc = round((peso/altura**2),1)

    if imc < 18.5:
        print(' você esta abaixo do pesso ')
    elif imc < 25:
        print('você esta com o seu peso normal')
    elif imc < 30:
        print('você esta com sobrepeso')
    elif imc < 35:
        print('você esta com obesidade grau 1')
    elif imc < 40:
        print('você esta com obseidade grau 2')
    elif imc >= 40:
        print('você esta com obseidade grau 3')
finally:
    print('fim do programa')
