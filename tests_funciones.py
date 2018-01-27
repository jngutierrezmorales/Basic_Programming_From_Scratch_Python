
def input_con_confirmacion(pregunta):
    confirmacion = False
    while not confirmacion:
        dato_usuario = input(pregunta)
        seguro = input("Has dicho {}, ¿Estas seguro? [Si / No] ".format(dato_usuario))
        if seguro == "Si":
            confirmacion = True
    return dato_usuario


nombre = input_con_confirmacion("¿Como te llamas? ")
print("Has confirmado que te llamas {}".format(nombre))

numero = input_con_confirmacion("Dime un numero ")
print("Has confirmado que el numero es {}".format(numero))
