import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
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
    screen.fill("blue")
    pygame.display.update()

    clock.tick(60)

pygame.quit()
