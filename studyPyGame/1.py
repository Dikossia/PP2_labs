import pygame 

pygame.init()

screen = pygame.display.set_mode((600,300)) #после кортежа можно добавить flags=pygame.NOFRAME это уберет рамку окна
pygame.display.set_caption("Hello World") #название окна
icon = pygame.image.load("C:\\Users\\Huawei\\Desktop\\PP2_labs\\lab_8_9\\IMAG\\coin.png")
pygame.display.set_icon(icon) #иконка окна

running = True
while running:

   ## screen.fill((255, 204,255)) #цвет фона

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                screen.fill((114,157,224))