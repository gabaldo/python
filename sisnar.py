'''
status = 0 --> ainda nao verificado ou sem possibilidades
status = 1 --> realocado
status = 5 --> aguardando futura saida


lista prfs = [status, nome, opcao1, latacao]

lista delegacias = [nome, efetivo]

'''

prfs = [
    [0, 'prf1','del1','del5'],
    [0, 'prf2','del5','del1'],
    [0, 'prf3','del5','del1'],
    # [0, 'prf4','del1','del2'],
    # [0, 'prf5','del2','del4'],
    # [0, 'prf6','del2','del4'],
    # [0, 'prf7','del2','del4'],
    # [0, 'prf8','del2','del1'],
]

delegacias = [
    ['del1', 0],
    ['del2', 0],
    ['del3', 0],
    ['del4', 0],
    ['del5', 1],
    ['del6', 0],
]

resultado = []

permutas = []

print(delegacias)

def busca_delegacia(recebe_prf):
    for delegacia in delegacias:
        if recebe_prf[2] == delegacia[0]:
            if delegacia[1] > 0:
                delegacia[1] -= 1
                print(recebe_prf[1], 'foi para', delegacia[0])
                resultado.append([recebe_prf[1], delegacia[0]])
                saida_delegacia(recebe_prf)
                return 1
            else:
                return 0

def busca_provavel_saida(recebe_delegacia):
    for futura_saida in prfs:
        if recebe_delegacia == futura_saida[3]:
            return 1

def saida_delegacia(recebe_prf):
	for delegacia in delegacias:
		if recebe_prf[3] == delegacia[0]:
			if delegacia[1] == 0:
				delegacia[1] += 1
				#print('Pesquisar prfs com status 5')
				pesquisa_status_5()
			else:
				delegacia[1] += 1

def pesquisa_status_5():
	for prf in prfs:
		if prf[0] == 5:
			if busca_delegacia(prf)== 1:
				prf[0] = 1
			else:
				if busca_provavel_saida(prf[2]) == 1:
					#print(prf[1], 'aguardando futura saida')
					prf[0] = 5
				else:
					#print(prf[1], 'sem possibilidades ou verificar outra opcao')
					pass


for prf in prfs:
	if busca_delegacia(prf)== 1:
		prf[0] = 1
	else:
		if busca_provavel_saida(prf[2]) == 1:
			#print(prf[1], 'aguardando futura saida')
			prf[0] = 5
		else:
			#print(prf[1], 'sem possibilidades')
			pass

#print(prfs)
print(delegacias)
print(resultado)





