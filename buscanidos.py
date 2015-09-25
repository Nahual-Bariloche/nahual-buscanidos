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

    posiciones = 40

    def iniciar(self):
        pass

    def generarPosiciones(self):
        pass

    def generarGrietas(self):
        pass

    def posiblesPasosPistas(self):
        pass

dialogo = pilas.actores.Dialogo()

#actores
pingu = PinguNahual(pilas)
moneda = pilas.actores.Moneda(x=287, y=206)
moneda.escala = 1


# Añadir un marcador
puntos = pilas.actores.Puntaje(x=-280, y=200, color=pilas.colores.blanco)
puntos.magnitud = 40

pilas.ejecutar()
