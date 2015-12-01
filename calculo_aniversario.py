'''
Programa que calcula aniversario por ano, mes e dia
Marcus Gabaldo
01/12/2015
'''

import datetime

agora = datetime.date.today()
#agora = datetime.date(2015, 12, 20)
aniversario = datetime.date(1975, 12, 20)
#print ('Somando-se 2 dias:', (agora + datetime.timedelta(days=2)).strftime('%d/%m/%Y'))

data_atual = aniversario + datetime.timedelta(days=1) # comecar contar 1 dia depois da data inicial
numero_de_dias = 0
numero_de_dias_restantes = 0
numero_de_meses = 0

while data_atual < agora: # loop que conta dia por dia

	numero_de_dias += 1 # contador de dias corridos totais
	numero_de_dias_restantes += 1	
	data_atual = data_atual + datetime.timedelta(days=1)

	if(data_atual.day) == (aniversario.day):
		numero_de_meses += 1 # toda vez que o dia e o mesmo, soma 1 mes
		numero_de_dias_restantes = 0 # contador que zera toda vez que o dia e o mesmo

numero_de_anos = numero_de_meses/12
resto_de_meses = numero_de_meses - (int(numero_de_meses/12)*12)

print(int(numero_de_anos), "anos")	
print(int(resto_de_meses), "meses")
print(numero_de_dias_restantes, "dias")		
print(numero_de_dias, "dias totais")
