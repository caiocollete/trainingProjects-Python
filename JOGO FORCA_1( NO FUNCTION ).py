import random, string
# CORES
RED   = "\033[1;31m"
BLUE  = "\033[0;34m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
YELLOW="\033[0;33m"


########CATEGORIAS######################
futebol = ['CORINTHIANS', 'SANTOS', 'FLAMENGO', 'PALMEIRAS', 'VASCO']
paises = ['NORUEGA', 'CROACIA', 'ESPANHA', 'INGLATERRA', 'PORTUGAL', 'ITALIA']
mCarros = ['BENTLEY', 'RENAULT', 'TOYOTA', 'FORD', 'FIAT']
########################################
futebolH = ['UDINESE', 'ARSENAL', 'NEWCASTLE', 'FEYENOORD', 'SOUTHAMPTON', 'SALERNITANA']
paisesH = ['UZBEQUISTAO', 'VIETNA', 'MARROCOS', 'TUVALU', 'SAMOA', 'QUIRIBATI']
mCarrosH = ['LAMBORGHINI', 'FERRARI', 'RENAULT', 'BUGATTI', 'KOENIGSEGG']
########################################

sugest = []
i = 0
acertos = 0
errosTL = 0
des_forca = ['''
 +---+
 |   |
     |
     |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
     |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |    
=========
''']

print(GREEN+'*** JOGO DA FORCA ***'+RESET+'\n')
#Seleção de Dificuldade
print(GREEN+"Selecione a dificuldade:\n1- Facil\n2- Dificil"+RESET+'\n-> ')
dificult = int(input())
if dificult==1:
    # SELECAO DE CATEGORIA E SORTEIO DE PALAVRAS
    print(GREEN+"Selecione a categoria desejada:\n1- Times de Futebol\n2- Paises\n3- Marcas de Carro"+RESET+'\n-> ')
    categoria = int(input())

    if categoria == 1:
        palavra = random.choice(futebol)
    if categoria == 2:
        palavra = random.choice(paises)
    if categoria == 3:
        palavra = random.choice(mCarros)
else:
    print(GREEN+"Selecione a categoria desejada:\n1- Times de Futebol\n2- Paises\n3- Marcas de Carro"+RESET+'\n-> ')
    categoria = int(input())

    if categoria == 1:
        palavra = random.choice(futebolH)
    if categoria == 2:
        palavra = random.choice(paisesH)
    if categoria == 3:
        palavra = random.choice(mCarrosH)

#####VERIFICAR QNTS LETRAS TEM ##########
qntdLetras = len(palavra)
#####################


## EXIBE A QUANTIDADE DE LETRAS
print(BLUE+des_forca[errosTL])
print('A quantidade de letras é de ', qntdLetras)
## INCREMENTA O ESPAÇO PARA A LETRA SER INSERIDA
for i in range(qntdLetras):
    sugest.append("")

## DICAS
if dificult == 1:
    if categoria == 1:
        if palavra == 'SANTOS':
            print('Dica: REI DO FUTEBOL')
        elif palavra == 'PALMEIRAS':
            print('Dica: Sem Mundial')
        elif palavra == 'VASCO':
            print('Dica: CAIU')
        elif palavra == 'FLAMENGO':
            print('Dica: 2019')
        elif palavra == 'CORINTHIANS':
            print('Dica: 2012')
    elif categoria == 2:
        print('Dica: Continente Europeu')
    elif categoria == 3:
        print('Dica: Tem em toda Cidade')

elif dificult == 2:
    if categoria == 1:
        if palavra == 'UDINENSE':
            print("Dica: Campeonato Italiano")
        elif palavra == 'ARSENAL':
            print('Dica: Unico time a vencer Premier League invicto')
        elif palavra == 'NEWCASTLE':
            print('Dica: Time inglês comprado por Árabes')
        elif palavra == 'FEYENOORD':
            print('Dica Primeiro time Holandês a vencer a UEFA CHAMPIONS LEAGUE')
        elif palavra == 'SOUTHAMPTON':
            print('Dica: Lanterna Premier League 22/23')
        elif palavra == 'SALERNITANA':
            print('Dica: Clube do OCHOA')
    elif categoria == 2:
        if palavra == 'TUVALU' or palavra == 'QUIRIBATI' or palavra == 'SAMOA':
            print('Dica: Oceania')
        elif palavra =='UZBEQUISTAO' or palavra == 'VIETNA':
            print('Dica: Ásia')
        else:
            print('Dica: Africa')
    elif categoria == 3:
        print('Dica: Carro Esportivo')




letra = input('Digite a letra: ').upper()
# LOOPING DO JOGO
while acertos != qntdLetras and errosTL < 6:
    tem=0
    for i in range(qntdLetras):
        if letra==sugest[i]:
            tem=1
            print('A letra ja foi digitada!')
    if tem==0:
        cont = 0
        for i in range(qntdLetras):
            if letra == palavra[i]:
                cont += 1
        if cont > 0:
            print('A letra %c apareceu %d vez' % (letra, cont))
            if cont > 0:
                # colocando nas posiçoes
                for pos in range(qntdLetras):
                    if palavra[pos] == letra:
                        sugest[pos] = letra
            # mostrando onde apareceu
            print('A letra a pareceu na seguintes posiçoes:')
            print(sugest)
            acertos = acertos + cont

        elif cont == 0:
            errosTL += 1
            print('Voce errou, a palavra nao contem essa letra!')
            print(sugest)

    if acertos != qntdLetras and errosTL < 6:
        print(des_forca[errosTL])
        letra = input('Digite a letra: ').upper()

if errosTL == 6 and acertos != qntdLetras:
    print(des_forca[errosTL])
    print(RESET+RED+'Voce perdeu, foi enforcado ate o talo!')
    print("A palavra era: " + RESET, palavra)
elif acertos == qntdLetras and errosTL < 6:
    print(RESET+YELLOW+'Voce ganhou o jogo!')
    print("A palavra era: "+RESET, palavra)
