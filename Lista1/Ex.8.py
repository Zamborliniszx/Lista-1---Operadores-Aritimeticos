
weight = float(input(" Insira o peso em quilograma: "))
height = float(input(" Insira a altura em metros: "))

IMC = weight/height ** 2
IMC = round(IMC, 2)

print(" O IMC é", IMC)