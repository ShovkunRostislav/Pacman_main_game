import random
import pygame

pygame.font.init()
pygame.init()

win_height = 800
win_width = 700
window = pygame.display.set_mode((win_width, win_height))

start_run = False

    # --- main ---
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, images, x, y, width, height, speed):
        super().__init__()

        # img = image.load(image)
        self.image = pygame.transform.scale(pygame.image.load(images), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, window):
        window.blit(self.image, self.rect)

    def redraw(self):
        window.blit(self.image, (1000, 1000))

class Hero(GameSprite):
    def update(self):
        print('TODO: Update Hero')

    def move(self, keyPressed):
        side = None

        if keyPressed[pygame.K_LEFT] and self.rect.left > 5:
            self.rect.x -= self.speed
            if pygame.sprite.spritecollide(self, walls, False):
                side = 'Right'
                self.rect.x += 5

        if keyPressed[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if pygame.sprite.spritecollide(player, walls, False):
                side = 'Left'
                self.rect.x -= 5

        if keyPressed[pygame.K_UP] and self.rect.top > 5:
            self.rect.y -= self.speed
            if pygame.sprite.spritecollide(self, walls, False):
                side = 'Down'
                self.rect.y += 5

        if keyPressed[pygame.K_DOWN] and self.rect.bottom < win_height:
            self.rect.y += self.speed
            if pygame.sprite.spritecollide(self, walls, False):
                side = 'Up'
                self.rect.y -= 5

        if side:
            print('Hero collision:', side)

        if self.rect.right > win_width - 10 and 300 < self.rect.top < 330 and game_complete == False:
            self.rect.left = 10

        elif self.rect.left < 10 and 300 < self.rect.top < 330 and game_complete == False:
            self.rect.right = win_width - 10

        if pygame.sprite.spritecollide(self, ghosts, False):
            if len(health) == 4:
                heart4.kill()
                self.rect.x, self.rect.y = 10, 302
            elif len(health) == 3:
                heart3.kill()
                self.rect.x, self.rect.y = 10, 302
            elif len(health) == 2:
                heart2.kill()
                self.rect.x, self.rect.y = 10, 302
            elif len(health) == 1:
                heart1.kill()
                self.rect.x, self.rect.y = 10, 302

class Enemy(GameSprite):

    def __init__(self, image, x, y, width, height, speed):
        super().__init__(image, x, y, width, height, speed)

        self.move_list = ['right', 'left', 'up', 'down']

        self.direction = random.choice(self.move_list)

    def move(self):
        if self.direction == 'right':
            if not pygame.sprite.spritecollide(self, walls, False):
                self.rect.x += self.speed
            else:
                self.rect.x -= 6
                self.direction = random.choice(self.move_list)
        elif self.direction == 'left':
            if not pygame.sprite.spritecollide(self, walls, False):
                self.rect.x -= self.speed
            else:
                self.rect.x += 6
                self.direction = random.choice(self.move_list)
        elif self.direction == 'up':
            if not pygame.sprite.spritecollide(self, walls, False):
                self.rect.y -= self.speed
            else:
                self.rect.y += 6
                self.direction = random.choice(self.move_list)
        elif self.direction == 'down':
            if not pygame.sprite.spritecollide(self, walls, False):
                self.rect.y += self.speed
            else:
                self.rect.y -= 6
                self.direction = random.choice(self.move_list)

class Wall(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()

        self.color = color
        self.width = width
        self.height = height

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, window):
        window.blit(self.image, self.rect)

# it keeps single coin so name `Coin` without `s` seems better
class Coin(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def draw(self, window):
        window.blit(self.image, self.rect)
class Area():
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    def change_color(self, new_color):
        self.fill_color = new_color
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def draw(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
class Label(Area):
    def set_text(self, text, t_size, t_color):
        self.image = pygame.font.SysFont("verdana", t_size).render(text, True, t_color)
    def reset(self, shift_x = 0, shift_y = 0):
        Area.draw(self)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

game_complete = False
game = True
supr_Pint = False

font_score = pygame.font.Font('Tkachev - Lugatype.ttf', 30)
coins_count = 0
font_end = pygame.font.Font('Tkachev - Lugatype.ttf', 50)

clock = pygame.time.Clock()

walls = [
        Wall((169, 169, 169), 0, 0, 700, 31),
        Wall((169, 169, 169), 0, 20, 31, 210),
        Wall((169, 169, 169), 0, 200, 145, 31),
        Wall((169, 169, 169), 115, 200, 31, 95),
        Wall((169, 169, 169), 0, 270, 145, 31),
        Wall((169, 169, 169), 670, 20, 31, 210),
        Wall((169, 169, 169), 556, 200, 145, 31),
        Wall((169, 169, 169), 556, 200, 31, 95),
        Wall((169, 169, 169), 556, 270, 150, 31),
        Wall((169, 169, 169), 335, 0, 31, 95),
        Wall((169, 169, 169), 187, 70, 110, 31),
        Wall((169, 169, 169), 406, 70, 110, 31),
        Wall((169, 169, 169), 187, 470, 110, 31),
        Wall((169, 169, 169), 406, 470, 110, 31),
        Wall((169, 169, 169), 190, 335, 31, 95),
        Wall((169, 169, 169), 485, 335, 31, 95),
        Wall((169, 169, 169), 0, 670, 700, 31),
        Wall((169, 169, 169), 0, 400, 31, 280),
        Wall((169, 169, 169), 0, 400, 145, 31),
        Wall((169, 169, 169), 115, 340, 31, 70),
        Wall((169, 169, 169), 0, 334, 145, 31),
        Wall((169, 169, 169), 670, 400, 31, 280),
        Wall((169, 169, 169), 556, 340, 31, 70),
        Wall((169, 169, 169), 556, 334, 145, 31),
        Wall((169, 169, 169), 556, 400, 150, 31),
        Wall((169, 169, 169), 16, 531, 60, 31),
        Wall((169, 169, 169), 624, 531, 60, 31),
        Wall((169, 169, 169), 260, 340, 180, 31),
        Wall((169, 169, 169), 260, 135, 180, 31),
        Wall((169, 169, 169), 260, 531, 180, 31),
        Wall((169, 169, 169), 260, 400, 180, 31),
        Wall((169, 169, 169), 190, 135, 31, 160),
        Wall((169, 169, 169), 335, 135, 31, 95),
        Wall((169, 169, 169), 335, 405, 31, 95),
        Wall((169, 169, 169), 335, 542, 31, 95),
        Wall((169, 169, 169), 190, 535, 31, 95),
        Wall((169, 169, 169), 485, 535, 31, 95),
        Wall((169, 169, 169), 485, 135, 31, 160),
        Wall((169, 169, 169), 75, 70, 70, 31),
        Wall((169, 169, 169), 75, 133, 70, 31),
        Wall((169, 169, 169), 555, 70, 70, 31),
        Wall((169, 169, 169), 555, 133, 70, 31),
        Wall((169, 169, 169), 555, 470, 70, 31),
        Wall((169, 169, 169), 75, 470, 70, 31),
        Wall((169, 169, 169), 115, 470, 31, 95),
        Wall((169, 169, 169), 555, 470, 31, 95),
        Wall((169, 169, 169), 75, 600, 220, 31),
        Wall((169, 169, 169), 405, 600, 220, 31),
        Wall((169, 169, 169), 215, 200, 85, 31),
        Wall((169, 169, 169), 405, 200, 85, 31),
        Wall((169, 169, 169), 260, 270, 30, 31),
        Wall((169, 169, 169), 410, 270, 30, 31),
        Wall((169, 169, 169), 260, 275, 31, 95),
        Wall((169, 169, 169), 410, 275, 31, 95),
    ]

coins = pygame.sprite.Group()

coins.add([
        Coin((255, 255, 0), 130, 309, 5, 5),
        Coin((255, 255, 0), 240, 309, 5, 5),
        Coin((255, 255, 0), 340, 250, 5, 5),
        Coin((255, 255, 0), 460, 309, 5, 5),
        Coin((255, 255, 0), 570, 309, 5, 5),
        Coin((255, 255, 0), 240, 180, 5, 5),
        Coin((255, 255, 0), 460, 180, 5, 5),
        Coin((255, 255, 0), 310, 111, 5, 5),
        Coin((255, 255, 0), 390, 111, 5, 5),
        Coin((255, 255, 0), 60, 180, 5, 5),
        Coin((255, 255, 0), 640, 180, 5, 5),
        Coin((255, 255, 0), 60, 50, 5, 5),
        Coin((255, 255, 0), 640, 50, 5, 5),
        Coin((255, 255, 0), 160, 409, 5, 5),
        Coin((255, 255, 0), 240, 380, 5, 5),
        Coin((255, 255, 0), 340, 380, 5, 5),
        Coin((255, 255, 0), 460, 380, 5, 5),
        Coin((255, 255, 0), 530, 409, 5, 5),
        Coin((255, 255, 0), 460, 450, 5, 5),
        Coin((255, 255, 0), 240, 450, 5, 5),
        Coin((255, 255, 0), 390, 450, 5, 5),
        Coin((255, 255, 0), 310, 450, 5, 5),
        Coin((255, 255, 0), 630, 450, 5, 5),
        Coin((255, 255, 0), 50, 450, 5, 5),
        Coin((255, 255, 0), 600, 520, 5, 5),
        Coin((255, 255, 0), 90, 520, 5, 5),
        Coin((255, 255, 0), 530, 570, 5, 5),
        Coin((255, 255, 0), 160, 570, 5, 5),
        Coin((255, 255, 0), 60, 640, 5, 5),
        Coin((255, 255, 0), 640, 640, 5, 5),
        Coin((255, 255, 0), 300, 315, 5, 5),
        Coin((255, 255, 0), 395, 315, 5, 5)
    ])

super_point = GameSprite('pixlr-bg-result (7).png', 350, 640, 20, 25, 1)
player = Hero('full_open_mouth.png', 10, 302, 24, 24,2)

ghost_chise = Enemy('pixlr-bg-result (2).png', 350, 309, 25, 25, 2)
ghost_other = Enemy('pixlr-bg-result (6).png', 350, 309, 20, 25, 2)
ghost_third = Enemy('pixlr-bg-result (8).png', 350, 309, 20, 25, 2)
ghost_forth = Enemy('pixlr-bg-result (9).png', 350, 309, 20, 25, 2)
ghost_ffifth = Enemy('pixlr-bg-result.png', 350, 309, 20, 25, 2)
ghost_sixth = Enemy('21575-4-pac-man-ghost-image.png', 350, 309, 20, 25, 2)
ghost_seventh = Enemy('galaxy.png', 350, 309, 20, 25, 2)

heart1 = GameSprite('pixlr-bg-result (4).png', 580, 745, 25, 25, 1)
heart2 = GameSprite('pixlr-bg-result (4).png', 605, 745, 25, 25, 1)
heart3 = GameSprite('pixlr-bg-result (4).png', 630, 745, 25, 25, 1)
heart4 = GameSprite('pixlr-bg-result (4).png', 655, 745, 25, 25, 1)

health = pygame.sprite.Group()
health.add(heart1, heart2, heart3)

apples = pygame.sprite.Group()
apples.add(super_point)

ghosts = pygame.sprite.Group()
ghosts.add(ghost_chise, ghost_other, ghost_third, ghost_forth, ghost_ffifth, ghost_sixth, ghost_seventh)

start = Label(win_width / 2 - 50, win_height / 2 - 10, 100, 50, (100, 200, 100))
start.set_text('PLAY', 30, (255, 0, 0))

exit_game = Label(win_width / 2 - 50, win_height / 2 + 50, 100, 50, (100, 200, 100))
exit_game.set_text('EXIT', 30, (255, 0, 0))

finish = False

counter = 10
text = '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font34 = pygame.font.SysFont('Consolas', 30)
def start_game():
    if finish != True:
        # GHOSTS
        ghost_chise.move()
        ghost_other.move()
        ghost_third.move()

        # PACMAN
        keyPressed = pygame.key.get_pressed()

        player.move(keyPressed)
        for w in walls:
            w.draw(window)
        score = font_score.render('Score : ', False, (255, 255, 0))
        score_num = font_score.render(str(coins_count), False, (255, 255, 0))
        window.blit(score, (30, 746))
        window.blit(score_num, (99, 746))

        coins.draw(window)

        player.draw(window)

        ghost_chise.draw(window)
        ghost_other.draw(window)
        ghost_third.draw(window)

        if len(health) == 3 and supr_Pint == False:
            super_point.draw(window)

        health.draw(window)

txt = 'Press S to continue, E to exit'
font3 = pygame.font.SysFont('verdana', 25)
pause_txt = font3.render(txt, True, (255, 255, 255))

counter = 10
text = '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font34 = pygame.font.SysFont('Consolas', 30)

pause = False

def pause():
    paused = True
    while paused:
        window.blit(pause_txt, (160, 190))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_s:
                    paused = False
                if e.key == pygame.K_e:
                    exit()
        pygame.display.update()

start_ticks=pygame.time.get_ticks()

starting = False
while game:
    window.fill((0,0,0))
    start.reset(15, 5)
    exit_game.reset(15, 5)
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
    pygame.display.set_icon(pygame.image.load("pacman-html-canvas-.ico"))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

        if e.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'boom!'

        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            if start.collidepoint(x, y):
                starting = True
            if exit_game.collidepoint(x, y): game = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_p:
                start = Label(1000, 1000, 100, 50, (100, 200, 100))
                start.set_text('PLAY', 30, (255, 0, 0))
                exit_game = Label(1000, 1000, 100, 50, (100, 200, 100))
                exit_game.set_text('EXIT', 30, (255, 0, 0))
                pause()

    if seconds > 3:
        # if more than 10 seconds close the game
        if starting:
            start = Label(1000, 1000, 100, 50, (100, 200, 100))
            start.set_text('PLAY', 30, (255, 0, 0))

            exit_game = Label(1000, 1000, 100, 50, (100, 200, 100))
            exit_game.set_text('EXIT', 30, (255, 0, 0))

            start_game()

            window.blit(font34.render(text, True, (0, 0, 0)), (32, 48))
    if coins_count >= 1000:
        ghost_forth.draw(window)
        ghost_forth.move()
        ghost_ffifth.draw(window)
        ghost_ffifth.move()
    if coins_count >= 2000:
        ghost_sixth.draw(window)
        ghost_sixth.move()
        ghost_seventh.draw(window)
        ghost_seventh.move()
    if coins_count == 2900:
        game_complete = True
    elif coins_count == 3100 and game_complete == True and 320 < player.rect.x < 350 and 290 < player.rect.y < 310:
        lvl_end_not_all = font_end.render('Game complete!', False, (255, 0, 0))
        coins_not_all = font_end.render('Coins earned 31/32', False, (255, 0, 0))
        window.blit(lvl_end_not_all, (150, 300))
        window.blit(coins_not_all, (150, 230))
        finish = True
    elif coins_count == 3200 and game_complete == True and player.rect.right > win_width - 10 and 300 < player.rect.top < 330:
        lvl_end_all = font_end.render('Game complete!', False, (255, 0, 0))
        coins_all = font_end.render('Coins earned 32/32', False, (255, 0, 0))
        window.blit(lvl_end_all, (150, 300))
        window.blit(coins_all, (150, 230))
        finish = True
    if pygame.sprite.spritecollide(player, coins, True): coins_count += 100
    # UPDATE SCREEN

    if len(health) == 3 and pygame.sprite.spritecollide(player, apples, True):
        super_point.kill()
        supr_Pint = True
        super_point.redraw()
        health.add(heart4)
        print(len(health))
    elif len(health) == 2:
        super_point.redraw()
    if len(health) == 0:
        window.fill((255, 255, 0))
        lvl_lose = font_end.render('GAME OVER!', False, (255, 0, 0))
        window.blit(lvl_lose, (150, 300))
        finish = True
    pygame.display.update()
    clock.tick(60)
