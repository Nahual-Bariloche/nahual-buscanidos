# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

#Clase Pinguino
class PinguNahual(pilasengine.actores.Actor):

    def iniciar(self):
        self.escala = 1
        self.x = -266
        self.y = -212
        self.aprender(pilas.habilidades.SeguirClicks)
        self.imagen = self.pilas.imagenes.cargar_grilla("pingu.png", 10)

    def posibles_pasos(self):
        pass

#MapaSuelo esta pensado para que pueda tener toda la información del suelo.
class MapaSuelo():

    # Las posiciones las tendriamos que definir como Ej: [1,1] [1,2] [1,3] [1,4][2,1][2,2], etc
    posiciones = 40

    def iniciar(self):
        pass

    # Debería generar las posiciones, con los valores de caminio firme, y camino con grieta
    def generarPosiciones(self):
        pass

    # Le devuelve al Pinguino los pasos posibles para su turno.
    def posiblesPasosPistas(self):
        pass

dialogo = pilas.actores.Dialogo()

#actores
pingu = PinguNahual(pilas)
moneda = pilas.actores.Moneda(x=287, y=206)
moneda.escala = 1

moneda.aprender(pilas.habilidades.PuedeExplotar)

def colision_moneda (pingu, moneda):
   moneda.eliminar()
    
pilas.colisiones.agregar(pingu, moneda, colision_moneda)


# Añadir un marcador
puntos = pilas.actores.Puntaje(x=-280, y=200, color=pilas.colores.blanco)
puntos.magnitud = 40

pilas.ejecutar()
