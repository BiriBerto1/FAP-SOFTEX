#salario por hora
salarioPH = 10
#hora extra
horaEx = 20
#hora trabalhada
horaTrab = int(input('Digite quantas horas você trabalhou '))

if horaTrab <= 50:
    salarioTot = salarioPH*horaTrab
    print(f'Você receberá {salarioTot} de salário')
elif horaTrab >= 50:
    horaTrab -= 50
    salarioTot = (horaEx*horaTrab)+500
    print(f'Você receberá {salarioTot}, com as horas extras')