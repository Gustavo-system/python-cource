def genera_pares(limite):
    num = 0
    mi_lista = []
    while num < limite:
        # print(f"num {num} * 2: {num*2}")
        mi_lista.append(num*2)
        num = num + 1
    return mi_lista

print(genera_pares(10))


"""Generadores"""
def genera_pares_optimizado(limite):
    num = 0
    mi_lista = []
    while num < limite:
        yield num*2
        num = num + 1
    return mi_lista

numero_generado = genera_pares_optimizado(10)

print(f"numero generado {next(numero_generado)}")
print(f"numero generado {next(numero_generado)}")
print(f"numero generado {next(numero_generado)}")
print(f"numero generado {next(numero_generado)}")
print(f"numero generado {next(numero_generado)}")
print(f"numero generado {next(numero_generado)}")


"""Generador de numeros pares"""
def genera_pares(limite):
    for numero in range(0, limite + 1):
        if numero % 2 == 0:
            yield numero


for generador in genera_pares(10):
    print(generador)


# generador de numero x2
def genera_pares_v2(limite):
    numero = 1
    while numero <= limite:
        yield numero * 2
        numero = numero + 1

for generador in genera_pares_v2(10):
    print(generador)