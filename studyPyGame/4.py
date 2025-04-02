import pygame 

pygame.init()

screen = pygame.display.set_mode((950,555)) #после кортежа можно добавить flags=pygame.NOFRAME это уберет рамку окна
pygame.display.set_caption("Hello World") #название окна
icon = pygame.image.load("C:\\Users\\Huawei\\Desktop\\PP2_labs\\lab_8_9\\IMAG\\coin.png")
pygame.display.set_icon(icon) #иконка окна
player = pygame.image.load("C:\\Users\\Huawei\\Desktop\\PP2_labs\\lab_7\\ima\\rose.jpg")

bg = pygame.image.load("C:\\Users\\Huawei\\Desktop\\PP2_labs\\studyPyGame\\imag\\night.jpg")

running = True
while running:

    screen.blit(bg, (0,0)) #размер и координаты картинки

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()