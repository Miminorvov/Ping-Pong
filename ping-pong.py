from pygame import *

back = transform.scale(image.load('kort.jpg'))
win_wight = 600
win_height = 500
window = display.set_mode((win_wight,win_height))
window.fill(back)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, w,h, player_speed):
        super().__init__()
        self.image =  transform.scale(image.load(player_image), (w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.x > 5:
            self.rect.y += self.speed    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN]and self.rect.x > 5:
            self.rect.y += self.speed

game = True
finish  = False 
clock = time.Clock()
FPS = 60

roket1 = Player('Roket.jpg', 30, 200, 50 , 150 ,5)
roket2 = Player('Roket.jpg', 520, 200, 50, 150,5)
ball = GameSprite('BaLL.png', 200,200,50,50,5)

font.init()
font = font.Font(None,35)
lose1 = font.render('Player 1 Lose!', True, (180,0,0))
lose2 = font.render('Player 2 Lose!', True, (180,0,0))


speed_x = 3
speed_y = 3

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        roket1.update_l()
        roket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y 

        if sprite.collide_rect(roket1, ball) or sprite.collide_rect(roket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.x < 0:
            finish = True 
            window.blit(lose2, (200, 200))
            game_over = True

        roket1.reset()
        roket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)



