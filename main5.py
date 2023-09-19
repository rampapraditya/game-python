import pygame
import random

# instalasi
pygame.init()

# mengatur ukuran layar/screen

width = 1000
height = 600

screen = pygame.display.set_mode([width, height])

# Mengubah title screen
pygame.display.set_caption("Tutorial 5")

# memuat dan menggati logo/icon screen
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

# menambahkan background
background = pygame.image.load("backgroud.jpg")

# memambahkan gambar
def plane(x, y):
    image = pygame.image.load("plane.png")
    screen.blit(image, (x, y))

def musuh(x, y):
    image = pygame.image.load("musuh.png")
    screen.blit(image, (x, y))

x = 100
y = 300

x_musuh = random.randint(0, 1000) # menentukan posisi random sesuaikan framenya
y_musuh = random.randint(0, 600)

x_point = 0
y_point = 0

running = True
while running:
    # loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x_point -= 0.5
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                x_point += 0.5
            if event.key == pygame.K_UP or event.key == ord('w'):
                y_point -= 0.5
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                y_point += 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x_point = 0
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                x_point = 0
            if event.key == pygame.K_UP or event.key == ord('w'):
                y_point = 0
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                y_point = 0


        # memberikan batasan
        if x <= 5:
            x = 5
        elif x >= 925:
            x = 925

        if y <= 5:
            y = 5
        elif y >= 525:
            y = 525

    # mengubah warna screen
    screen.fill((255, 255, 255))

    # menambhkan background
    screen.blit(background, (0, 0))

    x += x_point
    y += y_point

    # menampilkan gambar pesawat ke dalam screen
    plane(x, y)
    # menampilkan gambar musuh ke dalam screen
    musuh(x_musuh, y_musuh)

    pygame.display.update()

pygame.quit()