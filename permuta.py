prfs = [
    [5, 'prf1','del1','del5'],
    [5, 'prf2','del4','del1'],
    [5, 'prf3','del1','del4'],
    [5, 'prf4','del5','del1'],
]

delegacias = [
    ['del1', 0],
    ['del2', 0],
    ['del3', 0],
    ['del4', 0],
    ['del5', 0],
    ['del6', 0],
]

resultado = []

def lista_prfs(recebe_prf):
    for busca_prf in prfs:
        if busca_prf[1] == recebe_prf[1]:
            pass
        else:
            if recebe_prf[2] == busca_prf[3]:
                if busca_prf[0] == 5:
                    if busca_prf[2] == recebe_prf[3]:
                        recebe_prf[0] = 1
                        busca_prf[0] = 1
                        resultado.append([recebe_prf[1], busca_prf[3]])
                        resultado.append([busca_prf[1], recebe_prf[3]])

                    break

for prf in prfs:
    if prf[0] == 5:
        lista_prfs(prf)



print(prfs)
print(resultado)
