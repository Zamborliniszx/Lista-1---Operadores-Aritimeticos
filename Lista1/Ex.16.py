
fahrenheit = float(input("Insira a temperatura em graus Fahrenheit: "))

celsius = (fahrenheit-32)/1.8
celsius = round(celsius, 2)

print(f"{fahrenheit}°F representa {celsius}°C")