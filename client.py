import pygame
from network import Network
import random

# initiating game window
pygame.init()

game = True
window_width = 1120
window_lenght = 630
window = pygame.display.set_mode((window_width, window_lenght))

# fonts
pixel_font_head = pygame.font.Font('data/font/Pixeltype.ttf', 50)
pixel_font_head2 = pygame.font.Font('data/font/Pixeltype.ttf', 80)
pixel_font_text = pygame.font.Font('data/font/Pixeltype.ttf', 30)
pixel_font_text2 = pygame.font.Font('data/font/Pixeltype.ttf', 20)


# player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.gravity = 0
        self.speed = 5
        self.face_r = True
        self.x = x
        self.y = y
        self.punch1 = False
        self.punch2 = False
        self.punch3 = False
        self.punch = 0
        self.kick1 = False
        self.kick2 = False
        self.kick = 0
        self.runpunch = False
        self.last_p = pygame.time.get_ticks()
        self.last_k = pygame.time.get_ticks()
        self.last_rp = pygame.time.get_ticks()
        self.cooldown = 250
        self.cont = 150
        self.last_atk = pygame.time.get_ticks()
        self.atkcooldown = 69
        self.test = 0
        self.health = 400
        self.game_active = False
        self.ready = False
        self.start = False
        self.rematch = False

        # idle_r
        player_idle_r1 = pygame.image.load('data/graphics/player/idle_r1.png').convert_alpha()
        player_idle_r2 = pygame.image.load('data/graphics/player/idle_r2.png').convert_alpha()
        player_idle_r3 = pygame.image.load('data/graphics/player/idle_r3.png').convert_alpha()
        player_idle_r4 = pygame.image.load('data/graphics/player/idle_r4.png').convert_alpha()

        self.player_idle_r_l = [player_idle_r1, player_idle_r2, player_idle_r3, player_idle_r4]
        self.player_idle_i = 0

        # idle_l
        player_idle_l1 = pygame.image.load('data/graphics/player/idle_l1.png').convert_alpha()
        player_idle_l2 = pygame.image.load('data/graphics/player/idle_l2.png').convert_alpha()
        player_idle_l3 = pygame.image.load('data/graphics/player/idle_l3.png').convert_alpha()
        player_idle_l4 = pygame.image.load('data/graphics/player/idle_l4.png').convert_alpha()

        self.player_idle_l_l = [player_idle_l1, player_idle_l2, player_idle_l3, player_idle_l4]

        # jump_r
        player_jump_r3 = pygame.image.load('data/graphics/player/jump_r3.png').convert_alpha()
        player_jump_r5 = pygame.image.load('data/graphics/player/jump_r5.png').convert_alpha()
        self.player_jump_r_l = [player_jump_r3, player_jump_r5]

        # jump_l
        player_jump_l3 = pygame.image.load('data/graphics/player/jump_l3.png').convert_alpha()
        player_jump_l5 = pygame.image.load('data/graphics/player/jump_l5.png').convert_alpha()
        self.player_jump_l_l = [player_jump_l3, player_jump_l5]

        # run_r
        player_run_r1 = pygame.image.load('data/graphics/player/run_r1.png').convert_alpha()
        player_run_r2 = pygame.image.load('data/graphics/player/run_r2.png').convert_alpha()
        player_run_r3 = pygame.image.load('data/graphics/player/run_r3.png').convert_alpha()
        player_run_r4 = pygame.image.load('data/graphics/player/run_r4.png').convert_alpha()
        player_run_r5 = pygame.image.load('data/graphics/player/run_r5.png').convert_alpha()
        player_run_r6 = pygame.image.load('data/graphics/player/run_r6.png').convert_alpha()

        self.player_run_r_l = [player_run_r1, player_run_r2, player_run_r3, player_run_r4, player_run_r5, player_run_r6]
        self.player_run_i = 0

        # run_l
        player_run_l1 = pygame.image.load('data/graphics/player/run_l1.png').convert_alpha()
        player_run_l2 = pygame.image.load('data/graphics/player/run_l2.png').convert_alpha()
        player_run_l3 = pygame.image.load('data/graphics/player/run_l3.png').convert_alpha()
        player_run_l4 = pygame.image.load('data/graphics/player/run_l4.png').convert_alpha()
        player_run_l5 = pygame.image.load('data/graphics/player/run_l5.png').convert_alpha()
        player_run_l6 = pygame.image.load('data/graphics/player/run_l6.png').convert_alpha()

        self.player_run_l_l = [player_run_l1, player_run_l2, player_run_l3, player_run_l4, player_run_l5, player_run_l6]

        # punch_r
        player_punch_r1 = pygame.image.load('data/graphics/player/punch_r1.png').convert_alpha()
        player_punch_r2 = pygame.image.load('data/graphics/player/punch_r2.png').convert_alpha()
        player_punch_r3 = pygame.image.load('data/graphics/player/punch_r3.png').convert_alpha()
        player_punch_r4 = pygame.image.load('data/graphics/player/punch_r4.png').convert_alpha()
        player_punch_r5 = pygame.image.load('data/graphics/player/punch_r5.png').convert_alpha()
        player_punch_r6 = pygame.image.load('data/graphics/player/punch_r6.png').convert_alpha()
        player_punch_r7 = pygame.image.load('data/graphics/player/punch_r7.png').convert_alpha()
        player_punch_r8 = pygame.image.load('data/graphics/player/punch_r8.png').convert_alpha()
        player_punch_r9 = pygame.image.load('data/graphics/player/punch_r9.png').convert_alpha()
        player_punch_r10 = pygame.image.load('data/graphics/player/punch_r10.png').convert_alpha()
        player_punch_r11 = pygame.image.load('data/graphics/player/punch_r11.png').convert_alpha()
        player_punch_r12 = pygame.image.load('data/graphics/player/punch_r12.png').convert_alpha()
        player_punch_r13 = pygame.image.load('data/graphics/player/punch_r13.png').convert_alpha()

        self.player_punch_r_l = [player_punch_r1, player_punch_r2, player_punch_r3, player_punch_r4, player_punch_r5,
                                 player_punch_r6, player_punch_r7, player_punch_r8, player_punch_r9, player_punch_r10,
                                 player_punch_r11, player_punch_r12, player_punch_r13]
        self.player_punch_r_i = 0

        # punch_l
        player_punch_l1 = pygame.image.load('data/graphics/player/punch_l1.png').convert_alpha()
        player_punch_l2 = pygame.image.load('data/graphics/player/punch_l2.png').convert_alpha()
        player_punch_l3 = pygame.image.load('data/graphics/player/punch_l3.png').convert_alpha()
        player_punch_l4 = pygame.image.load('data/graphics/player/punch_l4.png').convert_alpha()
        player_punch_l5 = pygame.image.load('data/graphics/player/punch_l5.png').convert_alpha()
        player_punch_l6 = pygame.image.load('data/graphics/player/punch_l6.png').convert_alpha()
        player_punch_l7 = pygame.image.load('data/graphics/player/punch_l7.png').convert_alpha()
        player_punch_l8 = pygame.image.load('data/graphics/player/punch_l8.png').convert_alpha()
        player_punch_l9 = pygame.image.load('data/graphics/player/punch_l9.png').convert_alpha()
        player_punch_l10 = pygame.image.load('data/graphics/player/punch_l10.png').convert_alpha()
        player_punch_l11 = pygame.image.load('data/graphics/player/punch_l11.png').convert_alpha()
        player_punch_l12 = pygame.image.load('data/graphics/player/punch_l12.png').convert_alpha()
        player_punch_l13 = pygame.image.load('data/graphics/player/punch_l13.png').convert_alpha()

        self.player_punch_l_l = [player_punch_l1, player_punch_l2, player_punch_l3, player_punch_l4, player_punch_l5,
                                 player_punch_l6, player_punch_l7, player_punch_l8, player_punch_l9, player_punch_l10,
                                 player_punch_l11, player_punch_l12, player_punch_l13]
        self.player_punch_l_i = 0

        # kick_r
        player_kick_r1 = pygame.image.load('data/graphics/player/kick_r1.png').convert_alpha()
        player_kick_r2 = pygame.image.load('data/graphics/player/kick_r2.png').convert_alpha()
        player_kick_r3 = pygame.image.load('data/graphics/player/kick_r3.png').convert_alpha()
        player_kick_r4 = pygame.image.load('data/graphics/player/kick_r4.png').convert_alpha()
        player_kick_r5 = pygame.image.load('data/graphics/player/kick_r5.png').convert_alpha()
        player_kick_r6 = pygame.image.load('data/graphics/player/kick_r6.png').convert_alpha()
        player_kick_r7 = pygame.image.load('data/graphics/player/kick_r7.png').convert_alpha()
        player_kick_r8 = pygame.image.load('data/graphics/player/kick_r8.png').convert_alpha()

        self.player_kick_r_l = [player_kick_r1, player_kick_r2, player_kick_r3, player_kick_r4, player_kick_r5,
                                player_kick_r6, player_kick_r7, player_kick_r8]
        self.player_kick_r_i = 0

        # kick_l
        player_kick_l1 = pygame.image.load('data/graphics/player/kick_l1.png').convert_alpha()
        player_kick_l2 = pygame.image.load('data/graphics/player/kick_l2.png').convert_alpha()
        player_kick_l3 = pygame.image.load('data/graphics/player/kick_l3.png').convert_alpha()
        player_kick_l4 = pygame.image.load('data/graphics/player/kick_l4.png').convert_alpha()
        player_kick_l5 = pygame.image.load('data/graphics/player/kick_l5.png').convert_alpha()
        player_kick_l6 = pygame.image.load('data/graphics/player/kick_l6.png').convert_alpha()
        player_kick_l7 = pygame.image.load('data/graphics/player/kick_l7.png').convert_alpha()
        player_kick_l8 = pygame.image.load('data/graphics/player/kick_l8.png').convert_alpha()

        self.player_kick_l_l = [player_kick_l1, player_kick_l2, player_kick_l3, player_kick_l4, player_kick_l5,
                                player_kick_l6, player_kick_l7, player_kick_l8]
        self.player_kick_l_i = 0

        # runpunch_r
        player_runpunch_r1 = pygame.image.load('data/graphics/player/runpunch_r1.png').convert_alpha()
        player_runpunch_r2 = pygame.image.load('data/graphics/player/runpunch_r2.png').convert_alpha()
        player_runpunch_r3 = pygame.image.load('data/graphics/player/runpunch_r3.png').convert_alpha()
        player_runpunch_r4 = pygame.image.load('data/graphics/player/runpunch_r4.png').convert_alpha()
        player_runpunch_r5 = pygame.image.load('data/graphics/player/runpunch_r5.png').convert_alpha()
        player_runpunch_r6 = pygame.image.load('data/graphics/player/runpunch_r6.png').convert_alpha()
        player_runpunch_r7 = pygame.image.load('data/graphics/player/runpunch_r7.png').convert_alpha()

        self.player_runpunch_r_l = [player_runpunch_r1, player_runpunch_r2, player_runpunch_r3, player_runpunch_r4,
                                    player_runpunch_r5, player_runpunch_r6, player_runpunch_r7]
        self.player_runpunch_r_i = 0

        # runpunch_l
        player_runpunch_l1 = pygame.image.load('data/graphics/player/runpunch_l1.png').convert_alpha()
        player_runpunch_l2 = pygame.image.load('data/graphics/player/runpunch_l2.png').convert_alpha()
        player_runpunch_l3 = pygame.image.load('data/graphics/player/runpunch_l3.png').convert_alpha()
        player_runpunch_l4 = pygame.image.load('data/graphics/player/runpunch_l4.png').convert_alpha()
        player_runpunch_l5 = pygame.image.load('data/graphics/player/runpunch_l5.png').convert_alpha()
        player_runpunch_l6 = pygame.image.load('data/graphics/player/runpunch_l6.png').convert_alpha()
        player_runpunch_l7 = pygame.image.load('data/graphics/player/runpunch_l7.png').convert_alpha()

        self.player_runpunch_l_l = [player_runpunch_l1, player_runpunch_l2, player_runpunch_l3, player_runpunch_l4,
                                    player_runpunch_l5, player_runpunch_l6, player_runpunch_l7]
        self.player_runpunch_l_i = 0

        # lost_r
        player_lost_r1 = pygame.image.load('data/graphics/player/lost_r1.png').convert_alpha()
        player_lost_r2 = pygame.image.load('data/graphics/player/lost_r2.png').convert_alpha()
        player_lost_r3 = pygame.image.load('data/graphics/player/lost_r3.png').convert_alpha()
        player_lost_r4 = pygame.image.load('data/graphics/player/lost_r4.png').convert_alpha()
        player_lost_r5 = pygame.image.load('data/graphics/player/lost_r5.png').convert_alpha()
        player_lost_r6 = pygame.image.load('data/graphics/player/lost_r6.png').convert_alpha()
        player_lost_r7 = pygame.image.load('data/graphics/player/lost_r7.png').convert_alpha()

        self.player_lost_r_l = [player_lost_r1, player_lost_r2, player_lost_r3, player_lost_r4, player_lost_r5,
                                player_lost_r6, player_lost_r7]
        self.player_lost_r_i = 0

        # lost_l
        player_lost_l1 = pygame.image.load('data/graphics/player/lost_l1.png').convert_alpha()
        player_lost_l2 = pygame.image.load('data/graphics/player/lost_l2.png').convert_alpha()
        player_lost_l3 = pygame.image.load('data/graphics/player/lost_l3.png').convert_alpha()
        player_lost_l4 = pygame.image.load('data/graphics/player/lost_l4.png').convert_alpha()
        player_lost_l5 = pygame.image.load('data/graphics/player/lost_l5.png').convert_alpha()
        player_lost_l6 = pygame.image.load('data/graphics/player/lost_l6.png').convert_alpha()
        player_lost_l7 = pygame.image.load('data/graphics/player/lost_l7.png').convert_alpha()

        self.player_lost_l_l = [player_lost_l1, player_lost_l2, player_lost_l3, player_lost_l4, player_lost_l5,
                                player_lost_l6, player_lost_l7]
        self.player_lost_l_i = 0

    def assignp1(self):
        self.face_r = True
        self.player_surf = self.player_idle_r_l[int(self.player_idle_i)]
        self.player_rect = self.player_surf.get_rect()
        self.player_rect.midbottom = (self.x, self.y)

    def assignp2(self):
        self.face_r = False
        self.player_surf = self.player_idle_l_l[int(self.player_idle_i)]
        self.player_rect = self.player_surf.get_rect()
        self.player_rect.midbottom = (self.x, self.y)

    def player_animation(self):
        keys = pygame.key.get_pressed()
        nowp = pygame.time.get_ticks()
        nowk = pygame.time.get_ticks()
        nowrp = pygame.time.get_ticks()
        # punch-cooldown
        if nowp - self.last_p >= self.cooldown:
            if self.punch == 0:
                if keys[pygame.K_j] and not (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_k] or keys[
                        pygame.K_l]) and self.player_rect.bottom == 595:
                    self.last_p = nowp
                    self.punch += 1
                    self.punch1 = True
                    self.punch2 = False
                    self.punch3 = False
                else:
                    self.punch1 = False
                    self.punch2 = False
                    self.punch3 = False
                    self.player_punch_r_i = 0
                    self.player_punch_l_i = 0
                    self.punch = 0
            elif self.punch == 1:
                if (self.last_p + 600) - nowp >= self.cont:
                    if keys[pygame.K_j] and not (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_k] or keys[
                            pygame.K_l]) and self.player_rect.bottom == 595:
                        self.last_p = nowp
                        self.punch += 1
                        self.punch1 = False
                        self.punch2 = True
                        self.punch3 = False
                else:
                    self.player_punch_r_i = 0
                    self.player_punch_l_i = 0
                    self.punch = 0
            elif self.punch == 2:
                if (self.last_p + 600) - nowp >= self.cont:
                    if keys[pygame.K_j] and not (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_k] or keys[
                            pygame.K_l]) and self.player_rect.bottom == 595:
                        self.last_p = nowp
                        self.punch += 1
                        self.punch1 = False
                        self.punch2 = False
                        self.punch3 = True

                else:
                    self.player_punch_r_i = 0
                    self.player_punch_l_i = 0
                    self.punch = 0

            elif self.punch == 3:
                if (self.last_p + 600) - nowp >= self.cont:
                    if keys[pygame.K_j] and not (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_k] or keys[
                            pygame.K_l]) and self.player_rect.bottom == 595:
                        self.last_p = nowp
                        self.punch += 1
                        self.punch1 = False
                        self.punch2 = False
                        self.punch3 = True

                else:
                    self.player_punch_r_i = 0
                    self.player_punch_l_i = 0
                    self.punch = 0

            elif self.punch == 4:
                self.punch1 = False
                self.punch2 = False
                self.punch3 = False
                self.player_punch_r_i = 0
                self.player_punch_l_i = 0
                self.punch = 0

        # kick-cooldown
        if nowk - self.last_k >= self.cooldown:
            if self.kick == 0:
                if keys[pygame.K_k] and not (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_j] or keys[
                        pygame.K_l]) and self.player_rect.bottom == 595:
                    self.last_k = nowk
                    self.kick += 1
                    self.kick1 = True
                    self.kick2 = False
                else:
                    self.player_kick_r_i = 0
                    self.player_kick_l_i = 0
                    self.kick = 0
            elif self.kick == 1:
                if (self.last_k + 500) - nowk >= self.cont:
                    if keys[pygame.K_k] and not (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_j] or keys[
                            pygame.K_l]) and self.player_rect.bottom == 595:
                        self.last_k = nowk
                        self.kick += 1
                        self.kick1 = False
                        self.kick2 = True
                else:
                    self.player_kick_r_i = 0
                    self.player_kick_l_i = 0
                    self.kick = 0
            elif self.kick == 2:
                self.kick = 0
                self.kick1 = False
                self.kick2 = False

                self.player_kick_r_i = 0
                self.player_kick_l_i = 0
                self.kick = 0

        # runpunch_cooldown
        if nowrp - self.last_rp >= 5000:
            if keys[pygame.K_l] and not (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_j] or keys[
                    pygame.K_k]) and self.player_rect.bottom == 595:
                self.last_rp = nowrp
                self.runpunch = True

        # runpunch_r
        if (self.player_rect.bottom == 595 and (self.runpunch)) and self.face_r:
            self.player_idle_i = 0
            self.player_run_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_punch_r_i = 0
            self.player_punch_l_i = 0

            self.player_runpunch_r_i += 0.25
            if self.player_runpunch_r_i >= 7:
                self.player_runpunch_r_i = 0
                self.runpunch = False
                self.player_rect = self.player_surf.get_rect(midbottom=(self.player_rect.center[0], 595))
            self.player_surf = self.player_runpunch_r_l[int(self.player_runpunch_r_i)]
            self.player_rect = self.player_surf.get_rect(bottomleft=(self.player_rect.left, 595))
            if int(self.player_runpunch_r_i) == 3:
                self.player_rect.x += 10
                self.hitrect(self.player_rect.center[0], self.player_rect.center[1], 60, 60, True, 3, 3, 8, 8)

        # runpunch_l
        elif (self.player_rect.bottom == 595 and (self.runpunch)) and not self.face_r:
            self.player_idle_i = 0
            self.player_run_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_punch_r_i = 0
            self.player_punch_l_i = 0

            self.player_runpunch_l_i += 0.25
            if self.player_runpunch_l_i >= 7:
                self.player_runpunch_l_i = 0
                self.runpunch = False
                self.player_rect = self.player_surf.get_rect(midbottom=(self.player_rect.center[0], 595))
            self.player_surf = self.player_runpunch_l_l[int(self.player_runpunch_l_i)]
            self.player_rect = self.player_surf.get_rect(bottomright=(self.player_rect.right, 595))
            if int(self.player_runpunch_l_i) == 3:
                self.player_rect.x -= 10
                self.hitrect(self.player_rect.center[0], self.player_rect.center[1], 60, 60, False, 3, 3, 8, 8)

        # punch_r
        elif (self.player_rect.bottom == 595 and (self.punch1 or self.punch2 or self.punch3)) and self.face_r:
            self.player_idle_i = 0
            self.player_run_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_runpunch_r_i = 0
            self.player_runpunch_l_i = 0
            if self.punch1 and not (self.punch2 or self.punch3):
                self.player_punch_r_i += 0.2
                if self.player_punch_r_i >= 4:
                    self.punch1 = False
                    if self.punch2 == False:
                        self.player_punch_r_i = 0

            elif self.punch2 and not (self.punch3):
                self.player_punch_r_i += 0.2
                if self.player_punch_r_i >= 8:
                    self.punch1 = False
                    self.punch2 = False
                    if self.punch3 == False:
                        self.player_punch_r_i = 0

            elif self.punch3:
                self.player_punch_r_i += 0.2
                if self.player_punch_r_i >= 13:
                    self.player_punch_r_i = 0
                    self.punch1 = False
                    self.punch2 = False
                    self.punch3 = False
            if int(self.player_punch_r_i) == 2 or int(self.player_punch_r_i) == 6 or int(self.player_punch_r_i) == 10:
                self.hitrect(self.player_rect.center[0], self.player_rect.center[1], 60, 60, True, 1, 1, 4, 4)

            self.player_surf = self.player_punch_r_l[int(self.player_punch_r_i)]
            self.player_rect = self.player_surf.get_rect(bottomleft=(self.player_rect.x, 595))

        # punch_l
        elif (self.player_rect.bottom == 595 and (self.punch1 or self.punch2 or self.punch3)) and not self.face_r:
            self.player_idle_i = 0
            self.player_run_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_runpunch_i = 0
            if self.punch1 and not (self.punch2 or self.punch3):
                self.player_punch_l_i += 0.2
                if self.player_punch_l_i >= 4:
                    self.punch1 = False
                    if self.punch2 == False:
                        self.player_punch_l_i = 0

            elif self.punch2 and not (self.punch3):
                self.player_punch_l_i += 0.2
                if self.player_punch_l_i >= 8:
                    self.punch1 = False
                    self.punch2 = False
                    if self.punch3 == False:
                        self.player_punch_l_i = 0

            elif self.punch3:
                self.player_punch_l_i += 0.2
                if self.player_punch_l_i >= 13:
                    self.player_punch_l_i = 0
                    self.punch1 = False
                    self.punch2 = False
                    self.punch3 = False
            if int(self.player_punch_l_i) == 2 or int(self.player_punch_l_i) == 6 or int(self.player_punch_l_i) == 10:
                self.hitrect(self.player_rect.center[0], self.player_rect.center[1], 60, 60, False, 1, 1, 4, 4)
            self.player_surf = self.player_punch_l_l[int(self.player_punch_l_i)]
            self.player_rect = self.player_surf.get_rect(bottomright=(self.player_rect.right, 595))

        # kick_r
        elif (self.player_rect.bottom == 595 and (self.kick1 or self.kick2)) and self.face_r:
            self.play_jump_r_i = 0
            self.player_idle_i = 0
            self.player_kick_l_i = 0
            self.player_runpunch_i = 0
            self.player_punch_r_i = 0
            self.player_punch_r_i = 0
            if self.kick1 and not (self.kick2):
                self.player_kick_r_i += 0.2
                if self.player_kick_r_i >= 4:
                    self.kick1 = False
                    if self.kick2 == False:
                        self.player_kick_r_i = 0
                if int(self.player_kick_r_i) == 2:
                    self.hitrect(self.player_rect.center[0], self.player_rect.center[1], 60, 60, True, 1, 1, 3, 3)
                self.player_surf = self.player_kick_r_l[(int(self.player_kick_r_i))]
                self.player_rect = self.player_surf.get_rect(bottomleft=(self.player_rect.left, 595))
            elif self.kick2:
                self.player_kick_r_i += 0.2
                if self.player_kick_r_i >= 8:
                    self.player_kick_r_i = 0
                    self.kick1 = False
                    self.kick2 = False
                if int(self.player_kick_r_i) == 5:
                    self.hitrect(self.player_rect.center[0], self.player_rect.center[1], 60, 60, True, 1, 1, 3, 3)
                self.player_surf = self.player_kick_r_l[(int(self.player_kick_r_i))]
                self.player_rect = self.player_surf.get_rect(bottomleft=(self.player_rect.left, 595))

        # kick_l
        elif (self.player_rect.bottom == 595 and (self.kick1 or self.kick2)) and not self.face_r:
            self.play_jump_r_i = 0
            self.player_idle_i = 0
            self.player_run_r_i = 0
            self.player_kick_r_i = 0
            self.player_runpunch_i = 0
            self.player_punch_r_i = 0
            self.player_punch_l_i = 0
            if self.kick1 and not (self.kick2):
                self.player_kick_l_i += 0.2
                if self.player_kick_l_i >= 4:
                    self.kick1 = False
                    if self.kick2 == False:
                        self.player_kick_l_i = 0
                if int(self.player_kick_l_i) == 2:
                    self.hitrect(self.player_rect.center[0], self.player_rect.center[1], 60, 60, False, 1, 1, 4, 4)
                self.player_surf = self.player_kick_l_l[(int(self.player_kick_l_i))]
                self.player_rect = self.player_surf.get_rect(bottomright=(self.player_rect.right, 595))
            elif self.kick2:
                self.player_kick_l_i += 0.2
                if self.player_kick_l_i >= 8:
                    self.player_kick_l_i = 0
                    self.kick1 = False
                    self.kick2 = False
                if int(self.player_kick_l_i) == 5:
                    self.hitrect(self.player_rect.center[0], self.player_rect.center[1], 60, 60, False, 1, 1, 4, 4)
                self.player_surf = self.player_kick_l_l[(int(self.player_kick_l_i))]
                self.player_rect = self.player_surf.get_rect(bottomright=(self.player_rect.right, 595))

        # idle_r
        elif ((((self.player_rect.bottom == 595 and not (keys[pygame.K_a] or keys[pygame.K_d])) or (
                self.player_rect.bottom == 595 and (keys[pygame.K_a] and keys[pygame.K_d]))) and self.face_r)):
            self.play_jump_r_i = 0
            self.player_run_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_runpunch_i = 0
            self.player_punch_i = 0
            self.player_idle_i += 0.1
            if self.player_idle_i >= len(self.player_idle_r_l): self.player_idle_i = 0
            self.player_surf = self.player_idle_r_l[int(self.player_idle_i)]
            self.player_rect = self.player_surf.get_rect(bottomleft=(self.player_rect.x, 595))

        # idle_l
        elif ((((self.player_rect.bottom == 595 and not (keys[pygame.K_a] or keys[pygame.K_d])) or (
                self.player_rect.bottom == 595 and (keys[pygame.K_a] and keys[pygame.K_d]))) and not self.face_r)):
            self.play_jump_l_i = 0
            self.player_run_l_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_runpunch_i = 0
            self.player_punch_i = 0
            self.player_idle_i += 0.1
            if self.player_idle_i >= len(self.player_idle_l_l): self.player_idle_i = 0
            self.player_surf = self.player_idle_l_l[int(self.player_idle_i)]
            self.player_rect = self.player_surf.get_rect(bottomright=(self.player_rect.right, 595))

        # jump_r
        elif (self.player_rect.bottom < 594 and self.face_r):
            if keys[pygame.K_a] and not (keys[pygame.K_d]):
                self.face_r = False
            self.player_idle_i = 0
            self.player_run_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_runpunch_i = 0
            self.player_punch_i = 0
            if self.gravity < 0:
                self.player_surf = self.player_jump_r_l[0]
            else:
                self.player_surf = self.player_jump_r_l[1]

        # jump_l
        elif (self.player_rect.bottom < 594 and not self.face_r):
            if keys[pygame.K_d] and not (keys[pygame.K_a]):
                self.face_r = True
            self.player_idle_i = 0
            self.player_run_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_runpunch_i = 0
            self.player_punch_i = 0
            if self.gravity < 0:
                self.player_surf = self.player_jump_l_l[0]
            else:
                self.player_surf = self.player_jump_l_l[1]

                # run_r
        elif (keys[pygame.K_d] and self.player_rect.bottom >= 595):
            self.face_r = True
            self.play_jump_r_i = 0
            self.player_idle_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_runpunch_i = 0
            self.player_punch_i = 0
            self.player_run_i += 0.13
            if self.player_run_i >= len(self.player_run_r_l): self.player_run_i = 0
            self.player_surf = self.player_run_r_l[int(self.player_run_i)]
            self.player_rect = self.player_surf.get_rect(bottomleft=(self.player_rect.x, 595))

        # run_l
        elif (keys[pygame.K_a] and self.player_rect.bottom >= 595):
            self.face_r = False
            self.play_jump_r_i = 0
            self.player_idle_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_runpunch_i = 0
            self.player_punch_i = 0
            self.player_run_i += 0.13
            if self.player_run_i >= len(self.player_run_l_l): self.player_run_i = 0
            self.player_surf = self.player_run_l_l[int(self.player_run_i)]
            self.player_rect = self.player_surf.get_rect(bottomright=(self.player_rect.right, 595))

    def p_animation(self):
        global p2x, p2y

        # runpunch_r
        if (self.player_rect.bottom == 595 and (p2rp)) and self.face_r:
            self.player_idle_i = 0
            self.player_run_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_punch_r_i = 0
            self.player_punch_l_i = 0

            self.player_runpunch_r_i += 0.25
            if self.player_runpunch_r_i >= 7:
                self.player_runpunch_r_i = 0
                self.player_rect = self.player_surf.get_rect(midbottom=(self.player_rect.center[0], 595))
            self.player_surf = self.player_runpunch_r_l[int(self.player_runpunch_r_i)]
            self.player_rect = self.player_surf.get_rect(bottomleft=(self.player_rect.left, 595))
            if int(self.player_runpunch_r_i) == 3:
                self.player_rect.x += 10
                self.hitrect(self.player_rect.center[0], self.player_rect.center[1], 60, 60, True, 10, 10, 25, 25)

        # runpunch_l
        elif (self.player_rect.bottom == 595 and (p2rp)) and not self.face_r:
            self.player_idle_i = 0
            self.player_run_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_punch_r_i = 0
            self.player_punch_l_i = 0

            self.player_runpunch_l_i += 0.25
            if self.player_runpunch_l_i >= 7:
                self.player_runpunch_l_i = 0
                self.player_rect = self.player_surf.get_rect(midbottom=(self.player_rect.center[0], 595))
            self.player_surf = self.player_runpunch_l_l[int(self.player_runpunch_l_i)]
            self.player_rect = self.player_surf.get_rect(bottomright=(self.player_rect.right, 595))
            if int(self.player_runpunch_l_i) == 3:
                self.player_rect.x -= 10
                self.hitrect(self.player_rect.center[0], self.player_rect.center[1], 60, 60, False, 10, 10, 25, 25)

        # punch_r
        elif (self.player_rect.bottom == 595 and (p2p1 or p2p2 or p2p3)) and self.face_r:
            self.player_idle_i = 0
            self.player_run_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_runpunch_i = 0
            if p2p1 and not (p2p2 or p2p3):
                self.player_punch_r_i += 0.2
                if self.player_punch_r_i >= 4:
                    if p2p2 == False:
                        self.player_punch_r_i = 0

            elif p2p2 and not (p2p3):
                self.player_punch_r_i += 0.2
                if self.player_punch_r_i >= 8:
                    if p2p3 == False:
                        self.player_punch_r_i = 0

            elif p2p3:
                self.player_punch_r_i += 0.2
                if self.player_punch_r_i >= 13:
                    self.player_punch_r_i = 0
            if int(self.player_punch_r_i) == 2 or int(self.player_punch_r_i) == 6 or int(self.player_punch_r_i) == 10:
                self.hitrect(self.player_rect.center[0], self.player_rect.center[1], 60, 60, True, 8, 8, 16, 16)
            self.player_surf = self.player_punch_r_l[int(self.player_punch_r_i)]
            self.player_rect = self.player_surf.get_rect(bottomleft=(self.player_rect.x, 595))

        # punch_l
        elif (self.player_rect.bottom == 595 and (p2p1 or p2p2 or p2p3)) and not self.face_r:
            self.player_idle_i = 0
            self.player_run_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_runpunch_i = 0
            if p2p1 and not (p2p2 or p2p3):
                self.player_punch_l_i += 0.2
                if self.player_punch_l_i >= 4:
                    if p2p2 == False:
                        self.player_punch_l_i = 0

            elif p2p2 and not (p2p3):
                self.player_punch_l_i += 0.2
                if self.player_punch_l_i >= 8:
                    if p2p3 == False:
                        self.player_punch_l_i = 0

            elif p2p3:
                self.player_punch_l_i += 0.2
                if self.player_punch_l_i >= 13:
                    self.player_punch_l_i = 0
            if int(self.player_punch_l_i) == 2 or int(self.player_punch_l_i) == 6 or int(self.player_punch_l_i) == 10:
                self.hitrect(self.player_rect.center[0], self.player_rect.center[1], 60, 60, False, 8, 8, 16 ,16)
            self.player_surf = self.player_punch_l_l[int(self.player_punch_l_i)]
            self.player_rect = self.player_surf.get_rect(bottomright=(self.player_rect.right, 595))

        # kick_r
        elif (self.player_rect.bottom == 595 and (p2k1 or p2k2)) and self.face_r:
            self.play_jump_r_i = 0
            self.player_idle_i = 0
            self.player_kick_l_i = 0
            self.player_runpunch_i = 0
            self.player_punch_r_i = 0
            self.player_punch_r_i = 0
            if p2k1 and not (p2k2):
                self.player_kick_r_i += 0.2
                if self.player_kick_r_i >= 4:
                    if p2k2 == False:
                        self.player_kick_r_i = 0
                if self.player_kick_r_i == 2:
                    self.hitrect(self.player_rect.center[0], self.player_rect.center[1], 60, 60, True, 5, 5, 15, 15)
                self.player_surf = self.player_kick_r_l[(int(self.player_kick_r_i))]
                self.player_rect = self.player_surf.get_rect(bottomleft=(self.player_rect.left, 595))
            elif p2k2:
                self.player_kick_r_i += 0.2
                if self.player_kick_r_i >= 8:
                    self.player_kick_r_i = 0
                if self.player_kick_r_i == 5:
                    self.hitrect(self.player_rect.center[0], self.player_rect.center[1], 60, 60, True, 5, 5, 15, 15)
                self.player_surf = self.player_kick_r_l[(int(self.player_kick_r_i))]
                self.player_rect = self.player_surf.get_rect(bottomleft=(self.player_rect.left, 595))

        # kick_l
        elif (self.player_rect.bottom == 595 and (p2k1 or p2k2)) and not self.face_r:
            self.play_jump_r_i = 0
            self.player_idle_i = 0
            self.player_run_r_i = 0
            self.player_kick_r_i = 0
            self.player_runpunch_i = 0
            self.player_punch_r_i = 0
            self.player_punch_l_i = 0
            if p2k1 and not (p2k2):
                self.player_kick_l_i += 0.2
                if self.player_kick_l_i >= 4:
                    if p2k2 == False:
                        self.player_kick_l_i = 0
                if self.player_kick_l_i == 2:
                    self.hitrect(self.player_rect.center[0], self.player_rect.center[1], 60, 60, False, 8, 8, 16, 16)
                self.player_surf = self.player_kick_l_l[(int(self.player_kick_l_i))]
                self.player_rect = self.player_surf.get_rect(bottomright=(self.player_rect.right, 595))
            elif p2k2:
                self.player_kick_l_i += 0.2
                if self.player_kick_l_i >= 8:
                    self.player_kick_l_i = 0
                if self.player_kick_l_i == 5:
                    self.hitrect(self.player_rect.center[0], self.player_rect.center[1], 60, 60, False, 8, 8, 16, 16)
                self.player_surf = self.player_kick_l_l[(int(self.player_kick_l_i))]
                self.player_rect = self.player_surf.get_rect(bottomright=(self.player_rect.right, 595))

        # idle_r
        elif (not (p2a or p2d) and p2.y == 595) and self.face_r:
            self.play_jump_r_i = 0
            self.player_run_i = 0
            self.player_punch_r_i = 0
            self.player_punch_l_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_idle_i += 0.1
            if self.player_idle_i >= len(self.player_idle_r_l): self.player_idle_i = 0
            self.player_surf = self.player_idle_r_l[int(self.player_idle_i)]
            self.player_rect = self.player_surf.get_rect(bottomleft=(self.player_rect.x, 595))

        # idle_l
        elif (not (p2a or p2d) and p2.y == 595) and not self.face_r:
            self.play_jump_l_i = 0
            self.player_run_l_i = 0
            self.player_punch_r_i = 0
            self.player_punch_l_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_idle_i += 0.1
            if self.player_idle_i >= len(self.player_idle_l_l): self.player_idle_i = 0
            self.player_surf = self.player_idle_l_l[int(self.player_idle_i)]
            self.player_rect = self.player_surf.get_rect(bottomright=(self.player_rect.right, 595))

        # jump_r
        elif p2y > p2.y and self.face_r:
            if p2a and not p2d:
                self.face_r = False
            self.player_punch_r_i = 0
            self.player_punch_l_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_idle_i = 0
            self.player_run_i = 0
            p2y = p2.y

            self.player_surf = self.player_jump_r_l[0]
        elif p2y < p2.y and self.face_r:
            if p2a and not p2d:
                self.face_r = False
            self.player_punch_r_i = 0
            self.player_punch_l_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_idle_i = 0
            self.player_run_i = 0
            self.player_surf = self.player_jump_r_l[1]
            p2y = p2.y

        # jump_l
        elif p2y > p2.y and not self.face_r:
            if p2d and not p2a:
                self.face_r = True
            self.player_punch_r_i = 0
            self.player_punch_l_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_idle_i = 0
            self.player_run_i = 0
            p2y = p2.y

            self.player_surf = self.player_jump_l_l[0]
        elif p2y < p2.y and not self.face_r:
            if p2d and not p2a:
                self.face_r = True
            self.player_punch_r_i = 0
            self.player_punch_l_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.player_idle_i = 0
            self.player_run_i = 0
            self.player_surf = self.player_jump_l_l[1]
            p2y = p2.y

        # run_r
        elif (p2d and p2.y == 595):
            if p2d:
                self.face_r = True
            self.player_punch_r_i = 0
            self.player_punch_l_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.play_jump_r_i = 0
            self.player_idle_i = 0
            self.player_run_i += 0.13
            if self.player_run_i >= len(self.player_run_r_l): self.player_run_i = 0
            self.player_surf = self.player_run_r_l[int(self.player_run_i)]
            self.player_rect = self.player_surf.get_rect(bottomleft=(self.player_rect.x, 595))
            p2x = p2.x

        # run_l
        elif (p2a and p2.y == 595):
            if p2a:
                self.face_r = False
            self.player_punch_r_i = 0
            self.player_punch_l_i = 0
            self.player_kick_r_i = 0
            self.player_kick_l_i = 0
            self.play_jump_r_i = 0
            self.player_idle_i = 0
            self.player_run_i += 0.13
            if self.player_run_i >= len(self.player_run_l_l): self.player_run_i = 0
            self.player_surf = self.player_run_l_l[int(self.player_run_i)]
            self.player_rect = self.player_surf.get_rect(bottomright=(self.player_rect.right, 595))
            p2x = p2.x

    def player_lost(self, x, y):

        if self.face_r:
            self.player_lost_r_i += 0.04
            if self.player_lost_r_i >= len(self.player_lost_r_l): self.player_lost_r_i = 5
            self.player_surf = self.player_lost_r_l[int(self.player_lost_r_i)]
            self.player_rect = self.player_surf.get_rect()
            self.player_rect.midbottom = (x, y)
        else:
            self.player_lost_l_i += 0.04
            if self.player_lost_l_i >= len(self.player_lost_l_l): self.player_lost_l_i = 5
            self.player_surf = self.player_lost_l_l[int(self.player_lost_l_i)]
            self.player_rect = self.player_surf.get_rect()
            self.player_rect.midbottom = (x, y)

    def start_p1_an(self):
        self.player_idle_i += 0.1
        if self.player_idle_i >= len(self.player_idle_r_l): self.player_idle_i = 0
        self.player_surf = self.player_idle_r_l[int(self.player_idle_i)]
        self.player_rect = self.player_surf.get_rect(bottomleft=(self.player_rect.x, 595))

    def start_p2_an(self):
        self.player_idle_i += 0.1
        if self.player_idle_i >= len(self.player_idle_l_l): self.player_idle_i = 0
        self.player_surf = self.player_idle_l_l[int(self.player_idle_i)]
        self.player_rect = self.player_surf.get_rect()
        self.player_rect.midbottom = (p2.x, p2.y)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.punch1 = False
            self.punch2 = False
            self.punch3 = False
            self.last_p = 0
            self.kick1 = False
            self.kick2 = False
            self.last_k = 0
            self.runpunch = False
            self.player_rect.x -= self.speed
        if keys[pygame.K_d]:
            self.punch1 = False
            self.punch2 = False
            self.punch3 = False
            self.last_p = 0
            self.kick1 = False
            self.kick2 = False
            self.last_k = 0
            self.runpunch = False
            self.player_rect.x += self.speed
        if (keys[pygame.K_w] or keys[pygame.K_SPACE]) and self.player_rect.bottom >= 580:
            self.punch1 = False
            self.punch2 = False
            self.punch3 = False
            self.last_p = 0
            self.kick1 = False
            self.kick2 = False
            self.last_k = 0
            self.runpunch = False
            self.gravity = -20

        if self.player_rect.left <= 0: self.player_rect.left = 0
        if self.player_rect.right >= 1120: self.player_rect.right = 1120

    def gravity_logic(self):
        self.gravity += 1
        self.player_rect.y += self.gravity
        if self.player_rect.bottom >= 595: self.player_rect.bottom = 595

    def update(self):
        self.gravity_logic()
        self.player_animation()
        self.input()

    def draw(self, win):
        win.blit(self.player_surf, self.player_rect)

    def uprect(self, x, y):
        self.p_animation()
        self.player_rect = self.player_surf.get_rect()
        self.player_rect.midbottom = (x, y)
        # self.player_animation()

    def hitrect(self, x, y, widht, height, face_r, ncr1, ncr2, cr1, cr2):

        atkrect_rect = pygame.Rect(x, y, widht, height)
        if face_r:
            atkrect_rect.midleft = (x, y)
        else:
            atkrect_rect.midright = (x, y)

        if pygame.Rect.colliderect(atkrect_rect, p2.player_rect):
            self.test += 1
            atk = self.gethit(ncr1, ncr2, cr1, cr2)
            self.health = self.hp(atk)
            # print('test : ',self.test,'dmg :',atk,'hp :',self.health)

    def gethit(self, ncr1, ncr2, cr1, cr2):
        cr = random.randint(1, 10)
        if 1 <= cr <= 3:
            atk = random.randint(cr1, cr2)
        else:
            atk = random.randint(ncr1, ncr2)
        return atk

    def hp(self, atk):
        self.health -= atk
        return self.health


