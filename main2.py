import pygame

# instalasi
pygame.init()

# ukuran layar
tinggi = 600
lebar = 600

screen = pygame.display.set_mode([tinggi, lebar])

# merubah title screen
pygame.display.set_caption("Tutorial 2")

# merubah logo
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

# membuat gambar
image = pygame.image.load("plane.png")
screen.blit(image, (200, 100)) # masukkan gambar dengan koordinat tertentu

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # melakukan update
    pygame.display.update()

pygame.quit()