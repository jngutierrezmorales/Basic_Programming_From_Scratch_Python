
class Pokemon:
    vida_base = 100
    ataque = 10
    nombre = "Pokemon"

    def __init__(self):
        self.vida = self.vida_base

    def atacar(self, enemigo):
        enemigo.recibir_danio(self.ataque)

    def recibir_danio(self, danio):
        self.vida -= danio

    def mostrar_vida(self):
        print("Vida de {}: {}".format(self.nombre, self.vida))


class Charmander(Pokemon):
    vida_base = 100
    ataque = 10
    nombre = "Charmander"


class Pikachu(Pokemon):
    vida_base = 120
    ataque = 12
    nombre = "Pikachu"


class Bulbasaur(Pokemon):
    vida_base = 90
    ataque = 7
    nombre = "Bulbasaur"


mi_charmander = Charmander()
tu_pikachu = Pikachu()

mi_charmander.mostrar_vida()
tu_pikachu.mostrar_vida()

tu_pikachu.atacar(mi_charmander)

mi_charmander.mostrar_vida()

otro_charmander = Charmander()

otro_charmander.mostrar_vida()
mi_charmander.mostrar_vida()

