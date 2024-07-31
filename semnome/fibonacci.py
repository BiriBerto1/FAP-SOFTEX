# a = 0
# b = 1
# fibonacci = []
# n = int(input('Digite o número que deseja conferir se está na sequencia de fibonacci. '))
# while True:
#     fibonacci.append(a)
#     a,b = b, a+b
#     if n in fibonacci:
#         print('O número que você digitou está na sequencia de fibonacci.')
#         print(fibonacci)
#         break
#     if fibonacci[-1] > n:
#         print('O número não está na sequencia de Fibonacci')
#         print(fibonacci)
#         break

def fibonelson(numero):
    if numero <= 1:
        return numero
    else:
        return fibonelson(numero-1) + fibonelson(numero-2)

def main():
    numero = int(input('Digite o numero e veja se ele está na sequencia de fibonacci: '))
    contador = 0
    while True:
        fibonation = fibonelson(contador)
        if fibonation >= numero:
            print(f'O número {numero} está na sequência de Fibonacci.')
            break
        elif fibonation > numero:
            print(f'O número {numero} não está na sequência de Fibonacci.')
            break
        print(fibonation)
        contador += 1

if __name__ == "__main__":
    main()
