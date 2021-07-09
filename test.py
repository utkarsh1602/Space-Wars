import sys, pygame
import os
pygame.init()

size = width, height = 700, 500
speed = 5
colour = 255, 255, 255
black = 0,0,0
RED = 0,255,255
BLUE = 255,0,255
BULLET_COUNT = 4

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space War")

background = pygame.image.load(os.path.join('asset','space.png'))
background = pygame.transform.scale(background,(width,height))
player_ship_1 = pygame.image.load(os.path.join('asset',"player_1.png"))
player_ship_1 = pygame.transform.scale(player_ship_1,(100,100))

player_ship_2 = pygame.image.load(os.path.join('asset',"player_1.png"))
player_ship_2 = pygame.transform.scale(player_ship_1,(100,100))

ballrect_1 = player_ship_1.get_rect()
ballrect_2 = player_ship_2.get_rect()

ballrect_1.x = width-100
ballrect_1.y = height-100

clock = pygame.time.Clock()

play_1_bullets = []
play_2_bullets = []

def main():

    player_1_health = 10
    player_2_health = 10

    while True:

        clock.tick(60)    
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(play_1_bullets)<BULLET_COUNT:
                    bullet = pygame.Rect(ballrect_2.x+100,ballrect_2.y+50,6,4)
                    play_1_bullets.append(bullet)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL and len(play_2_bullets)<BULLET_COUNT:
                    bullet = pygame.Rect(ballrect_1.x,ballrect_1.y+50,6,4)
                    play_2_bullets.append(bullet)        

        keys = pygame.key.get_pressed()        

        # player 1 controls
        if keys[pygame.K_UP]:
            if not (ballrect_1.y < 0):
                ballrect_1.y -= speed

        if keys[pygame.K_DOWN]:
            if not (ballrect_1.y > height-100):
                ballrect_1.y += speed

        if keys[pygame.K_RIGHT]:
            if not (ballrect_1.x > width-100):
                ballrect_1.x += speed 

        if keys[pygame.K_LEFT]:
            if not (ballrect_1.x < border.x):
                ballrect_1.x -= speed 


        # player 2 controls        
        if keys[pygame.K_w]:
            if not (ballrect_2.y < 0):
                ballrect_2.y -= speed

        if keys[pygame.K_s]:
            if not (ballrect_2.y > height-100):
                ballrect_2.y += speed

        if keys[pygame.K_d]:
            if not (ballrect_2.x > border.x-100):
                ballrect_2.x += speed 

        if keys[pygame.K_a]:
            if not (ballrect_2.x < 0):
                ballrect_2.x -= speed 

        # bullets movement  
        for bullet in play_1_bullets:
            bullet.x += 3     
            if ballrect_1.colliderect(bullet):
                player_1_health-=1
                play_1_bullets.remove(bullet)
            if bullet.x >= width:
                play_1_bullets.remove(bullet)

        for bullet in play_2_bullets:
            bullet.x -= 3     
            if ballrect_2.colliderect(bullet):
                player_2_health-=1
                play_2_bullets.remove(bullet)
            if bullet.x <= 0:
                play_2_bullets.remove(bullet)          


        border = pygame.Rect(width//2,0,5,height)        
        screen.fill(colour)
        screen.blit(background,(0,0))
        player_1_health_text = HEALTH_FONT.render(
            "Player 2: " + str(player_1_health), 1, colour)
        player_2_health_text = HEALTH_FONT.render(
            "Player 1: " + str(player_2_health), 1, colour)
        screen.blit(player_1_health_text, (width - player_1_health_text.get_width() - 10, 10))
        screen.blit(player_2_health_text, (10, 10))

        for bullet in play_1_bullets:
            pygame.draw.rect(screen,RED,bullet)
        for bullet in play_2_bullets:
            pygame.draw.rect(screen,BLUE,bullet)    

        pygame.draw.rect(screen,black,border)
        screen.blit(player_ship_1, ballrect_1)
        screen.blit(player_ship_2, ballrect_2)

        if player_1_health<=0 or player_2_health<=0:

            game_over = WINNER_FONT.render("GAME OVER!!",1,(0,255,0))
            screen.blit(game_over,(width//2 - game_over.get_width()//2,height//2 - game_over.get_height()))

            if player_1_health<=0:
                player_won = WINNER_FONT.render("Player 1 WON!!",1,(0,255,0))
                screen.blit(player_won,(width//2 - player_won.get_width()//2,height//2))

            if player_2_health<=0:
                player_won = WINNER_FONT.render("Player 2 WON!!",1,(0,255,0))
                screen.blit(player_won,(width//2 - player_won.get_width()//2,height//2))   

            pygame.display.update()
            play_1_bullets.clear()
            play_2_bullets.clear()
            pygame.time.delay(5000)
            break     

        pygame.display.flip()

    main()    

if __name__ == '__main__':
    main()    