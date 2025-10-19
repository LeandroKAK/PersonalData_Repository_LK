from datetime import timedelta

# Inputs de entrada
print("Data Inicial")
diaI = int(input("Dia "))
horasI, minutosI, segundosI = map(int, input("Insira o horário nesse padrão hh:mm:ss ").split(':'))
print("Data Final")
diaF = int(input("Dia "))
horasF, minutosF, segundosF = map(int, input("Insira o horário nesse padrão hh:mm:ss ").split(':'))

# Utilizando o datetime para identificar os dias
 
data_inicial = timedelta(days=diaI, hours=horasI, minutes=minutosI, seconds=segundosI)
data_final = timedelta(days=diaF, hours=horasF, minutes=minutosF, seconds=segundosF)

# Calculo da diferença e tranferência para variáveis individuais

diferenca = data_final - data_inicial

dias = diferenca.days
segundos_totais = diferenca.seconds
horas, resto = divmod(segundos_totais, 3600)
minutos, segundos = divmod(resto, 60)

print(f'{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)\n')