import sys
import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.game_background = pygame.image.load("background test.jpg")
        self.game_background = pygame.transform.scale_by(self.game_background, 10)

    def run(self):
        running = True
        while running:
            x, y = pygame.mouse.get_pos()
            self.draw()
            self.clock.tick(60)
            pygame.display.update()

    def draw(self):
        self.screen.blit(self.game_background, (0, 0))

    def iterate(self, x):
        if x == 0:
            return 0
        return 1 + self.iterate(x - 1)
