import pygame
import random
pygame.init()
pygame.font.init()

screenSize = [300, 500]
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

nonePng = pygame.image.load("texture\\none.png")
crossPng = pygame.image.load("texture\\cross.png")
circlePng = pygame.image.load("texture\\circle.png")
twoPersonIconPng = pygame.transform.rotozoom(pygame.image.load('texture\\twopersonicon.png'), 0, 1/8)
robotIconImg = pygame.transform.rotozoom(pygame.image.load('texture\\robotIcon.png'), 0, 1/30)
font = pygame.font.Font('Oswald-VariableFont_wght.ttf', 25)
retDotImg = pygame.image.load("texture\\redDot.png")
skresleniePrawoImg = pygame.image.load('texture\skresleniePrawo.png').convert_alpha()
skreslenieLewoImg = pygame.image.load('texture\skreslenieLewo.png').convert_alpha()

tryb_dwoch_graczy = True
tura = "cross"
class Guzik:
    def __init__(self, x, y, stan = 'none') -> None:
        self.x = x
        self.y = y
        self.stan = stan
        self.kolumna = int((self.x/100) + 1)
        self.rzad = int((self.y - 100)/100 + 1)
        self.img = nonePng

    def draw(self):
        if self.stan == 'none':
            self.img = nonePng
        elif self.stan == 'cross':
            self.img = crossPng
        elif self.stan == 'circle':
            self.img = circlePng
        screen.blit(self.img, (self.x, self.y))

    def isClicked(self):
        mousePosition = pygame.mouse.get_pos()
        mouseX = mousePosition[0]
        mouseY = mousePosition[1]
        
        if mouseX > self.x and mouseX < self.x + 100 and mouseY > self.y and mouseY < self.y + 100:
            #print(self.kolumna, self.rzad)
            return True

def text_u_gory(tryb):
    if tryb == True:
        nazwa_trybu = font.render("Tryb dwu osobowy", True,(255,255,255))
    else:
        nazwa_trybu = font.render("Przeciwko AI", True,(255,255,255))
    return nazwa_trybu

guziki = []
for y in range(3):
    for x in range(3):
        guziki.append(Guzik(x*100, y*100+100))

def dwoch_graczy():
    global tura
    if tura == "cross":
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(230, 10, 50, 50))
    if tura == "circle":
        pygame.draw.circle(screen, (255, 255, 255), (255, 35), 30)

def sprawdzenie_wygranek():
    #poziom
    if guziki[0].stan == guziki[1].stan and guziki[2].stan == guziki[1].stan and guziki[0].stan != "none":
        wygrana(guziki[0].stan,1)
    if guziki[3].stan == guziki[4].stan and guziki[5].stan == guziki[4].stan and guziki[3].stan != "none":
        wygrana(guziki[3].stan,2)
    if guziki[6].stan == guziki[7].stan and guziki[8].stan == guziki[7].stan and guziki[8].stan != "none":
        wygrana(guziki[8].stan,3)
    #pion
    if guziki[0].stan == guziki[3].stan and guziki[6].stan == guziki[3].stan and guziki[6].stan != "none":
        wygrana(guziki[0].stan, 4)
    if guziki[1].stan == guziki[4].stan and guziki[7].stan == guziki[4].stan and guziki[7].stan != "none":
        wygrana(guziki[1].stan,5)
    if guziki[2].stan == guziki[5].stan and guziki[8].stan == guziki[5].stan and guziki[8].stan != "none":
        wygrana(guziki[2].stan,6)
    #ukos
    if guziki[0].stan == guziki[4].stan and guziki[8].stan == guziki[4].stan and guziki[4].stan != "none":
        wygrana(guziki[0].stan,7)
    if guziki[2].stan == guziki[4].stan and guziki[6].stan == guziki[4].stan and guziki[4].stan != "none":
        wygrana(guziki[2].stan,8)

