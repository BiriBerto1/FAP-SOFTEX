def operacoes(num1, num2, operacao):
  """
  Função que realiza a operação matemática especificada.

  Argumentos:
    num1: O primeiro número.
    num2: O segundo número.
    operacao: A operação matemática (+, -, *, /).

  Retorna:
    O resultado da operação matemática.
  """
  if operacao == "+":
    return num1 + num2
  elif operacao == "-":
    return num1 - num2
  elif operacao == "*":
    return num1 * num2
  elif operacao == "/":
    return num1 / num2
  else:
    raise ValueError("Operação inválida.")

def par_impar(resultado):
  """
  Função que verifica se o resultado é par ou ímpar.

  Argumento:
    resultado: O valor a ser verificado.

  Retorna:
    "Par" se o resultado for par, "Ímpar" caso contrário.
  """
  if resultado % 2 == 0:
    return "Par"
  else:
    return "Ímpar"

def positivo_negativo(resultado):
  """
  Função que verifica se o resultado é positivo ou negativo.

  Argumento:
    resultado: O valor a ser verificado.

  Retorna:
    "Positivo" se o resultado for positivo, "Negativo" caso contrário.
  """
  if resultado >= 0:
    return "Positivo"
  else:
    return "Negativo"

def inteiro_decimal(resultado):
  """
  Função que verifica se o resultado é um número inteiro ou decimal.

  Argumento:
    resultado: O valor a ser verificado.

  Retorna:
    "Inteiro" se o resultado for um número inteiro, "Decimal" caso contrário.
  """
  if isinstance(resultado, int):
    return "Inteiro"
  else:
    return "Decimal"

def main():
  """
  Função principal que solicita os dados, realiza as operações e apresenta os resultados.
  """
  try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    resultado = operacoes(num1, num2, operacao)

    print(f"O resultado da operação é {resultado}.")
    print(f"O número é {par_impar(resultado)}.")
    print(f"O número é {positivo_negativo(resultado)}.")
    print(f"O número é {inteiro_decimal(resultado)}.")

  except ValueError as e:
    print(f"Erro: {e}")

if __name__ == "__main__":
  main()
