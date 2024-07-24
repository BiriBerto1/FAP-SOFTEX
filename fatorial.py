def calculo(numeros):
    numero = 1
    for n in range(numeros, 0, -1):
        numero *= n
    return numero

def main():
    print('Calculadora de fatorial.')
    numeros = int(input('Digite o número que você quer fazer o calculo.'))
    calculo(numeros)
    print(calculo(numeros))

main()