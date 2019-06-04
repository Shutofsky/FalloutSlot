background_1_filename = 'L1.JPG'
background_2_filename = 'L2.JPG'
background_3_filename = 'L3.JPG'
background_4_filename = 'W1.JPG'
background_5_filename = 'W2.JPG'
background_6_filename = 'W3.JPG'
background_slot_filename = 'slot.JPG'

import pygame, random, time, os
from pygame.locals import *

slot_pic = dict()
winner = dict()
sl = []
win = []
res = []
x_pos = [65, 320, 570]

win = [[[0,0,0]], \
       [[1,4,4], [2,4,4], [1,4,5], [2,4,5], [2,5,5], [2,4,6], [3,4,6], [3,5,6], [3,6,6]], \
       [[4,4,4], [1,5,5], [1,4,6], [1,5,6], [2,5,6], [2,6,6]], \
       [[5,5,5], [1,6,6]], \
       [[6,6,6]]]

def game(screen):

    font1 = pygame.font.Font(os.path.join("Disney.TTF"),36)
    font2 = pygame.font.Font(os.path.join("Disney.TTF"),72)
    font3 = pygame.font.Font(os.path.join("Disney.TTF"),24)
    font4 = pygame.font.Font(os.path.join("Disney.TTF"),60)
    font5 = pygame.font.Font(os.path.join("Smiley.TTF"),60)
    font6 = pygame.font.Font(os.path.join("VeraMoBI.TTF"),24)

    winner[0] = font2.render("LOSE ", True, (0,0,0))
    winner[1] = font2.render("WIN X 1", True, (0, 0, 0))
    winner[2] = font2.render("WIN X 2", True, (0, 0, 0))
    winner[3] = font2.render("WIN X 3", True, (0, 0, 0))
    winner[4] = font2.render("WIN X 4", True, (0, 0, 0))

    odds1 = font6.render(" ODDS TO GET ALL 3 SLOTS IS 4%", True,(0,0,0))
    odds2 = font6.render(" ODDS TO GET AT LEAST 2 SLOTS IS 48%", True , (0,0,0))
        
    image = pygame.Surface((50,50))
    image.fill((255,255,255))
    pygame.draw.circle(image,(0,0,0),(15,15),12)

    slot_pic[1] = pygame.image.load(background_1_filename).convert()
    slot_pic[2] = pygame.image.load(background_2_filename).convert()
    slot_pic[3] = pygame.image.load(background_3_filename).convert()
    slot_pic[4] = pygame.image.load(background_4_filename).convert()
    slot_pic[5] = pygame.image.load(background_5_filename).convert()
    slot_pic[6] = pygame.image.load(background_6_filename).convert()

    slot1 = pygame.image.load(background_slot_filename).convert()
    slot2 = pygame.image.load(background_slot_filename).convert()
    slot3 = pygame.image.load(background_slot_filename).convert()
    
    pos = 1
    
    optiona = font5.render("VAULT-BOY SLOT-MACHINE ", True, (0, 0, 0))
    optionb = font6.render("use the up and down arrow keys and enter",True,(0,0,0))
    play = font5.render("PLAY" , True,(0,0,0))
    quit = font5.render("QUIT" , True,(0,0,0))  
    
    screen.fill((255,255,255))
    screen.blit(optiona,(40,20))

    screen.blit(slot_pic[1], (10, 80))
    screen.blit(slot_pic[2], (160, 160))
    screen.blit(slot_pic[3], (310, 240))
    screen.blit(slot_pic[4], (460, 320))

    pygame.display.update()
    pygame.time.delay(2000)
           
    while 1:
        screen.fill((255,255,255))
        screen.blit(optiona,(40,20))
        screen.blit(optionb,(110,100))
        screen.blit(play,(350,180))
        screen.blit(quit,(350,380))
        screen.blit(image,(300,pos*200))

        for event in pygame.event.get():
           if event.type == QUIT:
               exit()
               
           elif event.type == KEYDOWN:
            
               if event.key == K_ESCAPE:
                     exit()
               
               elif event.key == K_DOWN:
                  pos += 1
                  if pos > 2: pos = 1
               elif event.key == K_UP:
                    pos -= 1
                    if pos < 1: pos = 2
                    
               elif event.key == K_RETURN:
                
                    if pos == 2.:  
                       exit()
                
                    if pos == 1.:
                            screen.fill((255,255,255))
                            screen.blit(slot1,(50,40))
                            screen.blit(slot2,(300,40))
                            screen.blit(slot3,(550,40))
                            pygame.display.update()
                            pygame.time.delay(600)

                    sl=[]

                    for i in (1, 2, 3):
                        tr = random.randint(1, 6)
                        sl.insert(i, tr)
#                        print("Sl[", i-1, "] = ", tr)
                        j = 0
                        j_end = random.randint(5, 20)
                        while j < j_end:
                            screen.blit(slot_pic[random.randint(1,6)], (x_pos[i - 1], 100))
                            pygame.display.update()
                            pygame.time.delay(100+j*10)
                            j+=1

                        screen.blit(slot_pic[tr], (x_pos[i - 1], 100))
                        pygame.display.update()
                        pygame.time.delay(600)

                    w_l = 0
                    for i in (1, 2, 3, 4):
                        for l in win[i]:
                            res = list(set(sl) ^ set(l))
#                            print("L=", l, " SL=", sl, " I=",i," Res=",res," L=",len(res))
                            if len(res) == 0:
                                w_l = i
                                break
                        if w_l != 0:
                            break

#                    print(w_l)
                    screen.blit(winner[w_l], (200,480))
                    pygame.display.update()
                    pygame.time.delay(5000)

        pygame.time.delay(50)                                
        pygame.display.update()                 
                    








