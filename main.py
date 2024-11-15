import random
from clases.enemigo import Enemigo
from clases.jugador import Jugador


def main():
    nombre_jugador = input("Bienvenido, ingresa tu nombre: ")
    jugador = Jugador(nombre_jugador)

    enemigo = [
        Enemigo("Alinen", 50, 10),
        Enemigo("Robot", 30, 5),
        Enemigo("Mounstro", 70, 15),
    ]
    enemigo_derrotado = []


    print('Comienza el Juego')

    while enemigo:
        enemigo_actual = random.choice(enemigo)
        if enemigo_actual in enemigo_derrotado:
            continue

        print(f'Te encuentras con un {enemigo_actual.nombre} en tu camino')

        while enemigo_actual.salud > 0:
            accion = input('Que deceas hacer (atacar/huir)').lower() 
            if accion == 'atacar':
                dano_jugador = jugador.atacar()
                print(f'has atacado al {enemigo_actual.nombre} y le has causado {dano_jugador} de dano')
                enemigo_actual.recibir_dano(dano_jugador)

                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    print(f'el {enemigo_actual.nombre} te ataco y te causo {dano_enemigo} de dano')
                    jugador.recibir_dano(dano_enemigo)
            elif accion == 'huir':
                print('has decidido huir')
                break
        if jugador.salud <= 0:
            print('has perdido la partida')
            break

        if enemigo_actual.salud <=0:
            enemigo_derrotado.append(enemigo_actual)
            enemigo.remove(enemigo_actual)

        jugador.ganar_experiencia(20)
        continuar = input('Quieres seguir? y/n: ').lower()

        if continuar != 'y':
            print('gracias por haber jugado')
            break
    if not enemigo:
        print('Ganasete el Juego')

if __name__ == '__main__': # no asegura que podremos ejectura desde el acchivo preoncipal
    main()