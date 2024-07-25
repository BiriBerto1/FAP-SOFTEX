def cadastrar_pessoa():
    nome = input('Digite o nome. ')
    idade = int(input('Digite a idade. '))
    cpf = str(input('Digite o cpf. '))
    pessoa = {
        'Nome': nome,
        'Idade': idade,
        'CPF': cpf
    }
    return pessoa

def main():
    lista_pessoas = []

    while True:
        seila = int(input('Para cadastrar uma pessoa digite 1. \nDigite 0 para terminar o cadastro.'))

        if seila == 1:
            pessoas = cadastrar_pessoa()
            lista_pessoas.append(pessoas)
            print(lista_pessoas)
        if seila == 0:
            break

    for pessoa in lista_pessoas:
        if lista_pessoas["Idade"] < 18:
            lista_pessoas.pop(pessoa)
        else:
            print(lista_pessoas)

main()