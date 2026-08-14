def calcular_rankeada(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas

    if vitorias <= 10:
        nivel = "Ferro"
    elif vitorias <= 20:
        nivel = "Bronze"
    elif vitorias <= 50:
        nivel = "Prata"
    elif vitorias <= 80:
        nivel = "Ouro"
    elif vitorias <= 90:
        nivel = "Diamante"
    elif vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return saldo_vitorias, nivel


while True:
    vitorias = int(input("Digite a quantidade de vitórias: "))
    derrotas = int(input("Digite a quantidade de derrotas: "))

    saldo, nivel = calcular_rankeada(vitorias, derrotas)

    print(f"\nO Herói tem saldo de {saldo} e está no nível de {nivel}")

    continuar = input("\nDeseja calcular novamente? (s/n): ").lower()

    if continuar != "s":
        print("Programa encerrado!")
        break