# MAIN #

# initializing
clock = pygame.time.Clock()
n = Network()
client_number = id
p1startPos = n.getP()
p1 = Player(p1startPos[0], p1startPos[1])
p2startPos = n.getP()
p2 = Player(p2startPos[0], p2startPos[1])
p2x = p2startPos[0]
p2y = p2startPos[1]

client_number = p1startPos[-1]

if client_number == 0:
    p1.assignp1()
    p2.assignp2()
elif client_number == 1:
    p1.assignp2()
    p2.assignp1()

print(id)

if client_number == 0:
    pygame.display.set_caption("[GAME CLIENT - 1]")
elif client_number == 1:
    pygame.display.set_caption("[GAME CLIENT - 2]")

# background
backg1 = pygame.image.load('data/graphics/bg/bg1.png').convert()
backg2 = pygame.image.load('data/graphics/bg/bg2.png').convert()
backg3 = pygame.image.load('data/graphics/bg/bg3.png').convert()
backg4 = pygame.image.load('data/graphics/bg/bg4.png').convert()
backg5 = pygame.image.load('data/graphics/bg/bg5.png').convert()
backg6 = pygame.image.load('data/graphics/bg/bg6.png').convert()
backg_l = [backg1, backg2, backg3, backg4, backg5, backg6]
backg_i = 0
backg_surf = backg_l[backg_i]


