entrada = int (input())

anos = entrada//365
meses = (entrada % 365)//30
dias = entrada % 365 % 30

print(f'{anos} ano(s)\n'
f'{meses} mes(es)\n'
f'{dias} dia(s)')