import pygame, random
from game.fileLoader import *
import game.constants as c



class Explosion(object):
    def __init__(self):
        self.explosion_list = []
        self.images = (c.IMAGES["explosion01"], c.IMAGES["explosion02"], c.IMAGES["explosion03"], c.IMAGES["explosion04"],
                       c.IMAGES["explosion05"], c.IMAGES["explosion06"], c.IMAGES["explosion07"], c.IMAGES["explosion08"],
                       c.IMAGES["explosion09"], c.IMAGES["explosion10"], c.IMAGES["explosion11"], c.IMAGES["explosion12"],
                       c.IMAGES["explosion13"], c.IMAGES["explosion14"], c.IMAGES["explosion15"])

    def add(self, pos):
        self.explosion_list.append([pos, 0])  # the second argument is for the frame number;
        c.SOUNDS["explosion"].play()

    def draw(self, screen):
        if len(self.explosion_list) > 0:
            for item in self.explosion_list:
                screen.blit(self.images[item[1]], item[0])
                if len(self.images) > item[1] + 1:
                    item[1] += 1
                else:
                    self.explosion_list.remove(item)

class Enemy(pygame.sprite.Sprite):
    tick = 15
    projectile_image = None

    def __init__(self, img, projectile_list, tick_delay):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        if (self.image == c.IMAGES["enemy3"]):
            factoN = random.randint(0, 1)
            self.rect.topleft = (150, -70)
            self.speed_x = 0

        else:
            self.rect.topleft = (random.randint(500, 800), -70)

            if self.rect.x < 210:
                self.speed_x = random.randint(-1, 5)
            elif self.rect.x < 315:
                self.speed_x = random.randint(-3, 3)
            elif self.rect.x < 420:
                self.speed_x = random.randint(-5, -1)
            else:
                self.speed_x = random.randint(-5, 0)
        self.projectile_list = projectile_list
        self.speed_y = random.randint(3, 7)
        self.tick_delay = tick_delay

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.tick == 0:
            projectile = Projectile(self.rect.center, self.projectile_image)
            projectile.speed_x = self.speed_x
            projectile.speed_y = 10
            self.projectile_list.add(projectile)
            self.tick = self.tick_delay
        else:
            self.tick -= 1


