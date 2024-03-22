
age = float(input("Insira a sua idade atual: "))
mes = float(input("Insira o mês que você nasceu: "))
day = float(input("Insira o dia que você nasceu: "))

age_day = (age*365) + (mes*30) + day

print(f" Você tem {age_day} dias de vida!")