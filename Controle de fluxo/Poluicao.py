poluicao = float(input('Qual o indice de poluição?'))

if poluicao >= 0.03 and poluicao <= 0.25:
    print('Intimar industrias do 1º grupo.')
elif poluicao >= 0.4 and poluicao < 0.5 :
    print('Intimar industrias do 1º e 2º grupo.')
elif poluicao >= 0.5:
    print('Intimar industrias de todos os grupos.')