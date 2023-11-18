import pygame as pg #Importar la libreria de pygame 
from button import Button #Importar la clase Button del otro modulo
from random import randrange #Importar la libreria ramdom para numeros aleatorios

#Inciar los componetes de la libreria para el audio y la fuente de texto
pg.init()

#Funcion para dibujar texto en pantalla
def render_text(text, color, x, y, font, screen):
    img = font.render(text, True, color) # Convierte el texto a imagen con el color pasasdo en el parametro
    
    #Modifica la posicion del texto en la pantalla
    rect = img.get_rect()
    rect.centerx = x
    rect.centery = y
    screen.blit(img, rect)
   
#Funcion principal que hara correr el proyecto
def main():
    SCREEN_SIZE = (550, 550) #Tamaño de la ventana
    pg.display.set_caption("Love Game") #Titulo de la ventana
    icon = pg.image.load("./src/images/icon.png") #Ruta de la imagen del icono
    pg.display.set_icon(icon) #Icono de la ventana 
    screen = pg.display.set_mode(SCREEN_SIZE) #Creamos la ventana
    font = pg.font.SysFont('inkfree', 32, italic = True, bold = True) #Cargamos una fuente por defecto del sistema
    
    pg.mixer.music.load("./src/music/background.mp3") #Ruta de la musica de fondo
    pg.mixer.music.play() #Reproduce la musica de fondo
    
    #Cargamos todas las imagenes
    win_image = pg.image.load("./src/images/win_image.png") #Imagen de la ventana ganadora
    background_image = pg.image.load("./src/images/background.jpg") #Imagen de fondo
    
    #Obtenemos las propiedades de ls posiciones de las imagenes para modificar
    rect_win_image = win_image.get_rect() 
    rect_background_image = background_image.get_rect()
    
    #Centramos las imagenes 
    rect_win_image.centerx = SCREEN_SIZE[0] //2
    rect_win_image.centery = SCREEN_SIZE[1] //2
    
    rect_background_image.centerx = SCREEN_SIZE[0] //2
    rect_background_image.centery = SCREEN_SIZE[1] //2
    
    #variables para saber si ganamos o no y saber que ventana mostrar
    run = True #Mantiene el juego en funcionamiento si es Falso, se cierra el juego
    won = False 
    fps = pg.time.Clock() #Variable para establecer la tasa de fotogramas a 60
    
    #Creamos 2 instancias de la clase Button
    btn_yes = Button("yes", SCREEN_SIZE, -1, 1)
    btn_no = Button("no", SCREEN_SIZE, 1, 1) 
    
    #Bucle principal
    while run:
        fps.tick(60)
        
        #Aqui capturamos si el usuario presiona la cruz de la ventana para deneter el juego
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        #Logica del juego
        mouse_pos = pg.mouse.get_pos() #Obtenemos la posicion del mause en todo momento
        mouse_click = pg.mouse.get_pressed() #Capturamos cuando hace click en alguna parte de la pantalla
        
        #Le damos posiciones randoms al botton "No"
        x = randrange(0, SCREEN_SIZE[0] - btn_no.rect.width)
        y = randrange(0, SCREEN_SIZE[1] - btn_no.rect.height)
        
        #Comprobamos si la posicion del mause coincide con la posicion del boton "No"
        if btn_no.check_event(mouse_pos):    
            #En caso de que si sean iguales le damos una nueva posicion aleatoria
            btn_no.rect.x = x
            btn_no.rect.y = y
        
        #Comprobamos si da click al boton de "Si"
        if btn_yes.check_event(mouse_pos) and mouse_click[0]:
            pg.mixer.music.stop() #Pausa la musica de fondo
            pg.mixer.music.load("./src/music/accept_music.mp3") #Carga la musica de fondo de cuando ganemos
            pg.mixer.music.play() #Reproduce la musica para cuando acepte
            won = True #Cambaimos la variable para cambiar la ventana 
        
        #Comprobamos si hace click en cualquier parte de la pantalla y no sea en el boton "Si" y que tampoco halla ganado    
        if not btn_yes.check_event(mouse_pos) and mouse_click[0] and not won:
            wrong_click = pg.mixer.Sound("./src/music/wrong_click.mp3") #Cargamos el sonido de click incorrecto
            wrong_click.play() #Reproduce el sonido
                   
        #DIbujar los elementos en la pantalla (Imagenes, texto, botones)
        if not won: #Mientras no hemos ganado se muestra la ventana principal
            screen.fill(pg.Color("white")) 
            screen.blit(background_image, (rect_background_image.x, rect_background_image.y)) #Se carga la imagen
            #Se dibujan los botones
            btn_yes.draw(screen)
            btn_no.draw(screen)    
            #Se dibuja el texto (Quieres ser mi novia)        
            render_text("¿You wanna be my girlfriend :)?", pg.Color("red"),SCREEN_SIZE[0] //2, 50, font, screen)
            
        #Si gana cambiamos la pantalla con la otra imagen y dibujamos el otro texto
        if won:
            screen.fill(pg.Color("white"))
            render_text("Always i knew it :3", pg.Color("red"),SCREEN_SIZE[0] //2, 50, font, screen)
            screen.blit(win_image, (rect_win_image.x, rect_win_image.y))
        
        #Actualiza los cuadros de la ventana
        pg.display.update()

    pg.quit()

#Corre la funcion principal
if __name__ == "__main__":
    main()