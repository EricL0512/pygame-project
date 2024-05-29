import pygame
import sys

from game import Game


class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("start_button")

        self.start_button = pygame.image.load("start.png")
        self.start_button = pygame.transform.scale(self.start_button,
                                                   (self.start_button.get_width() * 5,
                                                    self.start_button.get_height() * 5))
        self.menu_background = pygame.image.load("menu_background.jpg")

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pass
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_r]:  # This will be used to switch screens
                        print('bruh')
                        Game().run()
                        running = False
                    if keys[pygame.K_e]:
                        pass
            self.draw()
            self.clock.tick(60)
            pygame.display.update()

    def draw(self):
        self.screen.blit(self.menu_background, (0, 0))
        self.screen.blit(self.start_button, ((self.screen.get_width() / 2) - (self.start_button.get_width() / 2),
                                             (self.screen.get_height() / 2) - (self.start_button.get_height()) / 2))
        self.screen.blit(self.start_button,
                         ((self.screen.get_width() / 2) - (self.start_button.get_width() / 2),
                          # CHANGE TO A DIFFERENT IMAGE LATER
                          (self.screen.get_height() / 2) - (
                              self.start_button.get_height()) / 2 + self.start_button.get_height() + 50))
        self.screen.blit(self.start_button, ((self.screen.get_width() / 2) - (self.start_button.get_width() / 2),
                                             (self.screen.get_height() / 2) - (
                                                 self.start_button.get_height()) / 2 + self.start_button.get_height() * 2 + 100))
        self.screen.blit(self.start_button, ((self.screen.get_width() / 2) - (self.start_button.get_width() / 2),
                                             (self.screen.get_height() / 2) - (
                                                 self.start_button.get_height()) / 2 - self.start_button.get_height() - 50))


Menu().run()
