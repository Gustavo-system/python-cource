"""
MAnejo de exceptions
"""

# sintaxis 
try:
    print("se ejecuta la logica del codigo que se debe cumplir")
except Exception:
    print("se captura la exception")
else:
    print("se muestra algo siempre y cuando no caiga en la exception")
finally:
    print("se ejecuta siempre que termina el try-except")