def bg_animation():
    global backg_surf, backg_i
    backg_i += 0.12
    if backg_i >= len(backg_l): backg_i = 0
    backg_surf = backg_l[int(backg_i)]
    window.blit(backg_surf, (0, 0))


# loading screen animation
load_rect_3_w = 0
walk_rect_x = 110
load_rect1 = pygame.Rect(107, 550, 906, 26)
load_rect2 = pygame.Rect(110, 553, 900, 20)

walk1 = pygame.image.load('data/graphics/player/walk1.png').convert_alpha()
walk2 = pygame.image.load('data/graphics/player/walk2.png').convert_alpha()
walk3 = pygame.image.load('data/graphics/player/walk3.png').convert_alpha()
walk4 = pygame.image.load('data/graphics/player/walk4.png').convert_alpha()
walk5 = pygame.image.load('data/graphics/player/walk5.png').convert_alpha()
walk6 = pygame.image.load('data/graphics/player/walk6.png').convert_alpha()
walk_l = [walk1, walk2, walk3, walk4, walk5, walk6]
walk_i = 0
walk_surf = walk_l[walk_i]
walk_rect = walk_surf.get_rect()


def load_screen():
    global walk_i, walk_surf, walk_rect
    # load_animation
    pygame.draw.rect(window, (0, 0, 0), load_rect1)
    pygame.draw.rect(window, (255, 255, 255), load_rect2)
    load_rect3 = pygame.Rect(112, 555, int(load_rect_3_w), 16)
    pygame.draw.rect(window, (0, 0, 0), load_rect3)
    # walk_animation
    walk_i += 0.12
    if walk_i >= len(walk_l): walk_i = 0
    walk_surf = walk_l[int(walk_i)]
    walk_rect.midbottom = (int(walk_rect_x), 546)
    window.blit(walk_surf, walk_rect)


