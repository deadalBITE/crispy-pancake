from pygame import *
import random
from time import sleep
font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, wEW, hEW, speedX, speedY, x_col, y_col, direction, imageEW):
        super().__init__()
        self.speedX =  speedX
        self.speedY =  speedY
        self.wEW = wEW
        self.hEW = hEW
        self.direction = direction
        self.image = transform.scale(image.load(imageEW), (wEW, hEW))
        self.rect = self.image.get_rect()
        self.rect.x = x_col
        self.rect.y = y_col
    def blited(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def walk_direction(self):
        if self.direction == 'right':
            self.rect.x += self.speedX
        if self.direction == 'left':
            self.rect.x -= self.speedX
    def colliderect (self, rect):
        return self.rect.colliderect(rect)
def set_text(text, fsize=50, text_color=(0,0,0)):
    image = pygame.font.Font(None, fsize).render(text, True, color)
def draw(self, shift_x=0, shift_y=0):
    fill()
    window.blit(image, (rect.x + shift_x, rect.y + shift_y))

win_il = font.Font(None,70)
lose_il = font.Font(None,70)
GREEN = (0, 255, 51)
YELLOW = (255,255,0)
RED = (255, 0, 0)
game_cycle = True
ball = GameSprite(40, 40, 6, 6, 30, 30, None, 'nEL_1.png')
platform = GameSprite(200, 30, 20, 0, 100, 10, None, 'nEL_2.png')
platform2 = GameSprite(200, 30, 20, 0, 100, 630, None, 'nEL_2.png')
back = (0,0,0)
window = display.set_mode((1000,700))
window.fill(back)
timed = time.Clock()
while game_cycle == True:
    window.fill(back)
    platform.blited()
    platform2.blited()
    ball.blited()
    platform.walk_direction()
    platform2.walk_direction()
    ball.walk_direction()
    if ball.colliderect(platform.rect):
        ball.speedX *= +1
        ball.speedY *= -1
    if ball.colliderect(platform2.rect):
        ball.speedX *= +1
        ball.speedY *= -1
    if ball.rect.x > 950 or ball.rect.x < 0:
        ball.speedX *= -1
        ball.speedY *= +1
    ball.rect.x += ball.speedX
    ball.rect.y += ball.speedY
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_RIGHT:
                platform.direction = 'right'
        elif e.type == KEYUP:
            if e.key == K_RIGHT:
                platform.direction = ''
        if e.type == KEYDOWN:
            if e.key == K_LEFT:
                platform.direction = 'left'
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                platform.direction = ''
        if e.type == KEYDOWN:
            if e.key == K_d:
                platform2.direction = 'right'
        elif e.type == KEYUP:
            if e.key == K_d:
                platform2.direction = ''
        if e.type == KEYDOWN:
            if e.key == K_a:
                platform2.direction = 'left'
        elif e.type == KEYUP:
            if e.key == K_a:
                platform2.direction = ''
        elif e.type == QUIT:
            game_cycle = False
    if ball.rect.y > 650:
        lose = lose_il.render('PLAYER 1 LOSE', True, (255, 0, 0))
        window.blit(lose,(250,250))
        display.update()
        sleep(4)
        game_cycle = False
    if ball.rect.y < 20:
        lose = lose_il.render('PLAYER 2 LOSE', True, (255, 0, 0))
        window.blit(lose,(250,250))
        display.update()
        sleep(4)
        game_cycle = False
    timed.tick(40)
    display.update()
display.update()
