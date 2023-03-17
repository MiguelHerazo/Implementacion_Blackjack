class Blackjack:
    def __init__(self):
        pass
    def registrar_jugador(self, nombre):
        pass
    def iniciar_juego(self, apuesta):
        pass
    def verificar_ganador(self) -> bool:
        pass
    def verificar_perdedor(self) -> bool:
        pass
    def verificar_empate(self) -> bool:
        pass

class Jugador:
    def __init__(self, fichas:int, nombre:str):
        self.fichas = fichas
        self.nombre = nombre

    def inicializar_mano(self,cartas):
        pass
    def seleccionar_jugada(self):
        pass
    def pedir_carta(self):
        pass

class Carta:
    def __init__(self,pinta:str,valor:str):
        pass

class Mano:
    def __init__(self,cartas):
        pass
    def es_blackjack(self) -> bool:
        pass
    def calcular_valor_mano(self,pinta,valor):
        pass
    def valor_mano(self) -> bool:
        pass

    def verificar_21(self,pinta,valor):
        pass


class Baraja:
    def __init__(self):
        pass
    def revolver(self):
        pass
    def repartir_carta(tapada) -> Carta:
        pass
    def repartir_carta(self):
        pass

