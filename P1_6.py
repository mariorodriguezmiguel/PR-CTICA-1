# PASAR DE HORAS/MINUTOS/SEGUNDOS UN TIEMPO DADO POR EL USUARIO (Y A LA INVERSA)

# Primera parte: de hh:mm:ss a segundos
horas=int(input("Introduce las horas:"))
minutos=int(input("Introduce los minutos:"))
segundos=int(input("Introduce los segundos:"))

total=horas*3600+minutos*60+segundos;
print(f"El tiempo en segundos es {total}")

# Segunda parte: de segundos a hh:mm:ss
# Se debe calcular el valor de hh, mm, ss a partir del valor de total2
total2=int(input("Dame un tiempo total en segundos:"))

hh = total2//3600
resto_hh = total2 % 3600

mm = resto_hh//60
ss = resto_hh % 60

print(f"{total2} segundos son {hh}:{mm}:{ss}") 
