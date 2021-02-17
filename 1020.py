entrada = int (input())

horas = (entrada//60)//60
minutos = (entrada//60) % 60
segundos = entrada % 60

print(f"{horas}:{minutos}:{segundos}")
