import random
numero_aleatorio = random.randint(1,100)

print('------- JOGO DE ADVINHAÇÃO-------')
print('Advinhe o número escolhido entre um a cem.')

tentativa = int(input())
guarda_numeros = []

while tentativa != numero_aleatorio:
    if tentativa > numero_aleatorio:
        print('O número é menor.')
        print('Tente novamente.')
        tentativa = int(input())
    elif tentativa < numero_aleatorio:
        print('O número é maior.')
        print('Tente novamente.')
        tentativa = int(input())
    guarda_numeros.append(tentativa)

print('Parabéns você acertou!')
print(f'O número escolhido foi {tentativa}')
print(f'Os números que você tentou foram {guarda_numeros}')