def wygrana(wygrany, miejsce_wygranej):
    kreska.opcja = miejsce_wygranej
    czy_tak = True
    if wygrany == 'cross':
        napis_wygrany = font.render("Wygrał kwadrat", True,(255,255,255))
    elif wygrany == "circle":
        napis_wygrany = font.render("Wygrało koło", True,(255,255,255))
    elif wygrany == "remis":
        napis_wygrany = font.render("Remis", True,(255,255,255))
    press_r_napis = font.render("(Naciśnij R by zrestartować)", True,(255,255,255))
    screen.blit(napis_wygrany, (10,30))
    screen.blit(press_r_napis, (10,60))

    while czy_tak:
        global tura
        global tryb_dwoch_graczy
        kreska.draw()
        key = pygame.key.get_pressed()
        if key[pygame.K_r] == True:
            for guzik in guziki:
                guzik.stan = 'none'
            tura = "cross"
            czy_tak = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    for przycisk in guziki_nawigacyjne:
                        
                        if przycisk.is_clicked() == "si" and tryb_dwoch_graczy == True:
                            for guzik in guziki:
                                guzik.stan = 'none'
                            tura = "cross"
                            tryb_dwoch_graczy = False
                            
                            tura = "cross"
                            czy_tak = False
                        if przycisk.is_clicked() == "dwochgraczy" and tryb_dwoch_graczy == False:
                            for guzik in guziki:
                                guzik.stan = 'none'
                            tura = "cross"
                            tryb_dwoch_graczy = True
                            tura = "cross"
                            czy_tak = False
        pygame.display.flip()
        
        for guzik in guziki:
            guzik.draw()
        for guzik in guziki_nawigacyjne:
            guzik.draw()
            
        clock.tick(60)
