
N1 = float(input(" Insira a nota da primeira avaliação: "))
N2 = float(input(" Insira a nota da segunda avaliação: "))
N3 = float(input(" Insira a nota da terceira avaliação: "))
N4 = float(input(" Insira a nota da quarta avaliação: "))

P1 = 1
P2 = 2
P3 = 3
P4 = 4

media = (N1*P1) + (N2*P2) + (N3*P3) + (N4*P4)/(P1+P2+P3+P4)

print(f"A média ponderada é: {media}")

