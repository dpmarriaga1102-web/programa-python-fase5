empleados = [
    ["Carlos", 8, 9, 8, 10, 9],
    ["Ana", 7, 8, 7, 8, 7],
    ["Luis", 9, 9, 10, 9, 9],
    ["Marta", 6, 7, 6, 7, 6]
]

def calcular_jornada(horas):
    total = sum(horas)
    if total > 40:
        return total, "Sobretiempo"
    else:
        return total, "Horario Estándar"

for empleado in empleados:
    nombre = empleado[0]
    horas = empleado[1:]
    total, clasificacion = calcular_jornada(horas)
    
    print(nombre, total, clasificacion)