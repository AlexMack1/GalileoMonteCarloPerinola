import numpy as np
import matplotlib.pyplot as plt

class Jugador:
    def __init__(self, dinero_inicial):
        self.billetera = dinero_inicial
        self.ganado = 0
        self.perdido = 0

    def pon(self, cantidad):
        monto = min(cantidad, self.billetera)
        self.billetera -= monto
        self.perdido += monto
        return monto

    def toma(self, cantidad):
        self.billetera += cantidad
        self.ganado += cantidad

def jugar_perinola(jugadores, pozo):
    acciones = ["Pon 1", "Pon 2", "Toma 1", "Toma 2", "Toma todo", "Todos ponen"]
    resultado = np.random.choice(acciones)

    if resultado == "Pon 1":
        pozo += jugadores[0].pon(1)
    elif resultado == "Pon 2":
        pozo += jugadores[0].pon(2)
    elif resultado == "Toma 1":
        if pozo > 0:
            pozo -= 1
            jugadores[0].toma(1)
    elif resultado == "Toma 2":
        monto = min(2, pozo)
        pozo -= monto
        jugadores[0].toma(monto)
    elif resultado == "Toma todo":
        jugadores[0].toma(pozo)
        pozo = 0
    elif resultado == "Todos ponen":
        for jugador in jugadores:
            pozo += jugador.pon(1)

    jugadores = jugadores[1:] + [jugadores[0]]

    return jugadores, pozo

def simulacion(n_jugadores, m_juegos, dinero_inicial):
    jugadores = [Jugador(dinero_inicial) for _ in range(n_jugadores)]
    pozo = 0
    juegos_para_ganador = -1
    juegos_para_bancarrota = -1

    for i in range(m_juegos):
        jugadores, pozo = jugar_perinola(jugadores, pozo)

        if any(j.billetera == dinero_inicial * n_jugadores for j in jugadores) and juegos_para_ganador == -1:
            juegos_para_ganador = i + 1

        if any(j.billetera == 0 for j in jugadores) and juegos_para_bancarrota == -1:
            juegos_para_bancarrota = i + 1

    return jugadores, juegos_para_ganador, juegos_para_bancarrota


n_jugadores = 5
m_juegos = 10000
dinero_inicial = 100

jugadores, juegos_ganador, juegos_bancarrota = simulacion(n_jugadores, m_juegos, dinero_inicial)

print(f"Juegos para que haya un ganador: {juegos_ganador if juegos_ganador != -1 else 'No hubo ganador en ' + str(m_juegos) + ' juegos'}")
print(f"Juegos para que un jugador se quede sin dinero: {juegos_bancarrota if juegos_bancarrota != -1 else 'Ningún jugador se quedó sin dinero en ' + str(m_juegos) + ' juegos'}")


# Gráfica de ganancias/pérdidas al final de la simulación
fig, ax = plt.subplots()
nombres = [f"Jugador {i+1}" for i in range(n_jugadores)]
ganancias = [j.ganado - j.perdido for j in jugadores]
ax.bar(nombres, ganancias)
ax.set_title("Ganancia/Pérdida por jugador al término de la simulación")
plt.xticks(rotation=45)
plt.show()