class Missile(pygame.sprite.Sprite):
    speed_x = 0
    speed_y = 0

    def __init__(self, pos, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


class Projectile(Missile):
    def __init__(self, pos, img):
        Missile.__init__(self, pos, img)
        self.mask = pygame.mask.from_surface(self.image)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        img= "fighter_" + c.SELECTED_CHAR
        self.image = pygame.image.load(img).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Game(object):
    display_help_screen = False
    display_credits_screen = False
    texture_increment = -480
    tick = 30  # 30 fps = 1 second
    tick_delay = 35
    level = 1
    running = True
    menu_choice = 0
    score_text = None
    level_text = None

    def __init__(self):
        self.player = Player()
        self.player_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.missile_list = pygame.sprite.Group()
        self.projectile_list = pygame.sprite.Group()
        self.player_list.add(self.player)
        # ---------------------------------------------------------------
        self.font = pygame.font.Font(None, 20)  # text font...
        self.menu_text = []
        # -----------Menu Texts------------------------------------------

        # ---------------------------------------------------------------
        self.explosion = Explosion()

    def start_game(self):
        self.running = True
        c.SOUNDS["plane"].play(-1)  # Start the plane sound;
        self.terminate_count_down = 150
        self.terminate = False
        self.score = 0
        if len(self.enemy_list) > 0:
            self.enemy_list.empty()
        if len(self.missile_list) > 0:
            self.missile_list.empty()
        if len(self.projectile_list) > 0:
            self.projectile_list.empty()
        self.tick_delay = 35
        self.level = 1
        self.score_text = self.font.render("Score: 0", True, (255, 255, 255))
        self.level_text = self.font.render("Level: 1", True, (255, 255, 255))

    def run_game(self):
        if not self.terminate:
            self.player.update()
        self.enemy_list.update()
        self.missile_list.update()
        self.projectile_list.update()

        for missile in self.missile_list:
            if missile.rect.x < 0 or missile.rect.x > 800:
                self.missile_list.remove(missile)
            elif missile.rect.y < - 40 or missile.rect.y > 600:
                self.missile_list.remove(missile)

        for projectile in self.projectile_list:
            if projectile.rect.x < 0 or projectile.rect.x > 800:
                self.projectile_list.remove(projectile)
            elif projectile.rect.y < - 20 or projectile.rect.y > 600:
                self.projectile_list.remove(projectile)

        for enemy in self.enemy_list:
            if enemy.rect.x < -120 or enemy.rect.x > 800:
                self.enemy_list.remove(enemy)
            elif enemy.rect.y < -100 or enemy.rect.y > 600:
                self.enemy_list.remove(enemy)

        for enemy in self.enemy_list:
            hit_list = pygame.sprite.spritecollide(enemy, self.missile_list, True)
            if len(hit_list) > 0:
                self.explosion.add((enemy.rect.x + 20, enemy.rect.y + 20))
                self.enemy_list.remove(enemy)
                self.score += 1
                if self.level == 1:
                    if self.score == 50:
                        self.level += 1
                        self.tick_delay = 25
                        self.level_text = self.font.render("Level: " + str(self.level), True, (255, 255, 255))
                elif self.level == 2:
                    if self.score == 100:
                        self.level += 1
                        self.tick_delay = 15
                        self.level_text = self.font.render("Level: " + str(self.level), True, (255, 255, 255))
                self.score_text = self.font.render("Score: " + str(self.score), True, (255, 255, 255))

        hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, False, pygame.sprite.collide_mask)
        if len(hit_list) > 0 and not self.terminate:
            self.terminate = True
            self.explosion.add(self.player.rect.topleft)
            c.SOUNDS["plane"].stop()
            for enemy in hit_list:
                self.explosion.add(enemy.rect.topleft)
                self.enemy_list.remove(enemy)

        hit_list = pygame.sprite.spritecollide(self.player, self.projectile_list, False, pygame.sprite.collide_mask)
        if len(hit_list) > 0 and not self.terminate:
            self.terminate = True
            self.explosion.add(self.player.rect.topleft)
            c.SOUNDS["plane"].stop()
            for projectile in hit_list:
                self.projectile_list.remove(projectile)

        if self.tick == 0:
            enemy = Enemy(random.choice((c.IMAGES["enemy1"], c.IMAGES["enemy2"], c.IMAGES["enemy3"])), self.projectile_list,
                          self.tick_delay)
            enemy.projectile_image = c.IMAGES["projectile"]
            self.enemy_list.add(enemy)
            self.tick = self.tick_delay
        else:
            self.tick -= 1

        if self.texture_increment == 0:
            self.texture_increment = -480
        else:
            self.texture_increment += 1

        if self.terminate:
            if self.terminate_count_down == 0:
                self.running = False
            else:
                self.terminate_count_down -= 1

    def display_frame(self, screen):
        if self.running:
            screen.blit(c.IMAGES["ocean"], (0, self.texture_increment))
            self.missile_list.draw(screen)
            self.projectile_list.draw(screen)
            self.enemy_list.draw(screen)
            if not self.terminate:
                self.player_list.draw(screen)
            screen.blit(self.score_text, (75, 20))
            screen.blit(self.level_text, (285, 20))
            self.explosion.draw(screen)
            if self.terminate_count_down <= 90:
                screen.blit(c.IMAGES["gameOver"], (200, 200))
        else:
            c.STATE="MENU"

    def shoot(self):
        missile = Missile(self.player.rect.center, c.IMAGES["missile"])
        missile.speed_y = -10
        self.missile_list.add(missile)

