print('Calculadora de Juros Simples')
#Valor Inicial
valorI = float(input('Digite o valor inicial '))
#Taxa de Juros
taxJu = float(input('Digite a taxa de juros '))
#Tempo para pagamento em anos
TempP = int(input('Digite o tempo para pagamento em anos '))

print('O valor final é R$',valorI*taxJu*TempP)