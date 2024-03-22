import math

raio = float(input("Insira o raio da circunferência: "))


volume = 4/3*math.pi*(raio)
volume = round(volume, 2)

print(f"O volume da circunferência é de: {volume}")