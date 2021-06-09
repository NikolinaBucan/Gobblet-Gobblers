import pygame

# GLOBAL VARIABLES
pygame.init()
screen = pygame.display.set_mode((1300, 1000))
pygame.display.set_caption("TIC - TAC - TOE")
pozadina = pygame.image.load('Pozadina.png')
cPobeda = pygame.image.load('cPobeda.png')
pPobeda = pygame.image.load('pPobeda.png')
nereseno = pygame.image.load('Nereseno.png')
crveni3 = pygame.image.load('Crveni3.png')
crveni2 = pygame.image.load('Crveni2.png')
crveni1 = pygame.image.load('Crveni1.png')
crveni3_2 = pygame.image.load('Crveni3.png')
crveni2_2 = pygame.image.load('Crveni2.png')
crveni1_2 = pygame.image.load('Crveni1.png')
plavi3 = pygame.image.load('Plavi3.png')
plavi2 = pygame.image.load('Plavi2.png')
plavi1 = pygame.image.load('Plavi1.png')
plavi3_2 = pygame.image.load('Plavi3.png')
plavi2_2 = pygame.image.load('Plavi2.png')
plavi1_2 = pygame.image.load('Plavi1.png')
selekcija1 = pygame.image.load('Selekcija1.png')
selekcija2 = pygame.image.load('Selekcija2.png')
running = True

player1 = True
player2 = False

c1_1x = 10
c1_1y = 315
c1_2x = 10
c1_2y = 485
c1_3x = 10
c1_3y = 655

c2_1x = 150
c2_1y = 315
c2_2x = 150
c2_2y = 485
c2_3x = 150
c2_3y = 655

p3_1x = 1008
p3_1y = 315
p3_2x = 1008
p3_2y = 485
p3_3x = 1008
p3_3y = 655

p4_1x = 1158
p4_1y = 315
p4_2x = 1158
p4_2y = 485
p4_3x = 1158
p4_3y = 655

mestoSvihPijuna = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 1], [4, 2],[4, 3]]

polje11 = [0,0] #prva koordinata odredjuje sta poslednje stoji na njemu, 0 za prazno, 1 za malog pijuna, 2 za srednjeg, 3 za velikog, kao sto je druga koordinata za mesto
polje21 = [0,0] #druga odredjuje koja boja stoji na njemu, 0 - niko, 1 - crveni, 2 - plavi
polje31 = [0,0]
polje12 = [0,0]
polje22 = [0,0]
polje32 = [0,0]
polje13 = [0,0]
polje23 = [0,0]
polje33 = [0,0]

svaPolja = [polje11, polje12, polje13, polje21, polje22, polje23, polje31, polje32, polje33]

pijunSelekcija = True
poljeSelekcija = True
polje = [0, 0]
mesto = [0, 0]



# GAME
def CrtajPozadinu():
    if ProveriKrajIgre() == 1:
        screen.blit(cPobeda, (0, 0))
    elif ProveriKrajIgre() == 2:
        screen.blit(pPobeda, (0, 0))
    elif ProveriKrajIgre() == 3:
        screen.blit(nereseno, (0, 0))
    else:
        screen.blit(pozadina, (0, 0))

        screen.blit(crveni1, (c1_1x, c1_1y))
        screen.blit(crveni1_2, (c2_1x, c2_1y))
        screen.blit(plavi1, (p4_1x, p4_1y))
        screen.blit(plavi1_2, (p3_1x, p3_1y))

        screen.blit(crveni2, (c1_2x, c1_2y))
        screen.blit(crveni2_2, (c2_2x, c2_2y))
        screen.blit(plavi2, (p4_2x, p4_2y))
        screen.blit(plavi2_2, (p3_2x, p3_2y))

        screen.blit(crveni3, (c1_3x, c1_3y))
        screen.blit(crveni3_2, (c2_3x, c2_3y))
        screen.blit(plavi3, (p4_3x, p4_3y))
        screen.blit(plavi3_2, (p3_3x, p3_3y))


