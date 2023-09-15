import pygame

# instalasi
pygame.init()

# ukuran layar
tinggi = 600
lebar = 600

screen = pygame.display.set_mode([tinggi, lebar])
# merubah warna screen
# screen.fill((255,0,0))

# membuat lingkaran
# pygame.draw.circle(screen, (0,0,200), (120,120), 20)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # melakukan update
    pygame.display.update()

pygame.quit()