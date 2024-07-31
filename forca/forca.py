import random

def ler_palavras_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        palavras = [linha.strip() for linha in arquivo if linha.strip()]
    return palavras

def aplicar_dificuldade(nivel):
    arquivos = {1: 'forca/palavras/facil.txt', 2: 'forca/palavras/medio.txt', 3: 'forca/palavras/dificil.txt', 4: 'forca/palavras/kkk.txt'}
    caminho = arquivos[nivel]
    palavras = ler_palavras_arquivo(caminho)
    tentativas = {1: 8, 2: 6, 3: 4, 4: 2}[nivel]
    return palavras, tentativas

def dificuldade():
    print('Selecione o nível de dificuldade:\n1. Fácil\n2. Médio\n3. Difícil')
    try:
        nivel = int(input("Escolha a dificuldade. "))
        if nivel in [1, 2, 3]:
            return nivel
        else:
            print("Por favor, selecione 1, 2 ou 3.")
            return 4
    except ValueError:
        print("Por favor, insira um número válido.")
        return dificuldade()

def ler_score(nome_arquivo):
    pontuacoes = {}
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(':')
                if len(partes) == 4:
                    jogador, vitorias, derrotas, pontuacao = partes
                    pontuacoes[jogador] = {
                        'vitorias': int(vitorias),
                        'derrotas': int(derrotas),
                        'pontuacao': int(pontuacao)
                    }
    except FileNotFoundError:
        pass
    return pontuacoes

def atualizar_score(nome_arquivo, jogador, nivel, vitoria=True):
    pontuacoes = ler_score(nome_arquivo)
    if jogador not in pontuacoes:
        pontuacoes[jogador] = {'vitorias': 0, 'derrotas': 0, 'pontuacao': 0}

    pontos_dificuldade = {1: 1, 2: 5, 3: 10, 4: 50}
    pontos = pontos_dificuldade.get(nivel, 0)

    if vitoria:
        pontuacoes[jogador]['vitorias'] += 1
        pontuacoes[jogador]['pontuacao'] += pontos
    else:
        pontuacoes[jogador]['derrotas'] += 1
    
    with open(nome_arquivo, 'w') as arquivo:
        for jogador, dados in pontuacoes.items():
            arquivo.write(f"{jogador}:{dados['vitorias']}:{dados['derrotas']}:{dados['pontuacao']}\n")

def exibir_pontuacoes(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            print("\nPontuações:")
            for linha in arquivo:
                jogador, vitorias, derrotas, pontuacao = linha.strip().split(':')
                print(f"Jogador: {jogador} | Vitórias: {vitorias} | Derrotas: {derrotas} | Pontuação: {pontuacao}")
    except FileNotFoundError:
        print("Nenhuma pontuação registrada ainda.")

def main():
    nome_arquivo_score = 'forca/pontuação/score.txt'
    jogador = input("Digite seu nome: ").strip()

    nivel = dificuldade()
    palavras, numero_tentativas = aplicar_dificuldade(nivel)
    palavra_secreta = random.choice(palavras)
    letras_usadas = []
    palavra_exibida = "_" * len(palavra_secreta)

    while numero_tentativas > 0:
        print("\n" + palavra_exibida)
        print(f'Letras já utilizadas: {letras_usadas}')
        
        tentativa = input('Digite uma letra ou tente adivinhar a palavra inteira: ').lower()

        if len(tentativa) > 1:
            if tentativa == palavra_secreta:
                print(f'Parabéns! Você acertou a palavra: {palavra_secreta}')
                atualizar_score(nome_arquivo_score, jogador, nivel, vitoria=True)
                break
            else:
                print('Palavra errada. Você perdeu!')
                atualizar_score(nome_arquivo_score, jogador, nivel, vitoria=False)
                break

        if tentativa in letras_usadas:
            print('Você já digitou essa letra!')
            continue

        letras_usadas.append(tentativa)

        if tentativa in palavra_secreta:
            palavra_exibida = "".join([tentativa if palavra_secreta[i] == tentativa else palavra_exibida[i] for i in range(len(palavra_secreta))])
            
            if palavra_exibida == palavra_secreta:
                print(f'Parabéns, você acertou a palavra: {palavra_secreta}')
                atualizar_score(nome_arquivo_score, jogador, nivel, vitoria=True)
                break
        else:
            numero_tentativas -= 1
            print(f"Você errou, restam {numero_tentativas} tentativas.")
    
    if numero_tentativas == 0:
        print('Você perdeu! A palavra secreta era:', palavra_secreta)
        atualizar_score(nome_arquivo_score, jogador, nivel, vitoria=False)

def menu_principal():
    while True:
        print('1. Jogar')
        print('2. Ver Pontuações')
        print('3. Sair')
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            main()
        elif escolha == '2':
            exibir_pontuacoes('forca/pontuação/score.txt')
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_principal()
