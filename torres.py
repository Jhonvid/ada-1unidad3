class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            raise IndexError("Desapilando de una pila vacía")

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            raise IndexError("Cima de una pila vacía")

    def __str__(self):
        return str(self.items)

def torres_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        disco = origen.desapilar()
        destino.apilar(disco)
        print(f"Mover disco {disco} de Torre {origen} a Torre {destino}")
        print_torres(torre_A, torre_B, torre_C)
    else:
        torres_hanoi(n - 1, origen, auxiliar, destino)
        disco = origen.desapilar()
        destino.apilar(disco)
        print(f"Mover disco {disco} de Torre {origen} a Torre {destino}")
        print_torres(torre_A, torre_B, torre_C)
        torres_hanoi(n - 1, auxiliar, destino, origen)

def print_torres(torre_A, torre_B, torre_C):
    # Crear una representación gráfica de las torres invertidas
    max_height = max(len(torre_A.items), len(torre_B.items), len(torre_C.items))
    
    # Mostrar los discos desde la cima hasta la base
    for i in range(max_height):
        line = ""
        for torre in [torre_A, torre_B, torre_C]:
            if i < len(torre.items):
                disco = torre.items[i]
                # Representar el disco con su tamaño
                line += " " * (4 - disco) + "█" * (2 * disco) + " " * (4 - disco) + "   "
            else:
                line += " " * 8 + " " * 8 + "   "
        print(line)

    # Mostrar el nombre de cada torre
    print("Torre A      Torre B      Torre C")
    print("-" * 30)

# Crear las pilas para las torres
torre_A = Pila()
torre_B = Pila()
torre_C = Pila()

# Inicializar la torre A con 4 discos
num_discos = 4
for disco in range(num_discos, 0, -1):
    torre_A.apilar(disco)

# Mostrar el estado inicial
print("Estado inicial:")
print_torres(torre_A, torre_B, torre_C)

# Resolver el juego
torres_hanoi(num_discos, torre_A, torre_C, torre_B)

# Mostrar el estado final
print("Estado final:")
print_torres(torre_A, torre_B, torre_C)
