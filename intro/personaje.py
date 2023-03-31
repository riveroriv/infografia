import time
import random

class Personaje:
    def __init__(self, nombre, vitalidad):
        self.nombre = nombre
        self.vitalidad = vitalidad
    
    def saludo(self):
        print(f'\nHola, mi nombre es {self.nombre}\n')
    
    def recibir_daño(self, daño):
        self.vitalidad -= daño
    
    def esta_vivo(self):
        return self.vitalidad > 0


class Jugador(Personaje):
    def __init__(self, nombre, vitalidad, habilidades):
        super().__init__(nombre, vitalidad)
        self.habilidades = habilidades
    
    def contraatacar(self, enemigo):
        # añadimos contrataque al jugador

        if random.random() < 0.7:
            # ocurre contrataque
            daño = int(self.vitalidad * 0.1)

            if random.random() < 0.2:
                # contraataque es crítico
                daño = int(daño * 1.5)
            
            print(f'Jugador {self.nombre} realiza contraataque con daño: {daño}')
            enemigo.recibir_daño(daño)

    def listar_habilidades(self):
        for h in self.habilidades:
            print(f'Puedo {h}')
        print('\n')


class Enemigo(Personaje):
    def __init__(self, nombre, vitalidad, daño_maximo, ataque_esp):
        super().__init__(nombre, vitalidad)
        self.daño_maximo = daño_maximo
        # ahora el daño especificado es el máximo posible

        self.ataque_esp = ataque_esp
    
    def atacar_jugador(self, jugador):
        daño = int(self.daño_maximo * random.random())
        # el enemigo ataca con un porcentaje random de su daño máximo

        print(f'Enemigo {self.nombre} atacando a jugador {jugador.nombre} con daño: {daño}')
        jugador.recibir_daño(daño)
        if jugador.esta_vivo():
            jugador.contraatacar(self)


jugador = Jugador('Juan', 100, ['atacar', 'volar', 'esquivar'])
jugador.saludo()
jugador.listar_habilidades()

enemigo = Enemigo('Raul', 50, 20, 70)

while jugador.esta_vivo():
    enemigo.atacar_jugador(jugador)

    if not jugador.esta_vivo():
        print(f'El jugador {jugador.nombre} ha muerto')
        break
    if not enemigo.esta_vivo():
        print(f'El enemigo {enemigo.nombre} ha muerto')
        break

    print(f'\tvitalidad {jugador.nombre}: {jugador.vitalidad}')
    print(f'\tvitalidad enemigo {enemigo.nombre}: {enemigo.vitalidad}\n')
    time.sleep(2)