def SI(ruch):
    pola = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(len(guziki)):
        if guziki[x].stan == 'none':
            pola[x] = 0
        elif guziki[x].stan == 'circle':
            pola[x] = 1
        elif guziki[x].stan == 'cross':
            pola[x] = 2
    
    #Atak
    #poziom
    if ruch == True:
        if pola[:3].count(1) == 2 and ruch == True and pola[:3].count(0) == 1 and ruch == True:
            guziki[pola[:3].index(0)].stan = 'circle'
            ruch = False
        if pola[3:6].count(1) == 2 and ruch == True and pola[3:6].count(0) == 1 and ruch == True:
            guziki[pola[3:6].index(0)+ 3].stan = 'circle'
            ruch = False
        if pola[6:9].count(1) == 2 and ruch == True and pola[6:9].count(0) == 1 and ruch == True:
            guziki[pola[6:9].index(0) + 6].stan = 'circle'
            ruch = False
    
    #pion
    if ruch == True:
        if (pola[0], pola[3], pola[6]).count(1) == 2 and (pola[0], pola[3], pola[6]).count(0) == 1 and ruch == True:
            if pola[0] == 0:
                guziki[0].stan = 'circle'
                ruch = False
            if pola[3] == 0:
                guziki[3].stan = 'circle'
                ruch = False
            if pola[6] == 0:
                guziki[6].stan = 'circle'
                ruch = False
        

        if (pola[1], pola[4], pola[7]).count(1) == 2 and (pola[1], pola[4], pola[7]).count(0) == 1 and ruch == True:
            if pola[1] == 0:
                guziki[1].stan = 'circle'
                ruch = False
            if pola[4] == 0:
                guziki[4].stan = 'circle'
                ruch = False
            if pola[7] == 0:
                guziki[7].stan = 'circle'
                ruch = False
        
        
        if (pola[2], pola[5], pola[8]).count(1) == 2 and (pola[2], pola[5], pola[8]).count(0) == 1 and ruch == True:
            if pola[2] == 0:
                guziki[2].stan = 'circle'
                ruch = False
            if pola[5] == 0:
                guziki[5].stan = 'circle'
                ruch = False
            if pola[8] == 0:
                guziki[8].stan = 'circle'
                ruch = False
        
    #ukos
    if (pola[0], pola[4], pola[8]).count(1) == 2 and (pola[0], pola[4], pola[8]).count(0) == 1 and ruch == True:
        if pola[0] == 0:
            guziki[0].stan = 'circle'
            ruch = False
        if pola[4] == 0:
            guziki[4].stan = 'circle'
            ruch = False
        if pola[8] == 0:
            guziki[8].stan = 'circle'
            ruch = False

    if (pola[2], pola[4], pola[6]).count(1) == 2 and (pola[2], pola[4], pola[6]).count(0) == 1 and ruch == True:
        if pola[2] == 0:
            guziki[2].stan = 'circle'
            ruch = False
        if pola[4] == 0:
            guziki[4].stan = 'circle'
            ruch = False
        if pola[6] == 0:
            guziki[6].stan = 'circle'
            ruch = False

    #Obrona
    #poziom
    if ruch == True:
        if pola[:3].count(2) == 2 and ruch == True and pola[:3].count(0) == 1:
            guziki[pola[:3].index(0)].stan = 'circle'
            ruch = False
        if pola[3:6].count(2) == 2 and ruch == True and pola[3:6].count(0) == 1:
            guziki[pola[3:6].index(0)+ 3].stan = 'circle'
            ruch = False
        if pola[6:9].count(2) == 2 and ruch == True and pola[6:9].count(0) == 1:
            guziki[pola[6:9].index(0) + 6].stan = 'circle'
            ruch = False
    
    #pion
    if ruch == True:
        if (pola[0], pola[3], pola[6]).count(2) == 2 and (pola[0], pola[3], pola[6]).count(0) == 1 and ruch == True:
            if pola[0] == 0:
                guziki[0].stan = 'circle'
                ruch = False
            if pola[3] == 0:
                guziki[3].stan = 'circle'
                ruch = False
            if pola[6] == 0:
                guziki[6].stan = 'circle'
                ruch = False
        

        if (pola[1], pola[4], pola[7]).count(2) == 2 and (pola[1], pola[4], pola[7]).count(0) == 1 and ruch == True:
            if pola[1] == 0:
                guziki[1].stan = 'circle'
                ruch = False
            if pola[4] == 0:
                guziki[4].stan = 'circle'
                ruch = False
            if pola[7] == 0:
                guziki[7].stan = 'circle'
                ruch = False
        
        
        if (pola[2], pola[5], pola[8]).count(2) == 2 and (pola[2], pola[5], pola[8]).count(0) == 1 and ruch == True:
            if pola[2] == 0:
                guziki[2].stan = 'circle'
                ruch = False
            if pola[5] == 0:
                guziki[5].stan = 'circle'
                ruch = False
            if pola[8] == 0:
                guziki[8].stan = 'circle'
                ruch = False
        
    #ukos
    if (pola[0], pola[4], pola[8]).count(2) == 2 and (pola[0], pola[4], pola[8]).count(0) == 1 and ruch == True:
        if pola[0] == 0:
            guziki[0].stan = 'circle'
            ruch = False
        if pola[4] == 0:
            guziki[4].stan = 'circle'
            ruch = False
        if pola[8] == 0:
            guziki[8].stan = 'circle'
            ruch = False

    if (pola[2], pola[4], pola[6]).count(2) == 2 and (pola[2], pola[4], pola[6]).count(0) == 1 and ruch == True:
        if pola[2] == 0:
            guziki[2].stan = 'circle'
            ruch = False
        if pola[4] == 0:
            guziki[4].stan = 'circle'
            ruch = False
        if pola[6] == 0:
            guziki[6].stan = 'circle'
            ruch = False
    
    #Sprawdzenie środka
    if pola[4] == 0 and ruch == True:
        guziki[4].stan = 'circle'
        ruch = False
    
    #Danie do jednego
    #poziom
    if ruch == True:
        if pola[:3].count(1) == 1 and ruch == True and pola[:3].count(0) == 2 and ruch == True:
            while True:
                los = random.randint(0,2)
                if pola[los] == 0:
                    guziki[los].stan = 'circle'
                    ruch = False
                    break

            
        if pola[3:6].count(1) == 1 and ruch == True and pola[3:6].count(0) == 2 and ruch == True:
            while True:
                los = random.randint(3,5)
                if pola[los] == 0:
                    guziki[los].stan = 'circle'
                    ruch = False
                    break
        if pola[6:9].count(1) == 1 and ruch == True and pola[6:9].count(0) == 2 and ruch == True:
            while True:
                los = random.randint(6,8)
                if pola[los] == 0:
                    guziki[los].stan = 'circle'
                    ruch = False
                    break
    
    #pion
    if ruch == True:
        if (pola[0], pola[3], pola[6]).count(1) == 1 and (pola[0], pola[3], pola[6]).count(0) == 2 and ruch == True:
            while True:
                los = random.randint(1,3)
                if los == 1 and pola[0] == 0:
                    guziki[0].stan = 'circle'
                    ruch = False
                    break
                if los == 2 and pola[3] == 0:
                    guziki[3].stan = 'circle'
                    ruch = False
                    break
                if los == 3 and pola[6] == 0:
                    guziki[6].stan = 'circle'
                    ruch = False
                    break
      
        if (pola[1], pola[4], pola[7]).count(1) == 1 and (pola[1], pola[4], pola[7]).count(0) == 2 and ruch == True:
            while True:
                los = random.randint(1,3)
                if los == 1 and pola[1] == 0:
                    guziki[1].stan = 'circle'
                    ruch = False
                    break
                if los == 2 and pola[4] == 0:
                    guziki[4].stan = 'circle'
                    ruch = False
                    break
                if los == 3 and pola[7] == 0:
                    guziki[7].stan = 'circle'
                    ruch = False
                    break
        
        
        if (pola[2], pola[5], pola[8]).count(1) == 1 and (pola[2], pola[5], pola[8]).count(0) == 2 and ruch == True:
            while True:
                los = random.randint(1,3)
                if los == 1 and pola[2] == 0:
                    guziki[2].stan = 'circle'
                    ruch = False
                    break
                if los == 2 and pola[5] == 0:
                    guziki[5].stan = 'circle'
                    ruch = False
                    break
                if los == 3 and pola[8] == 0:
                    guziki[8].stan = 'circle'
                    ruch = False
                    break
        
    #ukos
    if (pola[0], pola[4], pola[8]).count(1) == 1 and (pola[0], pola[4], pola[8]).count(0) == 2 and ruch == True:
        while True:
            los = random.randint(1,3)
            if los == 1 and pola[0] == 0:
                guziki[0].stan = 'circle'
                ruch = False
                break
            if los == 2 and pola[4] == 0:
                guziki[4].stan = 'circle'
                ruch = False
                break
            if los == 3 and pola[8] == 0:
                guziki[8].stan = 'circle'
                ruch = False
                break

    if (pola[2], pola[4], pola[6]).count(1) == 2 and (pola[2], pola[4], pola[6]).count(0) == 1 and ruch == True:
        while True:
                los = random.randint(1,3)
                if los == 1 and pola[2] == 0:
                    guziki[2].stan = 'circle'
                    ruch = False
                    break
                if los == 2 and pola[4] == 0:
                    guziki[4].stan = 'circle'
                    ruch = False
                    break
                if los == 3 and pola[6] == 0:
                    guziki[6].stan = 'circle'
                    ruch = False
                    break

    #Pozostałe
    if ruch == True:
        jakie_zostały = []
        for x in range(len(guziki)):
            if guziki[x].stan == 'none':
                jakie_zostały.append(x)
        if len(jakie_zostały) > 0:
            los = random.randint(0, len(jakie_zostały))
            guziki[los].stan = 'circle'
            ruch = False

    for x in range(len(guziki)):
         if guziki[x].stan == 'none':
             pola[x] = 0
         elif guziki[x].stan == 'circle':
             pola[x] = 1
         elif guziki[x].stan == 'cross':
             pola[x] = 2
    if ruch == False:
        global tura
        tura = 'cross'
    
