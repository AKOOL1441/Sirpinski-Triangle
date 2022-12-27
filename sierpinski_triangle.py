import random
import math
import pygame
pygame.init()

#USER CAN CHANGE
TRIANGLE_BASE = 800 #Must be even
ITERATIONS = 30000

TRIANGLE_HEIGHT = round((TRIANGLE_BASE/2)*math.sqrt(3))
WIN_WIDTH, WIN_HEIGHT = TRIANGLE_BASE + 20, TRIANGLE_HEIGHT + 20
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Sierpinski Triangle????")

FPS = 240
BLACK = (0,0,0)
WHITE = (255,255,255)
WIN_FONT = pygame.font.SysFont("comicsans",100)

def gen_new_pixel():
    new_pixel_x = random.randint(10, TRIANGLE_BASE + 10)
    temp_new_pixel_x = new_pixel_x - 10
    if temp_new_pixel_x > TRIANGLE_BASE/2:
        temp_new_pixel_x -= 2*(temp_new_pixel_x - (TRIANGLE_BASE/2))
    temp_new_triangle_height = round(temp_new_pixel_x*math.sqrt(3))
    new_pixel_y = random.randint(TRIANGLE_HEIGHT + 10 - temp_new_triangle_height, TRIANGLE_HEIGHT + 10)
    return new_pixel_x, new_pixel_y

def main():
    WIN.fill(WHITE)
    point_1 = (TRIANGLE_BASE/2 + 10, 10)
    point_2 = (10, TRIANGLE_HEIGHT + 10)
    point_3 = (10 + TRIANGLE_BASE, TRIANGLE_HEIGHT + 10)
    points = [point_1, point_2, point_3]
    pygame.draw.rect(WIN,BLACK,(point_1[0], point_1[1], 1, 1))
    pygame.draw.rect(WIN,BLACK,(point_2[0], point_2[1], 1, 1))
    pygame.draw.rect(WIN,BLACK,(point_3[0], point_3[1], 1, 1))
    
    new_pixel_x, new_pixel_y = gen_new_pixel()
    pygame.display.update()

    run = True
    i = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if i < ITERATIONS:
            corner = points[random.randrange(3)]
            new_pixel_x = (new_pixel_x + corner[0])/2
            new_pixel_y = (new_pixel_y + corner[1])/2
            pygame.draw.rect(WIN,BLACK,(new_pixel_x, new_pixel_y, 1, 1))
            i += 1
            if i == ITERATIONS:
                WIN.blit(WIN_FONT.render("Tada!",1,BLACK), (5,5))
            pygame.display.update()
        

if __name__ == "__main__":
    main()