# game_start_screen
game_timer = pygame.USEREVENT + 1
black_screen = pygame.image.load('data/graphics/bg/black_screen.png').convert()
black_screen.set_alpha(200)
time_r = 4000
game_start_msg = pixel_font_head2.render(f'{time_r}', None, (255, 255, 255))
game_start_msg_rect = game_start_msg.get_rect()
game_start_msg_rect.center = (560, 350)


def start_screen():
    global game_stage, time_r, game_start_msg, game_start_msg_rect
    window.blit(black_screen, (0, 0))
    time_r = (time_r - 17)
    tr = time_r // 1000
    if tr > 0:
        game_start_msg = pixel_font_head2.render(f'{tr}', None, (255, 255, 255))
    elif tr > -1:
        game_start_msg = pixel_font_head2.render('TATAKAE!', None, (255, 255, 255))
        game_start_msg_rect = game_start_msg.get_rect()
        game_start_msg_rect.center = (560, 350)
    else:
        game_stage = 2
        pygame.time.set_timer(game_timer, 1000)

    window.blit(game_start_msg, game_start_msg_rect)


# p1_health_bar
p1hbar_rect1 = pygame.Rect(104, 40, 406, 22)
p1hbar_rect2 = pygame.Rect(106, 42, 402, 18)
p1hbar_rect3 = pygame.Rect(107, 43, 400, 16)
player_text1 = pixel_font_text.render('|| PLAYER - 1 ||', None, (0, 0, 0))
player_text1_rect = player_text1.get_rect()
player_text1_rect.midbottom = (200, 35)


