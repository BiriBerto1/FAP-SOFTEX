print('Bem-Vindo a calculadora de descontos')
valor = float(input('Digite o valor do produto '))
descon = int(input('Digite a porcengatem de desconto recebida '))
valordescon = (descon*valor)/100

print(f'O preço final do produto com desconto é R${valor-valordescon}')