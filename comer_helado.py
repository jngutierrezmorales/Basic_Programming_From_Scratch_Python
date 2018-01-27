
apetece_helado_input = input("Te apetece un helado? (Si/No): ")

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Te he dicho que me digas si o no, no se que has dicho pero cuento como que no")
    apetece_helado = False

tiene_dinero_input = input("¿Tienes dinero para un helado? (Si/No): ")
esta_el_senor_helados_input = input("¿Esta el señor de los helados? (Si / No): ")
esta_su_tia_input = input("¿Estas con tu tia? (Si / No): ")

tiene_dinero = tiene_dinero_input == "Si"
esta_su_tia = esta_su_tia_input == "Si"
puede_permitirselo = tiene_dinero or esta_su_tia
esta_el_senor_helados = esta_el_senor_helados_input == "Si"

if apetece_helado  and puede_permitirselo or esta_el_senor_helados:
    print("Pues comete un helado")
else:
    print("Pues nada")
