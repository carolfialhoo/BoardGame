import random

# parametros de entrada
escadas = {3: 16, 5: 7, 15: 25, 18: 20, 21: 32}
cobras = {12: 2, 14: 11, 17: 4, 31: 19, 35: 22 }
final = 36

# funcao jogo
def jogar_padrao():
    posicao = [1, 1]
    turno = 0
    quedas_cobras = [0,0]
    while True:
        dado = random.randint(1, 6)
        posicao[turno] += dado
        if posicao[turno] in escadas:
            posicao[turno] = escadas[posicao[turno]]
        elif posicao[turno] in cobras:
            posicao[turno] = cobras[posicao[turno]]
            quedas_cobras[turno] += 1
        if posicao[turno] >= final:
            return turno, quedas_cobras
        turno = 1 - turno

# funcao jogo escadas
def jogar_escadas_50_chance():
    posicao = [1, 1]
    turno = 0
    lancamentos = 0
    while True:
        dado = random.randint(1, 6)
        lancamentos += 1
        posicao[turno] += dado
        if posicao[turno] in escadas:
            if random.random() < 0.5:
              posicao[turno] = escadas[posicao[turno]]
        elif posicao[turno] in cobras:
            posicao[turno] = cobras[posicao[turno]]
        if posicao[turno] >= final:
            return lancamentos
        turno = 1 - turno

# funcao jogo com posicao do segundo jogador alterada
def jogar_alterar_posicao_segundo():
    posicao = [1, 7]
    turno = 0
    while True:
        dado = random.randint(1, 6)
        posicao[turno] += dado
        if posicao[turno] in escadas:
            posicao[turno] = escadas[posicao[turno]]
        elif posicao[turno] in cobras:
            posicao[turno] = cobras[posicao[turno]]
        if posicao[turno] >= final:
            return turno
        turno = 1 - turno

# funcao jogo com imunidade jogador 2 na primeira cobra
def jogar_imunidade():
    posicao = [1, 1]
    turno = 0
    quedas_cobras = [0, 0]
    while True:
        dado = random.randint(1, 6)
        posicao[turno] += dado
        if posicao[turno] in escadas:
            posicao[turno] = escadas[posicao[turno]]
        elif posicao[turno] in cobras:
            if turno == 1:
                if quedas_cobras[1] == 0:
                    quedas_cobras[1] += 1
                else:
                    posicao[turno] = cobras[posicao[turno]]
                    quedas_cobras[1] += 1
            else:
                posicao[turno] = cobras[posicao[turno]]
                quedas_cobras[0] += 1

        if posicao[turno] >= final:
            return turno
        turno = 1 - turno

# inicializando contagem de vitorias de cada jogador, contagem de quedas em cobras, contagem de
# lancamentos (50% escadas), contagem de vitorias posicao do 2 alternada, contagem de vitorias com o o jogador 2 com imunidade
vitorias = [0, 0]
cont_cobras = 0
cont_lancamentos = 0
vitorias_chances_alteradas = [0, 0]
vitorias_imunidade = [0, 0]

# experimento
for _ in range(10000):
    # chama a primeira funcao
    vencedor, quedas_cobras = jogar_padrao()
    # chama a segunda funcao
    lancamentos = jogar_escadas_50_chance()
    # chama a terceira funcao
    vencedor_alterado = jogar_alterar_posicao_segundo()
    # chama a quarta funcao
    vencedor_imunidade = jogar_imunidade()
    # contagem de vitorias padrao
    vitorias[vencedor] += 1
    # contagem de queda em cobras
    cont_cobras += sum(quedas_cobras)
    # contagem de lancamentos (escadas com 50% de chance de ativar)
    cont_lancamentos += lancamentos
    # contagem de vitorias posicao do jogador 2 alterada
    vitorias_chances_alteradas[vencedor_alterado] += 1
    # contagem de vitorias com jogador 2 imune primeira cobra
    vitorias_imunidade[vencedor_imunidade] += 1

# probabilidade do jogador que começa vencer
probabilidade = (vitorias[0]/10000)*100
print(f"A probabilidade de o jogador que começa o jogo vencer é de {(vitorias[0]/10000)*100:.2f}%")

# media de cobras
print(f"A media de quedas em cobras por jogo é de {cont_cobras/10000:.2f}")

# media de lancamentos
print(f"A media de lancamentos por jogo com escadas com 50% de chance é de {cont_lancamentos/10000:.2f}")

# experimentos para que os jogadores tenham aproximadamente
# chances iguais de vencerem o jogo
print(f"A probabilidade de o jogador 1 vencer é de {(vitorias_chances_alteradas[0] / 10000) * 100:.2f}% e a probabilidade de o jogador 2 vencer é de {(vitorias_chances_alteradas[1] / 10000) * 100:.2f}%")
print("Para que o jogador 1 e o jogador 2 tenham chances próximas de vencer é necessário que o 2 inicie na casa 7")

# probabilidade aproximada de que o Jogador 1 vença com o jogador 2 com imunidade na primeira cobra
print(f"A probabilidade de o jogador 1 vencer é de aproximadamente {(vitorias_imunidade[0] / 10000) * 100:.2f}%")