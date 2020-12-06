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
    pesos_colombia = input("¿Cuantos pesos Colombianos tienes?: ")
    pesos_colombia = float(pesos_colombia)
    dolares = pesos_colombia / dolar_to_CO_pesos
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " dolares")
elif option_selected == 2:
    pesos_argentina = input("¿Cuantos pesos Argentinos tienes?: ")
    pesos_argentina = float(pesos_argentina)
    dolares = pesos_argentina / dolar_to_ARG_pesos
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " dolares")
elif option_selected == 3:
    pesos_mexicanos = input("¿Cuantos pesos Mexicanos tienes?: ")
    pesos_mexicanos = float(pesos_mexicanos)
    dolares = pesos_mexicanos / dolar_to_MEX_pesos
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " dolares")
else:
    print("Error!! Opcion selecionada no valida")