num1 = int(input('Digite um número '))
num2 = int(input('Digite outro número '))
num3 = int(input('Digite o último número '))

if num1 <= num2 and num1 <= num3:
    menornum = num1
elif num2 <= num1 and num2 <= num3:
    menornum = num2
elif num3 <= num2 and num3 <= num3:
    menornum = num3

print(f'O menor número entre os três é {menornum}')