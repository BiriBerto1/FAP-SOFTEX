#Realizando as operações
def operacoes():
    num1 = int(input('Digite um número. '))
    num2 = int(input('Digite outro número. '))
    ope = input('Digite qual operação você gostaria de fazer. ')
    if ope == '+':
        result = (num1+num2)
    elif ope == '-':
        result = (num1-num2)
    elif ope == '*' or ope == 'x':
        result = (num1*num2)
    elif ope == '/':
        result = (num1/num2)
    return result


#Par/Impar
def impar():
    if result % 2 == 0:
        parimp = ('par.')
    else:
        parimp = ('Impar')
    return parimp

#Positivo/Negativo
def naosei():
    if result < 0:
        maisoumenos = ('negativo')
    else:
        maisoumenos = ('positivo')
    return maisoumenos

#Inteiro/Decimal
def intdec():
    if type(result) == int:
        intdec = ('inteiro')
    elif type(result) == float:
        intdec = ('decimal')
    return intdec

def main():
    result = operacoes()
    impar()
    naosei()
    intdec()
    print(f"O resultado é {operacoes}, esse número é {impar}, {naosei} e {intdec}.")

main()