def NadjiMestoPijuna(mousePOS):
    if (mousePOS[0] >= 10 and mousePOS[0] <= 142):
        kolona = 1
    elif (mousePOS[0] >= 150 and mousePOS[0] <= 282):
        kolona = 2
    elif (mousePOS[0] >= 1008 and mousePOS[0] <= 1140):
        kolona = 3
    elif (mousePOS[0] >= 1158 and mousePOS[0] <= 1290):
        kolona = 4
    else:
        kolona = 0

    if (mousePOS[1] >= 315 and mousePOS[1] <= 447):
        red = 1
    elif (mousePOS[1] >= 485 and mousePOS[1] <= 617):
        red = 2
    elif (mousePOS[1] >= 655 and mousePOS[1] <= 787):
        red = 3
    else:
        red = 0

    return [kolona, red]


def NadjiPolje(mousePOS):
    if (mousePOS[0] >= 305 and mousePOS[0] < 535):
        kolona = 1
    elif (mousePOS[0] >= 535 and mousePOS[0] < 765):
        kolona = 2
    elif (mousePOS[0] >= 765 and mousePOS[0] < 995):
        kolona = 3
    else:
        kolona = 0

    if (mousePOS[1] >= 155 and mousePOS[1] < 385):
        red = 1
    elif (mousePOS[1] >= 385 and mousePOS[1] < 615):
        red = 2
    elif (mousePOS[1] >= 615 and mousePOS[1] < 845):
        red = 3
    else:
        red = 0

    return [kolona, red]

def ProveriKrajIgre():
    sveKombinacijeZaPolja = [[polje11, polje21, polje31], [polje12, polje22, polje32], [polje13, polje23, polje33],[polje11, polje12, polje13], [polje21, polje22, polje23], [polje31, polje32, polje33],[polje11, polje22, polje33], [polje31, polje22, polje13]]


    for kombinacijaPolja in sveKombinacijeZaPolja:
        crveni = 0
        plavi = 0
        for p in kombinacijaPolja:
            if p[1] == 1:
                crveni += 1
            elif p[1] == 2:
                plavi += 1
        if crveni == 3:
            return 1
        elif plavi == 3:
            return 2

    mmax = 0
    nmin = 4
    if mestoSvihPijuna is []:
        return 3
    elif [0,0] not in svaPolja:
        for m in mestoSvihPijuna:
            if m[1]>mmax:
                mmax=m[1]
        for n in svaPolja:
            if n[0]<nmin:
                nmin=n[0]
        if mmax<= nmin:
            return 3


