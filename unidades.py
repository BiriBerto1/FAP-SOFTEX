def novecentos(numero):
    if numero > 999:
        while numero > 999:
            print("O número é maior que 999. Escolha outro número")
            numero = input()
def centena(numero):
    return numero // 100
def dezena(numero):
    return (numero % 100) // 10
def unidade(numero):
    return numero % 10
def main():
    numero = int(input("Digite um número entre 1 e 999: "))
    while numero > 999:
        print('O número digitado é maior que 999, escolha outro número.')
        numero = int(input())
    if numero < 10:
        print(f"O número tem {unidade(numero)} unidades.")
    elif numero < 100:
        print(f'O número tem {dezena(numero)} dezenas e {unidade(numero)} unidades.')
    else:
        print(f"O número tem {centena(numero)} centenas, {dezena(numero)} dezenas e {unidade(numero)} unidades.")
main()