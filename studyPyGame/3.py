import pygame 

pygame.init()

screen = pygame.display.set_mode((600,300)) #после кортежа можно добавить flags=pygame.NOFRAME это уберет рамку окна
pygame.display.set_caption("Hello World") #название окна
icon = pygame.image.load("C:\\Users\\Huawei\\Desktop\\PP2_labs\\lab_8_9\\IMAG\\coin.png")
player = pygame.image.load("C:\\Users\\Huawei\\Desktop\\PP2_labs\\lab_7\\ima\\rose.jpg")
pygame.display.set_icon(icon) #иконка окна

square = pygame.Surface((50, 50))
square.fill((255, 0, 0)) #цвет квадрата

myFont = pygame.font.Font(None, 30)
text_surface = myFont.render("Hello World", True, (255, 255, 255))

running = True
while running:

    screen.blit(player, (0,0)) #размер и координаты картинки
    screen.blit(square, (0,0)) #размер и координаты квадрата
    screen.blit(text_surface, (100, 100)) #размер и координаты текста
    pygame.draw.circle(screen, (0, 200, 240) ,(100, 100), 50)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        