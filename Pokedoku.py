from pygame import *
import sys, random

tablero = [
            [7, 8, -1, 4, -1, -1, 1, 2, -1],
            [6, -1, -1, -1, 7, 5, -1, -1, 9],
            [-1, -1, -1, 6, -1, 1, -1, 7, 8],
            [-1, -1, 7, -1, 4, -1, 2, 6, -1],
            [-1, -1, 1, -1, 5, -1, 9, 3, -1],
            [9, -1, 4, -1, 6, -1, -1, -1, 5],
            [-1, 7, -1, 3, -1, -1, -1, 1, 2],
            [1, 2, -1, -1, -1, 7, 4, -1, -1],
            [-1, 4, 9, 2, -1, 6, -1, -1, 7]
          ]

init() 
screen = display.set_mode((1200,1000)) 
font = font.SysFont("Calibri", 40)
musica = mixer.Sound("Ship.ogg")
activo = 0 
personaje = 0
seleccion = -1

def Repetido(tab, f, c, sel):
    for vert in range(0, len(tablero)):
        if tab[vert][c] == sel: return True
    for hor in range(0, len(tablero[0])):
        if tab[f][hor] == sel: return True
    return False

def InSeccion(tab,cFil, cCol, sel):
    for f in range(cFil*3, (cFil+1)*3): 
        for c in range(cCol*3, (cCol+1)*3):
            if tab[f][c] == sel: return True
    return False
  

def Inicio(escena):
    background = transform.scale(image.load("lab.png"), (1200,1000))
    musica.play(loops=-1)
    musica.set_volume(0.9)
    while True:
        screen.fill((255,255,255))   
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == KEYDOWN and e.key == K_p: return 2            
        screen.blit(background, (0,0))
        hello = font.render("Presiona P para elegir tu personaje", True, (250,0,250)) 
        screen.blit(hello, (300, 500))
        display.flip()

def Seleccion(escena):
    global activo, personaje
    lab = image.load("lab.png")
    lab = transform.scale(lab, (1200,1000))
    squirtle = image.load("Squirtle.png")
    squirtle = transform.scale(squirtle, (100,400))
    bulbasaur = image.load("Bulbasaur.png")
    bulbasaur = transform.scale(bulbasaur, (150,400))
    charmander = image.load("Charmander.png")
    charmander = transform.scale(charmander, (100,400))
    while True:
        screen.fill((255,255,255))   
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == KEYDOWN and e.key == K_d: activo = (activo + 1) % 3
            if e.type == KEYDOWN and e.key == K_a: activo = (activo - 1) % 3
            if e.type == KEYDOWN and e.key == K_j: return 3
        screen.blit(lab, (0,0))
        if activo==0:
            screen.blit(squirtle, (100,300))
            personaje=squirtle
            hello = font.render("Squirtle", True, (0,0,250)) 
            screen.blit(hello, (80, 300))
        if activo==1:
            screen.blit(bulbasaur, (520,300))
            personaje=bulbasaur
            hello = font.render("Bulbasaur", True, (0,200,0)) 
            screen.blit(hello, (510, 300))
        if activo==2:
            screen.blit(charmander, (1000,300))
            personaje=charmander
            hello = font.render("Charmander", True, (250,0,0)) 
            screen.blit(hello, (960, 300))
        hello = font.render("Presiona A o D para elegir", True, (250,0,250)) 
        screen.blit(hello, (400, 750))
        hello2 = font.render("Presiona J para jugar", True, (250,0,250)) 
        screen.blit(hello2, (450, 800))
        display.flip()

def Sudoku(escena):
    global seleccion
    background = transform.scale(image.load("lab.png"), (1200,1000))
    colores = transform.scale(image.load("Colores.png"), (900,900))
    blanco = transform.scale(image.load("blanco.png"), (50,450))
    while True:
        screen.fill((255,255,255))
        screen.blit(background, (0,0))
        screen.blit(personaje, (1000,600))
        screen.blit(colores, (0,0))
        screen.blit(blanco, (1100,50))
        for e in event.get():
            if e.type == KEYDOWN and e.key == K_q: return quit()
            if e.type == QUIT: sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                x, y = mouse.get_pos()
                if Rect(1100,50,50,450).collidepoint((x,y)):
                    seleccion = y//50
                    print(seleccion)
                if Rect(0,0,900,900).collidepoint((x,y)):
                    fila, col = y//100, x//100
                    cuadranteCol = col//3
                    cuadranteFil = fila//3
                    print("Cuadrantes", cuadranteFil, cuadranteCol)
                    if not Repetido(tablero, fila, col, seleccion) and not InSeccion(tablero,cuadranteFil, cuadranteCol, seleccion): 
                        tablero[fila][col] = seleccion
                        print(fila, col)
                    else: print("Error")
        for fila in range(len(tablero)):
            for col in range(len(tablero[fila])):                      
                draw.rect(screen, (0,0,0), (col*100,fila*100,100,100), 3)
                if tablero[fila][col] != -1:
                    texto = font.render(str(tablero[fila][col]), True, (0,0,0)) 
                    screen.blit(texto, (col*100+20,fila*100))
        for num in range(1,10):
            texto = font.render(str(num), True, (0,0,0))
            if num==seleccion:
                draw.rect(screen, (0,200,200), (1100,num*50,50,50), 0)
            else:
                draw.rect(screen, (0,0,0), (1100,num*50,50,50), 2)
            screen.blit(texto, (1100,num*50))
        hello = font.render("Presiona Q para salir del juego", True, (250,0,250)) 
        screen.blit(hello, (350, 900))
        display.flip()

        

escena = 1 
while True:
    if escena==1:
        escena = Inicio(escena)
    elif escena==2:
        escena = Seleccion(escena)
    elif escena==3:
        escena = Sudoku(escena)