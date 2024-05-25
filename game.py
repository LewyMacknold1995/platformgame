import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400)) 
pygame.display.set_caption('Adventures of Guru Muhammed')
clock = pygame.time.Clock()  
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

score_surface = test_font.render('Welcome traveler', False, (64,64,64))
score_rect = score_surface.get_rect(center = (400,50))

pig_surface  = pygame.image.load('graphics/pig/pig1.png')
original_size = pig_surface.get_size()
new_size = (int(original_size[0] * 0.5), int(original_size[1] * 0.5))
pig_surface = pygame.transform.scale(pig_surface, new_size)
pig_rect = pig_surface.get_rect(bottomright = (600,325))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300)) 
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos): print('collision')
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20
    

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    pygame.draw.rect(screen,'#c0e8ec',score_rect)
    pygame.draw.rect(screen,'#c0e8ec',score_rect, 10)
    screen.blit(score_surface,score_rect)  

    pig_rect.x -= 4
    if pig_rect.right <= 0: pig_rect.left = 800
    screen.blit(pig_surface, pig_rect)

    # Player
    player_gravity += 1
    player_rect.y += player_gravity
    screen.blit(player_surf,player_rect)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')

    # if player_rect.colliderect(pig_rect):
    #     print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)