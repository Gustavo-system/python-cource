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