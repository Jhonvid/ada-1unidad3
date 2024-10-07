class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, dato):
        self.elementos.append(dato)

    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            return None

    def esta_vacia(self):
        return len(self.elementos) == 0

def es_operador(token):
    return token in "+-*/"

def evaluar_posfija(expresion):
    pila = Pila()

    for token in expresion.split():
        if token.isdigit():  # Si es un operando (número), lo apilamos
            pila.push(int(token))
        elif es_operador(token):  # Si es un operador, desapilamos dos operandos
            op2 = pila.pop()  # Segundo operando
            op1 = pila.pop()  # Primer operando
            if token == '+':
                pila.push(op1 + op2)
            elif token == '-':
                pila.push(op1 - op2)
            elif token == '*':
                pila.push(op1 * op2)
            elif token == '/':
                pila.push(op1 / op2)

    return pila.pop()  # El resultado final estará en la cima de la pila

def evaluar_prefija(expresion):
    pila = Pila()

    # Recorremos la expresión de derecha a izquierda
    for token in expresion.split()[::-1]:
        if token.isdigit():  # Si es un operando, lo apilamos
            pila.push(int(token))
        elif es_operador(token):  # Si es un operador, desapilamos dos operandos
            op1 = pila.pop()  # Primer operando
            op2 = pila.pop()  # Segundo operando
            if token == '+':
                pila.push(op1 + op2)
            elif token == '-':
                pila.push(op1 - op2)
            elif token == '*':
                pila.push(op1 * op2)
            elif token == '/':
                pila.push(op1 / op2)

    return pila.pop()  # El resultado final estará en la cima de la pila

def evaluar_expresion():
    tipo = input("¿Qué tipo de notación deseas evaluar? (posfija/prefija): ").strip().lower()
    
    if tipo not in ["posfija", "prefija"]:
        print("Tipo de notación no válida. Usa 'posfija' o 'prefija'.")
        return

    expresion = input(f"Introduce la expresión {tipo}: ").strip()

    if tipo == "posfija":
        resultado = evaluar_posfija(expresion)
    elif tipo == "prefija":
        resultado = evaluar_prefija(expresion)

    print(f"El resultado de la expresión {tipo} '{expresion}' es: {resultado}")

# Ejecutar el programa
evaluar_expresion()
