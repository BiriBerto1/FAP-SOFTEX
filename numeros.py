numeros = []
print('Digite quantos números você quiser, para encerrar digite -1')
numeros.append(int(input('Digite, digite algum número imediatamente. ')))

while numeros[-1] != -1:
    print('Digite novamente.')
    numeros.append(int(input()))


numeros.pop(-1)
print('A quantidade de valores lidos foi ', len(numeros))
print('Esses são os valores na ordem informada ', numeros)
numeros.reverse()
print('Esses são os valores na ordem inversa á que foram informados ', numeros)
soma =sum(numeros)
print('A soma dos números é ', soma)
media = soma / len(numeros)
print(f'A média dos números é {media:.1f}')
acimamed = []
for numero in numeros:
    if numero > media:
        acimamed.append(numero)
print(f'Foram digitados {len(acimamed)} números acima da média.')
menor7 = []
for numero in numeros:
    if numero < 7:
        menor7.append(numero)
print(f'Foram digitados {len(menor7)} números abaixo de 7.')
