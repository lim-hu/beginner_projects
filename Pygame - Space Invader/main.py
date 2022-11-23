# Import library
import pygame
from pygame.locals import * #QUIT and keyboard buttons: K_LEFT, K_SPACE etc.
from pygame import mixer
import random

mainClock = pygame.time.Clock()

# Initalize pygame
pygame.init()

# Load sounds
mixer.music.load('sounds/bg_sound.mp3')
mixer.music.set_volume(0.4)
mixer.music.play(-1)


# Background
bg_img = pygame.image.load('images/background.png')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/ufo.png')
pygame.display.set_icon(icon)

# Create the screen
screen = pygame.display.set_mode((640, 480))

# Player
player_img = pygame.image.load("images/player.png")
player_img = pygame.transform.scale(player_img, (36, 36))
player_x = (screen.get_width() / 2) - (player_img.get_width() / 2)
player_y = screen.get_height() - player_img.get_height() - 10
move_px = 0

# Enemy
enemy_img = pygame.image.load("images/enemy.png")
enemy_imgs = []
enemy_x = []
enemy_y = []
move_ex = []
move_ey = []

num_enemy = 6

for i in range(num_enemy):
    enemy_img = pygame.transform.scale(enemy_img, (54, 54))
    enemy_imgs.append(enemy_img)
    enemy_x.append(random.randint(0, screen.get_width() - enemy_img.get_width()))
    enemy_y.append(random.randint(10, 108))
    move_ex.append(2)
    move_ey.append(enemy_img.get_height())

# Bullet
# READY = You can't see the bullet on the screen
# FIRE = The bullet is currently moving
bullet_img = pygame.image.load("images/bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (10 , 32))
bullet_x = player_x + (player_img.get_width() / 2) - (bullet_img.get_width() / 2)
bullet_y = screen.get_height() + bullet_img.get_height()
move_bx = 0
move_by = 6
bullet_state = "READY"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 20)
font_x = 10
font_y = 10

def show_score(x, y):
    score = font.render(f"Score: {str(score_value)}", True, (255,166,0))
    screen.blit(score, (x, y))
def player(x, y):
    screen.blit(player_img, (x, y))
    
def enemy(x, y, i):
    screen.blit(enemy_imgs[i], (x, y))
    
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "FIRE"
    screen.blit(bullet_img, (x, y))
    
def detect_collision(enemy_x, bullet_x, enemy_y, bullet_y):
    enemy_rect = pygame.Rect(enemy_x + 3, enemy_y, enemy_img.get_width() - 6, enemy_img.get_height())
    bullet_rect = pygame.Rect(bullet_x, bullet_y, bullet_img.get_width(), bullet_img.get_height())
    # pygame.draw.rect(screen, (0, 255, 0), enemy_rect)
    # pygame.draw.rect(screen, (0, 255, 0), bullet_rect)
    screen.blit(bullet_img, (bullet_x, bullet_y))
    if enemy_rect.colliderect(bullet_rect) == True:
        return True
    else:
        return False
    
def game_over_text():
    over_font = pygame.font.Font('freesansbold.ttf', 64)
    over_text = over_font.render("GAME OVER", True, (200, 50, 50))
    screen.blit(over_text, ((screen.get_width() / 2) - (over_text.get_width() / 2), (screen.get_height() / 2) - (over_text.get_height() / 2)))

running = True
# Game loop
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    
    #Background
    screen.blit(bg_img, (0, 0))
    pygame.draw.line(screen, (30, 30, 30), (0, 400), (screen.get_width(), 400))
    
    for event in pygame.event.get(): #check events
        if event.type == QUIT: #clear quit
            running = False
        
        # Check events
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_px = -4
            if event.key == K_RIGHT:
                move_px = 4
            if event.key == K_SPACE:
                if bullet_state == "READY":
                    bullet_sound = mixer.Sound('sounds/shot.mp3')
                    bullet_sound.set_volume(0.4)
                    bullet_sound.play()
                    bullet_x = player_x + (player_img.get_width() / 2) - (bullet_img.get_width() / 2)
                    bullet_y = player_y - bullet_img.get_height()
                    fire_bullet(bullet_x, bullet_y)

        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                move_px = 0
    
    # Check Player/Wall collision
    player_x += move_px
    if player_x <= 0:
        player_x = 0
    elif player_x >= screen.get_width() - player_img.get_width():
        player_x = screen.get_width() - player_img.get_width()
    
    # Check Enemy/Wall collision    
    for i in range(num_enemy):
        # GAME OVER
        if enemy_y[i] + enemy_img.get_height() > 400:
            for j in range(num_enemy):
                enemy_y[j] = 1500
            game_over_text()
            break
        
        enemy_x[i] += move_ex[i]
        if enemy_x[i] <= 0:
            move_ex[i] *= -1
            enemy_y[i] += move_ey[i]
        elif enemy_x[i] >= screen.get_width() - enemy_img.get_width():
            move_ex[i] *= -1
            enemy_y[i] += move_ey[i]
            
        # Check Bullet/Enemy collision
        collision = detect_collision(enemy_x[i], bullet_x, enemy_y[i], bullet_y)
        if collision:
            explosion_sound = mixer.Sound('sounds/explosion.wav')
            explosion_sound.set_volume(0.4)
            explosion_sound.play()
            bullet_state = "READY"
            bullet_y = screen.get_height() + bullet_img.get_height()
            enemy_x[i] = random.randint(0, screen.get_width() - enemy_img.get_width())
            enemy_y[i] = random.randint(10, 162)
            score_value += 1
            
        enemy(enemy_x[i], enemy_y[i], i)
      
    if bullet_state == "FIRE":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= move_by
    
    # Check the Bullet-upper wall collision 
    if bullet_y <= 0:
        bullet_y = screen.get_height() + bullet_img.get_height()
        bullet_state = "READY"
    
    
    show_score(font_x, font_y)
    player(player_x, player_y)
    
        
    pygame.display.update()
    mainClock.tick(60)