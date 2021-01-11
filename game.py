import pygame
import random

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640, 640))

# player
playerX_change = 20
playerY_change = 20
pos_X = random.randint(0, 32) * 20
pos_Y = random.randint(0, 32) * 20
player_surface = pygame.transform.scale(pygame.image.load("player.png"), (20, 20)).convert()
player_surface_rect = player_surface.get_rect(center=(pos_X, pos_Y))
position_list = []

# food
pos_foodX = random.randint(0, 32) * 20
pos_foodY = random.randint(0, 32) * 20
food_surface = pygame.transform.scale(pygame.image.load("apple.png"), (20, 20)).convert()
food_surface_rect = food_surface.get_rect(center=(pos_foodX, pos_foodY))

key = ""

black_surface = pygame.transform.scale(pygame.image.load("black-square.png"), (20, 20)).convert()
for i in range(0, 32):
    for j in range(0, 32):
        screen.blit(black_surface, (i * 20, j * 20))


def create_snake():
    global pos_Y, pos_X, player_surface, player_surface_rect
    screen.blit(player_surface, player_surface_rect)


create_snake()


def create_food():
    global pos_foodY, pos_foodX, food_surface
    screen.blit(food_surface, food_surface_rect)


create_food()


def blit_black():
    pass


def blit_player(rect):
    global position_list
    position_list.append(rect)
    print(position_list)
    screen.blit(player_surface, rect)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                key = "down"
            if event.key == pygame.K_UP:
                key = "up"
            if event.key == pygame.K_LEFT:
                key = "left"
            if event.key == pygame.K_RIGHT:
                key = "right"

    if key == "down":
        player_surface_rect.centery += playerY_change
        blit_player(player_surface_rect)

    if key == "up":
        player_surface_rect.centery -= playerY_change
        blit_player(player_surface_rect)

    if key == "left":
        player_surface_rect.centerx -= playerX_change
        blit_player(player_surface_rect)

    if key == "right":
        player_surface_rect.centerx += playerX_change
        blit_player(player_surface_rect)

    pygame.display.update()
    clock.tick(10)