class GuzikiWyboru:
    def __init__(self, x, y, img, znaczenie) -> None:
        self.x = x
        self.y = y
        self.img = img
        self.znaczenie = znaczenie
    def draw(self):
        pygame.draw.rect(screen, (255, 255,200), pygame.Rect(self.x, self.y, 130, 80))
        screen.blit(self.img, (self.x + 33,self.y+10))
    def is_clicked(self):
        mousePosition = pygame.mouse.get_pos()
        mouseX = mousePosition[0]
        mouseY = mousePosition[1]
        
        if mouseX > self.x and mouseX < self.x + 130 and mouseY > self.y and mouseY < self.y + 80:
            return self.znaczenie
guziki_nawigacyjne = [GuzikiWyboru(10,410,twoPersonIconPng, "dwochgraczy"), GuzikiWyboru(160,410, robotIconImg, "si")]

class Kreska:
    def __init__(self):
        self.opcja = 0

    def draw(self):
        if self.opcja == 1:
            pygame.draw.rect(screen, (255, 0,0), pygame.Rect(0, 145, 300, 10))
        if self.opcja == 2:
            pygame.draw.rect(screen, (255, 0,0), pygame.Rect(0, 245, 300, 10))
        if self.opcja == 3:
            pygame.draw.rect(screen, (255, 0,0), pygame.Rect(0, 345, 300, 10))
        if self.opcja == 4:
            pygame.draw.rect(screen, (255, 0,0), pygame.Rect(45, 100, 10, 300))
        if self.opcja == 5:
            pygame.draw.rect(screen, (255, 0,0), pygame.Rect(145, 100, 10, 300))
        if self.opcja == 6:
            pygame.draw.rect(screen, (255, 0,0), pygame.Rect(245, 100, 10, 300))
        #skos
        if self.opcja == 7:
            screen.blit(skresleniePrawoImg, (0,100))
        if self.opcja == 8:
            screen.blit(skreslenieLewoImg, (0,100))
            
