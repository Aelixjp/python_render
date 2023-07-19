import pygame

from .Graphics import Graphics
from .EventHandler import EventHandler

class Screen:
    
    def __init__(self, SCREEN_DIM = (1280, 720), SCREEN_COLOR = (0, 0, 0, 0), SCREEN_TITLE = '', FPS = 75) -> None:
        #Constants
        self.FPS = FPS
        self.SCREEN_DIM = SCREEN_DIM
        self.SCREEN_COLOR = SCREEN_COLOR
        
        #Variables
        self.running = True
        self.title = SCREEN_TITLE

        self.init()

    def init(self):
        self.screen  = pygame.display.set_mode(self.SCREEN_DIM)
        self.clock   = pygame.time.Clock()
        self.eventHandler = EventHandler()
        self.graphics = Graphics(self.screen)

        self.setTitle(self.title)
    
    def setTitle(self, title):
        self.title = title

        pygame.display.set_caption(self.title)

    def tick(self):
        self.clock.tick(self.FPS)

    def paint(self):
        # fill the screen with a color to wipe away anything from last frame
        self.screen.fill(self.SCREEN_COLOR)

    def listenForEvents(self):
        self.running = self.eventHandler.listenKeyboardEvents()

    def getFPS(self) -> int:
        return self.FPS

    def setFPS(self, FPS):
        self.FPS = FPS

    def kill(self):
        self.running = False