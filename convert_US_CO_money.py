dolares_americanos = input("¿Cuantos dolares Americanos tienes?: ")
# float function convert values to double
dolares_americanos = float(dolares_americanos)
valor_pesos = 0.00029
pesos = dolares_americanos / valor_pesos
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes " + pesos + " pesos Colombianos")
