
numero_tabla = int(input("De que numero quieres la tabla de multiplicar: "))

for multiplo in range(1, 11):
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))
