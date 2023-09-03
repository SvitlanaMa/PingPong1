import pygame
from random import choice
pygame.init()

window = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

window.fill((175, 238, 238))

FPS = 40

class GameSprite:
    def __init__(self, x, y, w, h, image):
        self.rect = pygame.Rect(x, y, w, h)
        image = pygame.transform.scale(image, (w, h))
        self.image = image

    def paint(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, x, y, w, h, image, speed):
        super().__init__(x, y, w, h, image)
        self.speed = speed
    def move(self, key_up, key_down):
        k = pygame.key.get_pressed()
        if k[key_up]:
            if self.rect.y >= 0:
                self.rect.y -= self.speed
        if k[key_down]:
            if self.rect.bottom <= 500:
                self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, x, y, w, h, image, speedx, speedy):
        super().__init__(x, y, w, h, image)
        self.speedx = speedx
        self.speedy = speedy
        self.isMoving = False
    def move(self):
        if self.isMoving:
            self.rect.x += self.speedx
            self.rect.y += self.speedy

platform_img = pygame.image.load("platform.jpg")
platform_img = pygame.transform.rotate(platform_img, 90)

platform = Player(20, 200, 25, 99, platform_img, 5)
platform1 = Player(460, 200, 25, 99, platform_img, 5)

ball_img = pygame.image.load("ball1.png")
ball = Ball(225, 225, 50, 50, ball_img, 1, 1)

game = True
finish = False

while game:
    if not finish:
        window.fill((175, 238, 238))
        # ball.paint()
        platform.paint()
        platform.move(pygame.K_w, pygame.K_s)
        platform1.paint()
        platform1.move(pygame.K_UP, pygame.K_DOWN)

        ball.paint()
        ball.move()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not ball.isMoving:
                ball.isMoving = True
                ball.speedy *= choice([1, -1])

    

    pygame.display.update()
    clock.tick(FPS)