def p1_hp_bar(x, y):
    global p1hbar_rect1, p1hbar_rect2, p1hbar_rect3
    p1hbar_rect1 = pygame.Rect(x, y, 406, 22)
    pygame.draw.rect(window, (0, 0, 0), p1hbar_rect1)
    p1hbar_rect2 = pygame.Rect(x + 2, y + 2, 402, 18)
    pygame.draw.rect(window, (255, 255, 255), p1hbar_rect2)
    p1hbar_rect3 = pygame.Rect(x + 3, y + 3, p2health, 16)
    if client_number == 0:
        p1hbar_rect3.topright = (x + 403, y + 3)
    pygame.draw.rect(window, (255, 0, 0), p1hbar_rect3)
    window.blit(player_text1, player_text1_rect)


# p2_health_bar
p2hbar_rect1 = pygame.Rect(604, 40, 406, 22)
p2hbar_rect2 = pygame.Rect(606, 42, 402, 18)
p2hbar_rect3 = pygame.Rect(607, 43, 400, 16)
player_text2 = pixel_font_text.render('|| PLAYER - 2 ||', None, (0, 0, 0))
player_text2_rect = player_text2.get_rect()
player_text2_rect.midbottom = (920, 35)


def p2_hp_bar(x, y):
    global p2hbar_rect1, p2hbar_rect2, p2hbar_rect3
    p2hbar_rect1 = pygame.Rect(x, y, 406, 22)
    pygame.draw.rect(window, (0, 0, 0), p2hbar_rect1)
    p2hbar_rect2 = pygame.Rect(x + 2, y + 2, 402, 18)
    pygame.draw.rect(window, (255, 255, 255), p2hbar_rect2)
    p2hbar_rect3 = pygame.Rect(x + 3, y + 3, p1.health, 16)
    if client_number == 0:
        p1hbar_rect3.topright = (x + 403, y + 3)
    pygame.draw.rect(window, (255, 0, 0), p2hbar_rect3)
    window.blit(player_text2, player_text2_rect)


