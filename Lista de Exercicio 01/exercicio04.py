segundos_digitados = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = segundos_digitados // 86400
horas = (segundos_digitados % 86400)//3600
minutos = ((segundos_digitados % 86400)%3600)//60
segundos = (((segundos_digitados % 86400)%3600)%60)
print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.')

