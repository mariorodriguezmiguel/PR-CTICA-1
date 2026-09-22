# CÁLCULO DEL CENTRO DE GRAVEDAD DE 3 MASAS PUNTUALES

x1 = float(input("Coordenada x del punto 1:"))
y1 = float(input("Coordenada y del punto 1: "))
m1 = float(input("Masa en el punto 1: "))

x2 = float(input("Coordenada x del punto 2:"))
y2 = float(input("Coordenada y del punto 2: "))
m2 = float(input("Masa en el punto 2: "))

x3 = float(input("Coordenada x del punto 3:"))
y3 = float(input("Coordenada y del punto 3: "))
m3 = float(input("Masa en el punto 3: "))

# FÓRMULAS
M = m1 + m2 + m3
XG = (m1 * x1 + m2 * x2 + m3 * x3) / M
YG = (m1 * y1 + m2 * y2 + m3 * y3) / M

print(f"Las coordenadas del centro de gravedad son ({XG:.2f},{YG:.3f})")
# :.2f PARA PONER DOS Nº DECIMALES 
# :.3f PARA PONER TRES Nº DECIMALES 
