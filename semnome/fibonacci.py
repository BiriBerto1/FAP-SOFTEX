a = 0
b = 1
fibonacci = []
n = int(input('Digite o número que deseja conferir se está na sequencia de fibonacci. '))
while True:
    fibonacci.append(a)
    a,b = b, a+b
    if n in fibonacci:
        print('O número que você digitou está na sequencia de fibonacci.')
        break
    if fibonacci[-1] > n:
        print('O número não está na sequencia de Fibonacci')
        break
