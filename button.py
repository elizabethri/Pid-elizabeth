import pygame as pg

#Clase para crear los botones
class Button:
    def __init__(self, image:pg.Surface, screen_size:tuple, direction_x:int, direction_y:int):
        self.image = pg.image.load(f"./src/images/{image}.png") #Pide la ruta de la imagen
        self.btn_size = self.image.get_size() #Pide el tamaño de la imagen
        self.rect = self.image.get_rect() #Obtenemos las posiciones para modificarlas 
        self.direction_x = direction_x # -1 or 1
        self.direction_y = direction_y # -1 or 1
        self.screen_size = screen_size
        self.position()
    
    #Funcion para darle posicion a los botones
    def position(self):
        #Obtenemos el centro de la pantalla para obtener referencias 
        center_x = (self.screen_size[0] /2) - (self.btn_size[0] /2)
        center_y = (self.screen_size[1] /2) - (self.btn_size[1] /2)
        
        self.rect.x = 0
        self.rect.y = 0

        #Posiciones acuerdo a las direcciones Izquierda -1 o Derecha 1        
        if self.direction_x == 1:
            self.rect.x = center_x + self.btn_size[0] *2
            
        if self.direction_x == -1:
            self.rect.x = center_x - self.btn_size[0] *2
            
        if self.direction_y == 1:
            self.rect.y = center_y + self.btn_size[1] * 2
            
        if self.direction_y == -1:
            self.rect.y = center_y - self.btn_size[1] * 2
    
        #Retorna las pocisiones
        return (self.rect.x, self.rect.y)
    
    #Comprobamos si se hace click en algun boton para devolver el evento
    def check_event(self, mouse_pos):
        if mouse_pos[0] >= self.rect.x and mouse_pos[0] <= self.rect.x + self.rect.width:
                if mouse_pos[1] >= self.rect.y and mouse_pos[1] <= self.rect.y + self.rect.height:
                    return True
        else:
            return False
        
    #Dibuja el boton
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))