kreska = Kreska() 
while True:
    screen.fill("black")
    screen.blit(text_u_gory(tryb_dwoch_graczy), (10,0))
    dwoch_graczy()
    sprawdzenie_wygranek()
    czy_wszystkie = True
    for guzik in guziki:
        guzik.draw()  
        if guzik.stan == "none":
            czy_wszystkie = False  
    if czy_wszystkie == True:
        wygrana("remis")
    for guzik in guziki_nawigacyjne:
        guzik.draw()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                for guzik in guziki:
                    if tura == 'cross' and guzik.isClicked() == True and guzik.stan == 'none':
                        guzik.stan = 'cross'
                        tura = "circle"

                    if tura == 'circle' and guzik.isClicked() == True and tryb_dwoch_graczy == True and guzik.stan == 'none':
                        guzik.stan = 'circle'
                        tura = "cross"
                    sprawdzenie_wygranek()
                    if tura == 'circle' and tryb_dwoch_graczy == False: #Dla SI
                        SI(True)

                for przycisk in guziki_nawigacyjne:
                    if przycisk.is_clicked() == "si" and tryb_dwoch_graczy == True:
                        for guzik in guziki:
                            guzik.stan = 'none'
                        tura = "cross"
                        tryb_dwoch_graczy = False
                    if przycisk.is_clicked() == "dwochgraczy" and tryb_dwoch_graczy == False:
                        for guzik in guziki:
                            guzik.stan = 'none'
                        tura = "cross"
                        tryb_dwoch_graczy = True
        key = pygame.key.get_pressed()
        if key[pygame.K_r] == True:
            for guzik in guziki:
                guzik.stan = 'none' 
            tura = 'cross' 
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
    clock.tick(60)
