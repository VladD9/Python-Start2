from pygame import *

class Game(sprite.Sprite):
    def __init__(self,player_image,p_x, p_y, p_s):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(50,50))
        self.speed = p_s
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
        
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Move(Game):
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_LEFT] and self.rect.x <620:
            self.rect.x -= self.speed
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_LEFT] and self.rect.y <420:
            self.rect.y -= self.speed
window = display.set_mode((700,500))
display.set_caption("Лабіринт")

bg = transform.scale(image.load("bg.jpg"),(700,500))
player = Game("png-transparent-among-us.png", 5, 420,4)
enemy = Game("impostor.png", 5, 420,4)
treasure = Game("Treasure.png", 580, 420,0)
FPS = 60
clock = time.Clock()


game = True

mixer.init()
mixer.music.load("Slugfest_ingame_03.mp3")
mixer.music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(bg,(0,0))
    player.reset()
    enemy.reset()
    treasure.reset()
    
    display.update()
    clock.tick(FPS)