# timer
game_time = 100

timer_box = pygame.Rect(560, 55, 102, 90)
timer_box.center = (556, 55)


def display_time():
    time_text = pixel_font_head.render(f'{game_time}', None, (255, 255, 255))
    timer_rect = time_text.get_rect(center=(556, 57))
    pygame.draw.rect(window, (0, 0, 0), timer_box)
    window.blit(time_text, timer_rect)


# won/lost
you_won = pixel_font_head2.render('YOU WON!', None, (255, 255, 255))
won_rect = you_won.get_rect(center=(560, 290))
you_lost = pixel_font_head2.render('YOU LOST!', None, (255, 255, 255))
lost_rect = you_lost.get_rect(center=(560, 290))

stat = 'playing'


# screen-update
def redrawWin(p1, p2, win):
    p2.draw(win)
    p2.uprect(p2.x, p2.y)
    p1.draw(win)


# player_id
p1id_txt = pixel_font_text2.render('P1', None, (255, 255, 255))
p1id_rect = p1id_txt.get_rect()
p2id_txt = pixel_font_text2.render('P2', None, (255, 255, 255))
p2id_rect = p2id_txt.get_rect()


def p_id(p1, p2):
    if client_number == 0:
        p1id_rect.midbottom = (p1.player_rect.midtop[0], p1.player_rect.midtop[1])
        window.blit(p1id_txt, p1id_rect)
        p2id_rect.midbottom = (p2.player_rect.midtop[0], p2.player_rect.midtop[1])
        window.blit(p2id_txt, p2id_rect)
    elif client_number == 1:
        p1id_rect.midbottom = (p2.player_rect.midtop[0], p2.player_rect.midtop[1])
        window.blit(p1id_txt, p1id_rect)
        p2id_rect.midbottom = (p1.player_rect.midtop[0], p1.player_rect.midtop[1])
        window.blit(p2id_txt, p2id_rect)


