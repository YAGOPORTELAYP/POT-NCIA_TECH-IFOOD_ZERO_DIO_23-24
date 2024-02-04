vitorias = int(input("Digite o número de vitórias: "))
derrotas = int(input("Digite o número de derrotas: "))


def calcular_nivel(vitorias, derrotas):
  saldo = vitorias - derrotas

  if saldo < 10:
    nivel = "Ferro"
  elif 10 <= saldo < 20:
    nivel = "Bronze"
  elif 20 <= saldo < 50:
    nivel = "Prata"
  elif 50 <= saldo < 80:
    nivel = "Ouro"
  elif 81 <= saldo < 90:
    nivel = "Diamante"
  elif 91 <= saldo < 100:
    nivel = "Lendário"
  else:
    nivel = "Imortal"

  return saldo,nivel

saldo,nivel = calcular_nivel(vitorias, derrotas)

print(f"O Herói tem saldo de {saldo} está no nível de {nivel}!!!")
