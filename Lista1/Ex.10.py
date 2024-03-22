
gasolina = float(input(" Qual é preço da gasolina por litro? R$ "))
etanol = float(input(" Qual é o preço do etanol por litro? R$ "))

if (etanol/gasolina <= 0.7):
    print(f" É mais vantajosa abastecer com Etanol, seu preço por litro esta à R$ {etanol}/L")

else:
    print(f" É mais vantajosa abastecer com Gasolina, seu preço por litro esta à R$ {gasolina}/L")
