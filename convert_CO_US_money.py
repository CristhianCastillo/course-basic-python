# Functions

def convertion(type_pesos, dolar_value):
    pesos = input("¿Cuantos pesos " + type_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / dolar_value
    dolares = round(dolares, 2)
    return str(dolares)


menu_options = """
Bienvenido al conversor de monedas 🖤

1. Pesos colombianos
2. Pesos argentinos
3. Pesos mexicanos
    
By: Cristhian Castillo

Elige una opcion: """
dolar_to_CO_pesos = 3466
dolar_to_ARG_pesos = 81.66
dolar_to_MEX_pesos = 19.77

option_selected = int(input(menu_options))

if option_selected == 1:
    result = convertion("Colombianos", dolar_to_CO_pesos)
    print("Tienes $ " + result + " dolares")
elif option_selected == 2:
    result = convertion("Argentinos", dolar_to_ARG_pesos)
    print("Tienes $ " + result + " dolares")
elif option_selected == 3:
    result = convertion("Mexicanos", dolar_to_ARG_pesos)
    print("Tienes $ " + result + " dolares")
else:
    print("Error!! Opcion selecionada no valida")