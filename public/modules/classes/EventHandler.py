import pygame.event

class EventHandler:

    #Constructor
    def __init__(self) -> None:
        self.key_map = {
            "W": False,
            "A": False,
            "S": False,
            "D": False,
            "A_UP": False,
            "A_DOWN": False,
            "A_LEFT": False,
            "A_RIGHT": False,
            "A_8": False,
            "A_5": False
        }

    #Eventos de escucha para el teclado
    def listenKeyboardEvents(self):
        events = pygame.event.get()

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in events:
            if event.type == pygame.QUIT:
                return not(True)

            elif event.type == pygame.KEYDOWN:
                #Arriba
                if event.key == pygame.K_w:
                    self.key_map["W"] = True
                #Izquierda
                if event.key == pygame.K_a:
                    self.key_map["A"] = True
                #Abajo
                if event.key == pygame.K_s:
                    self.key_map["S"] = True
                #Derecha
                if event.key == pygame.K_d:
                    self.key_map["D"] = True
                #Flecha Arriba
                if event.key == pygame.K_UP:
                    self.key_map["A_UP"] = True
                #Flecha Abajo
                if event.key == pygame.K_DOWN:
                    self.key_map["A_DOWN"] = True
                #Flecha Izquierda
                if event.key == pygame.K_LEFT:
                    self.key_map["A_LEFT"] = True
                #Flecha Derecha
                if event.key == pygame.K_RIGHT:
                    self.key_map["A_RIGHT"] = True
                #Num 5
                if event.key == pygame.K_KP5:
                    self.key_map["A_5"] = True
                #Num 8
                if event.key == pygame.K_KP8:
                    self.key_map["A_8"] = True

            elif event.type == pygame.KEYUP:
                #Arriba
                if event.key == pygame.K_w:
                    self.key_map["W"] = False
                #Izquierda
                if event.key == pygame.K_a:
                    self.key_map["A"] = False
                #Abajo
                if event.key == pygame.K_s:
                    self.key_map["S"] = False
                #Derecha
                if event.key == pygame.K_d:
                    self.key_map["D"] = False
                #Flecha Arriba
                if event.key == pygame.K_UP:
                    self.key_map["A_UP"] = False
                #Flecha Abajo
                if event.key == pygame.K_DOWN:
                    self.key_map["A_DOWN"] = False
                #Flecha Izquierda
                if event.key == pygame.K_LEFT:
                    self.key_map["A_LEFT"] = False
                #Flecha Derecha
                if event.key == pygame.K_RIGHT:
                    self.key_map["A_RIGHT"] = False
                #Num 5
                if event.key == pygame.K_KP5:
                    self.key_map["A_5"] = False
                #Num 8
                if event.key == pygame.K_KP8:
                    self.key_map["A_8"] = False


        return not(False)