import pygame, sys
pygame.init()


#since i cant put multiple text lines at once with indentations, i'll instead use images and put texts on it


White = (255,255,255)
Black = (0,0,0)
screenx = 1280
screeny = 1024


border = 1

print(pygame.font.match_font('impact'))
#print(pygame.font.get_fonts())

textfont = pygame.font.Font(r'C:\Windows\Fonts\georgia.ttf', 16 )
 
click = False
test = textfont.render("test", True, White)
screen = pygame.display.set_mode((screenx,screeny))
running = True





#procedural generation
#



def Spawn():
    enemy = "*"
    runtime = pygame.time.get_ticks()
    testspawn = "4"
    spawninterval = 4000
    if runtime > spawninterval:
        
        screen.blit(textfont.render(testspawn,True,Black),(200,200))
        runtime = 0
        
                    


    
    


# def EnemySpawn():
#     enemy = "*"
#     if runtime > 0:
#         screen.blit(textfont.render(enemy,True,Black))
                    


def grid():
    pygame.draw.rect(screen, Black, (0,0,1280,10))
    pygame.draw.rect(screen, Black, (0,0, 10,1280))
    pygame.draw.rect(screen, Black, (1270,0,10,1280))
    pygame.draw.rect(screen, Black, (0,1014, 1280,10))
    
    
    
    
  
def option():
    running = True
    while running:
        
        screen.fill(White)
        
        screen.blit(textfont.render("options",True, Black), (200,50))
        button3 = pygame.draw.rect(screen, Black,(100,100,50,50))
        screen.blit(test, (50,50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Did the user click the window close button?
                running = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
        pygame.display.update()
        


def game():
    running = True
    spawnx = 200
    spawny = 200
    
    while running:
        screen.fill(White)
        grid()
        pygame.draw.circle(screen, Black, (spawnx,spawny) ,34)
        Spawn()
        keypressed = pygame.key.get_pressed()
        #if keypressed[pygame.K_DOWN] and spawny < screeny:
         #   spawny += border
        if keypressed[pygame.K_LEFT] and spawnx > border:
            spawnx -= border
        if keypressed[pygame.K_RIGHT] and spawnx <  screenx :
            spawnx += border
        if keypressed[pygame.K_UP] and spawny > border:
            spawny -= border
       
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Did the user click the window close button?
                running = False
                sys.exit()
        
                    
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_DOWN:
            #         spawny += border #if ever the free movement doesnt seem to work, this is an example code that only allows one short movement with one click 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
        pygame.display.update()
        

while running:
    screen.fill(White) #the colour
    button1 = pygame.draw.rect(screen, Black,(50,50,50,50))
    
    screen.blit(textfont.render("Play", True, White), (50,50))
    mousex, mousey = pygame.mouse.get_pos()
    if button1.collidepoint(mousex,mousey):
        if click == True:
            game()
            click = False
    button2 = pygame.draw.rect(screen, Black,(100,100,100,50))
    screen.blit(textfont.render("Options", True, White), (100,100))
    if button2.collidepoint(mousex,mousey):
        if click == True:
            option()
            click = False
            
    

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Did the user click the window close button?
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
    pygame.display.update()