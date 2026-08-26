# Polimofirmos
"""

Es una herramienta que permite redifinir métodos que heredemos de una clase padre.

"""

class Empleado:

    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    
    def calcularSueldo(self):
        sueldo = 12 * self.sueldo * (1 + 1/100)
        print(f"el sueldo anual de {self.nombre}, empleado normal, es de {sueldo} €")

class Contable(Empleado):

    # Si no hacemos nada podríamos omitir este texto y esto también es polimofirmos pero del init.
    def __init__(self, nombre, sueldo):
        super().__init__(nombre, sueldo)

    def calcularSueldo(self):
        sueldo = 12 * self.sueldo * (1 + 4/100)
        print(f"el sueldo anual de {self.nombre}, empleado contable, es de {sueldo} €")

class Publicista(Empleado):

    # Si no hacemos nada podríamos omitir este texto y esto también es polimofirmos pero del init.
    def __init__(self, nombre, sueldo):
        super().__init__(nombre, sueldo)

    def calcularSueldo(self):
        sueldo = 12 * self.sueldo * (1 + 5/100)
        print(f"el sueldo anual de {self.nombre}, empleado publicista, es de {sueldo} €")


class Becario (Empleado):

    # Si no hacemos nada podríamos omitir este texto y esto también es polimofirmos pero del init.
    def __init__(self, nombre, sueldo):
        super().__init__(nombre, sueldo)

    def calcularSueldo(self):
        sueldo = 12 * self.sueldo
        print(f"el sueldo anual de {self.nombre}, empleado becario, es de {sueldo} €")


empleados = [
    Empleado("Juan", 1000),
    Contable("Angela", 1100),
    Publicista("Ryan", 1200),
    Becario("pepito", 750)
]

for empleado in empleados:
    empleado.calcularSueldo()
