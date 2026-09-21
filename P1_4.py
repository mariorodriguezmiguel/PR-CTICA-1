
coste_adquisicion = float(input("Introduce el precio de adquisicion: "))
beneficio = coste_adquisicion * 1.25
IVA = beneficio * 0.21
precio_final = beneficio + IVA

print(f"El valor del impuesto es: {IVA}")
print(f"El precio final del programa es: {precio_final}")