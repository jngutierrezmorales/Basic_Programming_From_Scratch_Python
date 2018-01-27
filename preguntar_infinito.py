

confirmacion_borrado = ""
respuestas_posibles = ["Si", "No", "Depende", "Posiblemente", "Quizas"]

while confirmacion_borrado not in respuestas_posibles:
    confirmacion_borrado = input("¿Quieres borrar el archivo? ({}): ".format("/".join(respuestas_posibles)))

