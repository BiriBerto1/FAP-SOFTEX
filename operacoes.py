#Operações
def operacoes(num1, num2, ope):
    operadores_validos = '+-*/'
    while ope not in operadores_validos:
        print('Operador inválido. Digite um operador válido (+, -, *, /). ')
        ope = input()
    if ope == '+':
        return num1+num2
    elif ope == '-':
        return num1-num2
    elif ope == '*':
        return num1*num2
    elif ope == '/':
        return num1/num2
#Par/Impar
def impar(resultado):
    if resultado % 2 == 0:
        return 'Par'
    return 'Impar'
#Positivo/Negativo
def Positivo(resultado):
    if resultado < 0:
        return 'Negativo'
    return 'Positivo'
#Inteiro/Decimal
def inteiro(resultado):
    if type(resultado) == int:
        return 'Inteiro'
    return 'Decimal'
def main():
    num1 = int(input("Digite o primeiro número. "))
    num2 = int(input("Digite o segundo número. "))
    ope = input("Digite a operação (+, -, *, /). ")
    resultado = operacoes(num1, num2, ope)
    print(f"O resultado da operação é {resultado}, esse número é {impar(resultado)}, {Positivo(resultado)}, e {inteiro(resultado)}.")
main()