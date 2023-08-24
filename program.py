valor = int(input("Digite o valor no Sistema Decimal: "))
base = int(input("Digite a base para qual se deve converter: "))
quociente = abs(valor)
restos = ""

while quociente > 0:
    restos += str(quociente % base)
    quociente = quociente // base

if valor > 0:
    print(f"({valor})10 = ({restos[::-1]}){base}")
else:
    print(f"({valor})10 = (-{restos[::-1]}){base}")
