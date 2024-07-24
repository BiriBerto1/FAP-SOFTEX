print('Bem-vindo a calculadora de imc')
peso = float(input('Por favor, digite seu peso. '))
altura = float(input('Agora digite sua altura. '))

imc = peso/altura**2

print(f'seu imc é {imc:.3} e sua classificação é')

if imc <= 18.5:
    print('Baixo peso')
elif imc >= 18.6 and imc <= 24.9:
    print('Peso normal')
elif imc >= 25.0 and imc <= 29.9:
    print('Sobrepeso')
elif imc >= 30.0 and imc <= 34.9:
    print('Obesidade grau I')
elif imc >= 35.0 and imc <= 39.9:
    print('Obesidade grau II')
elif imc >= 40.0:
    print('Obesidade grau III')