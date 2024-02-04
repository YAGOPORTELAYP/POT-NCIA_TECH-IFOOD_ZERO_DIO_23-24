player_game = input("Digite o nome do herói: ")
xp = int(input("Digite a quantidade de experiência do herói: "))

if xp < 1000:
    level = "Ferro"
elif 1001 <= xp <= 2000:
    level = "Bronze"
elif 2001 <= xp <= 5000:
    level = "Prata"
elif 5001 <= xp <= 7000:
    level = "Ouro"
elif 7001 <= xp <= 8000:
    level = "Platina"
elif 8001 <= xp <= 9000:
    level = "Ascendente"
elif 9001 <= xp <= 10000:
    level = "Imortal"
else:
    level = "Radiante"

print(f"O Herói de nome {player_game} está no nível de {level}.")