while running:
    CrtajPozadinu()

    if player1:
        # MOUSE data
        mousePOS = pygame.mouse.get_pos()

        if pijunSelekcija:
            mesto = NadjiMestoPijuna(mousePOS)

        # selekcija Pijuna

        if mesto == [1, 1] and mesto in mestoSvihPijuna:
            screen.blit(selekcija2, (10, 315))
        elif mesto == [1, 2] and mesto in mestoSvihPijuna:
            screen.blit(selekcija2, (10, 485))
        elif mesto == [1, 3] and mesto in mestoSvihPijuna:
            screen.blit(selekcija2, (10, 655))
        elif mesto == [2, 1] and mesto in mestoSvihPijuna:
            screen.blit(selekcija2, (150, 315))
        elif mesto == [2, 2]and mesto in mestoSvihPijuna:
            screen.blit(selekcija2, (150, 485))
        elif mesto == [2, 3] and mesto in mestoSvihPijuna:
            screen.blit(selekcija2, (150, 655))

        if pijunSelekcija == False:
            # selekcija Polja
            if poljeSelekcija:
                polje = NadjiPolje(mousePOS)
                if polje == [1, 1] and mesto[1] > polje11[0]:
                    screen.blit(selekcija1, (305, 155))
                elif polje == [1, 2] and mesto[1] > polje12[0]:
                    screen.blit(selekcija1, (305, 385))
                elif polje == [1, 3] and mesto[1] > polje13[0]:
                    screen.blit(selekcija1, (305, 615))
                elif polje == [2, 1] and mesto[1] > polje21[0]:
                    screen.blit(selekcija1, (535, 155))
                elif polje == [2, 2] and mesto[1] > polje22[0]:
                    screen.blit(selekcija1, (535, 385))
                elif polje == [2, 3] and mesto[1] > polje23[0]:
                    screen.blit(selekcija1, (535, 615))
                elif polje == [3, 1] and mesto[1] > polje31[0]:
                    screen.blit(selekcija1, (765, 155))
                elif polje == [3, 2] and mesto[1] > polje32[0]:
                    screen.blit(selekcija1, (765, 385))
                elif polje == [3, 3] and mesto[1] > polje33[0]:
                    screen.blit(selekcija1, (765, 615))
            else:
                if polje == [1, 1]:
                    x = "c" + str(mesto[0]) + "_" + str(mesto[1]) + "x"
                    vars()[x] = 305 + 49
                    y = "c" + str(mesto[0]) + "_" + str(mesto[1]) + "y"
                    vars()[y] = 155 + 49
                    player1 = False
                    player2 = True
                    polje11[0] = mesto[1]
                    polje11[1] = 1

                    pijunSelekcija = True
                    poljeSelekcija = True
                    mesto = [0,0]
                    polje = [0,0]

                elif polje == [1, 2]:
                    x = "c" + str(mesto[0]) + "_" + str(mesto[1]) + "x"
                    vars()[x] = 305 + 49
                    y = "c" + str(mesto[0]) + "_" + str(mesto[1]) + "y"
                    vars()[y] = 385 + 49
                    player1 = False
                    player2 = True
                    polje12[0] = mesto[1]
                    polje12[1] = 1

                    pijunSelekcija = True
                    poljeSelekcija = True
                    mesto = [0, 0]
                    polje = [0, 0]

                elif polje == [1, 3]:
                    x = "c" + str(mesto[0]) + "_" + str(mesto[1]) + "x"
                    vars()[x] = 305 + 49
                    y = "c" + str(mesto[0]) + "_" + str(mesto[1]) + "y"
                    vars()[y] = 615 + 49
                    player1 = False
                    player2 = True
                    polje13[0] = mesto[1]
                    polje13[1] = 1

                    pijunSelekcija = True
                    poljeSelekcija = True
                    mesto = [0, 0]
                    polje = [0, 0]

                elif polje == [2, 1]:
                    x = "c" + str(mesto[0]) + "_" + str(mesto[1]) + "x"
                    vars()[x] = 535 + 49
                    y = "c" + str(mesto[0]) + "_" + str(mesto[1]) + "y"
                    vars()[y] = 155 + 49
                    player1 = False
                    player2 = True
                    polje21[0] = mesto[1]
                    polje21[1] = 1

                    pijunSelekcija = True
                    poljeSelekcija = True
                    mesto = [0, 0]
                    polje = [0, 0]

                elif polje == [2, 2]:
                    x = "c" + str(mesto[0]) + "_" + str(mesto[1]) + "x"
                    vars()[x] = 535 + 49
                    y = "c" + str(mesto[0]) + "_" + str(mesto[1]) + "y"
                    vars()[y] = 385 + 49
                    player1 = False
                    player2 = True
                    polje22[0] = mesto[1]
                    polje22[1] = 1

                    pijunSelekcija = True
                    poljeSelekcija = True
                    mesto = [0, 0]
                    polje = [0, 0]

                elif polje == [2, 3]:
                    x = "c" + str(mesto[0]) + "_" + str(mesto[1]) + "x"
                    vars()[x] = 535 + 49
                    y = "c" + str(mesto[0]) + "_" + str(mesto[1]) + "y"
                    vars()[y] = 615 + 49
                    player1 = False
                    player2 = True
                    polje23[0] = mesto[1]
                    polje23[1] = 1

                    pijunSelekcija = True
                    poljeSelekcija = True
                    mesto = [0, 0]
                    polje = [0, 0]

                elif polje == [3, 1]:
                    x = "c" + str(mesto[0]) + "_" + str(mesto[1]) + "x"
                    vars()[x] = 765 + 49
                    y = "c" + str(mesto[0]) + "_" + str(mesto[1]) + "y"
                    vars()[y] = 155 + 49
                    player1 = False
                    player2 = True
                    polje31[0] = mesto[1]
                    polje31[1] = 1

                    pijunSelekcija = True
                    poljeSelekcija = True
                    mesto = [0, 0]
                    polje = [0, 0]

                elif polje == [3, 2]:
                    x = "c" + str(mesto[0]) + "_" + str(mesto[1]) + "x"
                    vars()[x] = 765 + 49
                    y = "c" + str(mesto[0]) + "_" + str(mesto[1]) + "y"
                    vars()[y] = 385 + 49
                    player1 = False
                    player2 = True
                    polje32[0] = mesto[1]
                    polje32[1] = 1

                    pijunSelekcija = True
                    poljeSelekcija = True
                    mesto = [0, 0]
                    polje = [0, 0]

                elif polje == [3, 3]:
                    x = "c" + str(mesto[0]) + "_" + str(mesto[1]) + "x"
                    vars()[x] = 765 + 49
                    y = "c" + str(mesto[0]) + "_" + str(mesto[1]) + "y"
                    vars()[y] = 615 + 49
                    player1 = False
                    player2 = True
                    polje33[0] = mesto[1]
                    polje33[1] = 1

                    pijunSelekcija = True
                    poljeSelekcija = True
                    mesto = [0, 0]
                    polje = [0, 0]

    if player2:
        # MOUSE data
        mousePOS = pygame.mouse.get_pos()

        if pijunSelekcija:
            mesto = NadjiMestoPijuna(mousePOS)
        if mesto == [3, 1] and mesto in mestoSvihPijuna:
            screen.blit(selekcija2, (1008, 315))
        elif mesto == [3, 2] and mesto in mestoSvihPijuna:
            screen.blit(selekcija2, (1008, 485))
        elif mesto == [3, 3] and mesto in mestoSvihPijuna:
            screen.blit(selekcija2, (1008, 655))
        elif mesto == [4, 1] and mesto in mestoSvihPijuna:
            screen.blit(selekcija2, (1158, 315))
        elif mesto == [4, 2] and mesto in mestoSvihPijuna:
            screen.blit(selekcija2, (1158, 485))
        elif mesto == [4, 3] and mesto in mestoSvihPijuna:
            screen.blit(selekcija2, (1158, 655))

        if pijunSelekcija == False:
            # selekcija Polja
            if poljeSelekcija:
                polje = NadjiPolje(mousePOS)
                if polje == [1, 1] and mesto[1] > polje11[0]:
                    screen.blit(selekcija1, (305, 155))
                elif polje == [1, 2] and mesto[1] > polje12[0]:
                    screen.blit(selekcija1, (305, 385))
                elif polje == [1, 3] and mesto[1] > polje13[0]:
                    screen.blit(selekcija1, (305, 615))
                elif polje == [2, 1] and mesto[1] > polje21[0]:
                    screen.blit(selekcija1, (535, 155))
                elif polje == [2, 2] and mesto[1] > polje22[0]:
                    screen.blit(selekcija1, (535, 385))
                elif polje == [2, 3] and mesto[1] > polje23[0]:
                    screen.blit(selekcija1, (535, 615))
                elif polje == [3, 1] and mesto[1] > polje31[0]:
                    screen.blit(selekcija1, (765, 155))
                elif polje == [3, 2] and mesto[1] > polje32[0]:
                    screen.blit(selekcija1, (765, 385))
                elif polje == [3, 3] and mesto[1] > polje33[0]:
                    screen.blit(selekcija1, (765, 615))
            else:
                if polje == [1, 1]:
                    x = "p" + str(mesto[0]) + "_" + str(mesto[1]) + "x"
                    vars()[x] = 305 + 49
                    y = "p" + str(mesto[0]) + "_" + str(mesto[1]) + "y"
                    vars()[y] = 155 + 49
                    player2 = False
                    player1 = True
                    polje11[0] = mesto[1]
                    polje11[1] = 2

                    pijunSelekcija = True
                    poljeSelekcija = True
                    mesto = [0, 0]
                    polje = [0, 0]


                elif polje == [1, 2]:
                    x2 = "p" + str(mesto[0]) + "_" + str(mesto[1]) + "x"
                    vars()[x2] = 305 + 49
                    y2 = "p" + str(mesto[0]) + "_" + str(mesto[1]) + "y"
                    vars()[y2] = 385 + 49
                    player2 = False
                    player1 = True
                    polje12[0] = mesto[1]
                    polje12[1] = 2

                    pijunSelekcija = True
                    poljeSelekcija = True
                    mesto = [0, 0]
                    polje = [0, 0]

                elif polje == [1, 3]:
                    x = "p" + str(mesto[0]) + "_" + str(mesto[1]) + "x"
                    vars()[x] = 305 + 49
                    y = "p" + str(mesto[0]) + "_" + str(mesto[1]) + "y"
                    vars()[y] = 615 + 49
                    player2 = False
                    player1 = True
                    polje13[0] = mesto[1]
                    polje13[1] = 2

                    pijunSelekcija = True
                    poljeSelekcija = True
                    mesto = [0, 0]
                    polje = [0, 0]

                elif polje == [2, 1]:
                    x = "p" + str(mesto[0]) + "_" + str(mesto[1]) + "x"
                    vars()[x] = 535 + 49
                    y = "p" + str(mesto[0]) + "_" + str(mesto[1]) + "y"
                    vars()[y] = 155 + 49
                    player2 = False
                    player1 = True
                    polje21[0] = mesto[1]
                    polje21[1] = 2

                    pijunSelekcija = True
                    poljeSelekcija = True
                    mesto = [0, 0]
                    polje = [0, 0]

                elif polje == [2, 2]:
                    x = "p" + str(mesto[0]) + "_" + str(mesto[1]) + "x"
                    vars()[x] = 535 + 49
                    y = "p" + str(mesto[0]) + "_" + str(mesto[1]) + "y"
                    vars()[y] = 385 + 49
                    player2 = False
                    player1 = True
                    polje22[0] = mesto[1]
                    polje22[1] = 2

                    pijunSelekcija = True
                    poljeSelekcija = True
                    mesto = [0, 0]
                    polje = [0, 0]

                elif polje == [2, 3]:
                    x = "p" + str(mesto[0]) + "_" + str(mesto[1]) + "x"
                    vars()[x] = 535 + 49
                    y = "p" + str(mesto[0]) + "_" + str(mesto[1]) + "y"
                    vars()[y] = 615 + 49
                    player2 = False
                    player1 = True
                    polje23[0] = mesto[1]
                    polje23[1] = 2

                    pijunSelekcija = True
                    poljeSelekcija = True
                    mesto = [0, 0]
                    polje = [0, 0]

                elif polje == [3, 1]:
                    x = "p" + str(mesto[0]) + "_" + str(mesto[1]) + "x"
                    vars()[x] = 765 + 49
                    y = "p" + str(mesto[0]) + "_" + str(mesto[1]) + "y"
                    vars()[y] = 155 + 49
                    player2 = False
                    player1 = True
                    polje31[0] = mesto[1]
                    polje31[1] = 2

                    pijunSelekcija = True
                    poljeSelekcija = True
                    mesto = [0, 0]
                    polje = [0, 0]

                elif polje == [3, 2]:
                    x = "p" + str(mesto[0]) + "_" + str(mesto[1]) + "x"
                    vars()[x] = 765 + 49
                    y = "p" + str(mesto[0]) + "_" + str(mesto[1]) + "y"
                    vars()[y] = 385 + 49
                    player2 = False
                    player1 = True
                    polje32[0] = mesto[1]
                    polje32[1] = 2

                    pijunSelekcija = True
                    poljeSelekcija = True
                    mesto = [0, 0]
                    polje = [0, 0]

                elif polje == [3, 3]:
                    x = "p" + str(mesto[0]) + "_" + str(mesto[1]) + "x"
                    vars()[x] = 765 + 49
                    y = "p" + str(mesto[0]) + "_" + str(mesto[1]) + "y"
                    vars()[y] = 615 + 49
                    player2 = False
                    player1 = True
                    polje33[0] = mesto[1]
                    polje33[1] = 2

                    pijunSelekcija = True
                    poljeSelekcija = True
                    mesto = [0, 0]
                    polje = [0, 0]


    #KLIKOVI
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if player1:
                if ((mesto[0] == 1 or mesto[0] == 2) and mesto[1] != 0 and mesto in mestoSvihPijuna):
                    pijunSelekcija = False
                if pijunSelekcija == False:
                    if not (polje[0] == 0 or polje[1] == 0) and (mesto in mestoSvihPijuna) and (mesto[1] > vars()["polje"+str(polje[0])+str(polje[1])][0]):
                        poljeSelekcija = False
                        mestoSvihPijuna.remove(mesto)

            if player2:
                if ((mesto[0] == 3 or mesto[0] == 4) and mesto[1] != 0 and mesto in mestoSvihPijuna):
                    pijunSelekcija = False
                if pijunSelekcija == False:
                    if not (polje[0] == 0 or polje[1] == 0) and (mesto in mestoSvihPijuna) and (mesto[1] > vars()["polje"+str(polje[0])+str(polje[1])][0]):
                        poljeSelekcija = False
                        mestoSvihPijuna.remove(mesto)

    pygame.display.update()
pygame.quit()