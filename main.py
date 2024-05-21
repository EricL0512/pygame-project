import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame.display.set_caption("start_button")

start_button = pygame.image.load("start.png")
start_button = pygame.transform.scale(start_button, (start_button.get_width() * 5, start_button.get_height() * 5))
menu_background = pygame.image.load("menu_background.jpg")
#menu_background = pygame.transform.scale()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:  # This will be used to switch screens
        running = False
    if keys[pygame.K_e]:  # This will be used to access the menu. These can and will change later but this is a temp.
        running = False
    screen.blit(menu_background, (0, 0))
    screen.blit(start_button, ((screen.get_width() / 2) - (start_button.get_width() / 2),
                               (screen.get_height() / 2) - (start_button.get_height()) / 2))
    screen.blit(start_button, ((screen.get_width() / 2) - (start_button.get_width() / 2), #CHANGE TO A DIFFERENT IMAGE LATER
                               (screen.get_height() / 2) - (start_button.get_height()) / 2 + start_button.get_height() + 50))
    screen.blit(start_button, ((screen.get_width() / 2) - (start_button.get_width() / 2),
                               (screen.get_height() / 2) - (start_button.get_height()) / 2 + start_button.get_height() * 2 + 100))
    screen.blit(start_button, ((screen.get_width() / 2) - (start_button.get_width() / 2),
                               (screen.get_height() / 2) - (start_button.get_height()) / 2 - start_button.get_height() - 50))

    pygame.display.update()
    clock.tick(60)

pygame.quit()