# GAME #

game_stage = 0
while game:

    # connecting screen
    if game_stage == 0:

        keys = pygame.key.get_pressed()
        p2Pos = n.send((p1.player_rect.midbottom[0], p1.player_rect.midbottom[1], keys[pygame.K_a], keys[pygame.K_d],
                        keys[pygame.K_w], keys[pygame.K_SPACE], keys[pygame.K_j], keys[pygame.K_k],
                        keys[pygame.K_RSHIFT], p1.punch1, p1.punch2, p1.punch3, p1.kick1, p1.kick2, p1.health,
                        p1.game_active, p1.ready, p1.start))
        p2game_active = p2Pos[15]
        p2ready = p2Pos[16]
        p2start = p2Pos[17]

        if client_number == 0:
            cp = 1
        elif client_number == 1:
            cp = 2
        #########################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
                exit()
        #########################

        window.fill((255, 255, 255))
        player_msg = pixel_font_text.render(f'YOU ARE PLAYER {cp}', None, (0, 0, 0))
        player_msg_rect = player_msg.get_rect(center=(560, 100))
        window.blit(player_msg, player_msg_rect)
        start_msg = pixel_font_head.render('PRESS [ENTER] TO CONNECT', None, (0, 0, 0))
        start_msg_rect = start_msg.get_rect(center=(560, 150))
        waiting_msg = pixel_font_head.render('|| CONNECTED ||  WAITING FOR OTHER PLAYER TO CONNECT...', None, (0, 0, 0))
        waiting_msg_rect = waiting_msg.get_rect(center=(560, 150))
        ready_msg = pixel_font_head.render('|| CONNECTED ||  PRESS [R] WHEN READY', None, (0, 0, 0))
        ready_msg_rect = ready_msg.get_rect(center=(560, 150))
        waiting_r_msg = pixel_font_head.render('|| READY ||  WAITING FOR OTHER PLAYER...', None, (0, 0, 0))
        waiting_r_msg_rect = waiting_r_msg.get_rect(center=(560, 150))
        starting_msg = pixel_font_head.render('||>>>  STARTING THE GAME  <<<||', None, (0, 0, 0))
        starting_msg_rect = starting_msg.get_rect(center=(560, 150))

        if keys[pygame.K_RETURN]:
            p1.ready = True
        elif keys[pygame.K_r]:
            p1.game_active = True

        if game and not (p1.ready):
            window.blit(start_msg, start_msg_rect)
        elif p1.ready and not p2ready:
            window.blit(waiting_msg, waiting_msg_rect)
            load_rect_3_w += 1
            if load_rect_3_w >= 224: load_rect_3_w = 224
            walk_rect_x += 1
            if walk_rect_x >= 334: walk_rect_x = 334
        elif (p1.ready and p2ready) and not (p1.game_active):
            window.blit(ready_msg, ready_msg_rect)
            load_rect_3_w += 1
            if load_rect_3_w >= 448: load_rect_3_w = 448
            walk_rect_x += 1
            if walk_rect_x >= 558: walk_rect_x = 558
        elif p1.game_active and not (p2game_active):
            window.blit(waiting_r_msg, waiting_r_msg_rect)
            load_rect_3_w += 1
            if load_rect_3_w >= 672: load_rect_3_w = 672
            walk_rect_x += 1
            if walk_rect_x >= 782: walk_rect_x = 782
        if p1.game_active and p2game_active:
            window.blit(starting_msg, starting_msg_rect)
            load_rect_3_w += 1
            if load_rect_3_w >= 896:
                load_rect_3_w = 896
                p1.start = True
            walk_rect_x += 1
            if walk_rect_x >= 1006: walk_rect_x = 1006
        load_screen()
        if p1.start and p2start:
            game_stage = 1
        clock.tick(60)

    # starting screen
    elif game_stage == 1:
        keys = pygame.key.get_pressed()
        p2Pos = n.send((p1.player_rect.midbottom[0], p1.player_rect.midbottom[1], keys[pygame.K_a], keys[pygame.K_d],
                        keys[pygame.K_w], keys[pygame.K_SPACE], keys[pygame.K_j], keys[pygame.K_k], keys[pygame.K_l],
                        p1.punch1, p1.punch2, p1.punch3, p1.kick1, p1.kick2, p1.health, p1.game_active, p1.ready,
                        p1.start, p1.runpunch))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
                exit()

        bg_animation()
        p1.start_p1_an()
        p2.start_p2_an()
        p_id(p1, p2)
        p1.draw(window)
        p2.draw(window)
        start_screen()
        clock.tick(60)

    # game screen
    elif game_stage == 2:
        keys = pygame.key.get_pressed()
        p2Pos = n.send((p1.player_rect.midbottom[0], p1.player_rect.midbottom[1], keys[pygame.K_a], keys[pygame.K_d],
                        keys[pygame.K_w], keys[pygame.K_SPACE], keys[pygame.K_j], keys[pygame.K_k],
                        keys[pygame.K_RSHIFT], p1.punch1, p1.punch2, p1.punch3, p1.kick1, p1.kick2, p1.health,
                        p1.game_active, p1.ready, p1.start, p1.runpunch))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2a = p2Pos[2]
        p2d = p2Pos[3]
        p2w = p2Pos[4]
        p2space = p2Pos[5]
        p2j = p2Pos[6]
        p2k = p2Pos[7]
        p2shift = p2Pos[8]
        p2p1 = p2Pos[9]
        p2p2 = p2Pos[10]
        p2p3 = p2Pos[11]
        p2k1 = p2Pos[12]
        p2k2 = p2Pos[13]
        p2health = p2Pos[14]
        p2rp = p2Pos[18]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
                exit()

            if event.type == game_timer:
                game_time -= 1
                if game_time == 0:
                    game_stage = 3

        if p1.health <= 0 or p2health <= 0:
            game_stage = 3

        bg_animation()
        p_id(p1, p2)

        redrawWin(p1, p2, window)
        if client_number == 0:
            p1_hp_bar(104, 40)
            p2_hp_bar(604, 40)
        elif client_number == 1:
            p1_hp_bar(604, 40)
            p2_hp_bar(104, 40)
        Player.update(p1)
        display_time()
        clock.tick(60)

    # after game screen
    elif game_stage == 3:
        keys = pygame.key.get_pressed()
        p2Pos = n.send((p1.player_rect.midbottom[0], p1.player_rect.midbottom[1], keys[pygame.K_a], keys[pygame.K_d],
                        keys[pygame.K_w], keys[pygame.K_SPACE], keys[pygame.K_j], keys[pygame.K_k],
                        keys[pygame.K_RSHIFT], p1.punch1, p1.punch2, p1.punch3, p1.kick1, p1.kick2, p1.health,
                        p1.game_active, p1.ready, p1.start, p1.runpunch, p1.rematch))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2health = p2Pos[14]
        p2rm = p2Pos[-2]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
                exit()

        bg_animation()
        p_id(p1, p2)

        if client_number == 0:
            p1_hp_bar(104, 40)
            p2_hp_bar(604, 40)
        elif client_number == 1:
            p1_hp_bar(604, 40)
            p2_hp_bar(104, 40)

        if p1.health > p2health:
            p1.player_lost(p1.player_rect.midbottom[0], 595)
            if p2.face_r:
                p2.start_p1_an()
            else:
                p2.start_p2_an()
            stat = 'lost'
        else:
            p2.player_lost(p2.x, 595)
            if p1.face_r:
                p1.start_p1_an()
            else:
                p1.start_p2_an()
            stat = 'won'

        p1.draw(window)
        p2.draw(window)
        display_time()
        clock.tick(60)
        window.blit(black_screen, (0, 0))
        if stat == 'lost':
            window.blit(you_lost, lost_rect)
        elif stat == 'won':
            window.blit(you_won, won_rect)

    pygame.display.update()
