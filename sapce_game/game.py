import pygame
import math

pygame.init()

def main():
    WIDTH, HEIGHT = 1100, 600
    win = pygame.display.set_mode((WIDTH, HEIGHT))

    class Player():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.vel = 5
            self.bullet_vel = 6
            self.player = pygame.image.load("space_ship.png")
            self.player_img = pygame.transform.rotate(self.player, 90)
            self.bullet = pygame.image.load("bullet.png")
            self.bullet_img = pygame.transform.rotate(self.bullet, -90)
            self.bullet_img = pygame.transform.scale(self.bullet, (20, 20))
            self.bullet_x = self.x
            self.bullet_y = self.y
            self.score_count = 0
            self.max_bullets = []

            
        def draw_players(self):
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render(f"score: {int(self.score_count)}", True, (255, 255, 255))
            win.blit(text, (1000, 20))
            win.blit(self.player_img, (self.x, self.y)) # 370, 500
        
        def handle_bullets(self, other_x, other_y):
            for i in self.max_bullets:
                win.blit(self.bullet_img, (i.x, i.y))
                i.x -= self.bullet_vel

                distance = math.sqrt((other_x-i.x)**2+(other_y-i.y)**2)
                if distance < 30:
                    self.max_bullets.remove(i)
                    self.score_count += 1

                if i.x <= 0:
                    self.max_bullets.remove(i)

        def is_win(self):
            if self.score_count == 10:
                font = pygame.font.Font('freesansbold.ttf', 40)
                text = "Right player win!"
                text_d = font.render(text, True, (0,255,0))
                win.blit(text_d, (370, 300))

                pygame.display.update()
                pygame.time.delay(3000)
                main()


        def move(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_UP]:
                self.y -= self.vel

            if key[pygame.K_DOWN]:
                self.y += self.vel

            if key[pygame.K_LEFT]:
                self.x -= self.vel

            if key[pygame.K_RIGHT]:
                self.x += self.vel
            
            
            if self.x <= 530:
                self.x = 530

            if self.x >= 1070:
                self.x = 1070
            
            if self.y <= 0:
                self.y = 0

            if self.y >= 570:
                self.y = 570
            

            self.draw_players()
        
        def hit_other_player(self, other_x, other_y):
            distance = math.sqrt((other_x-self.bullet_x)**2+(other_y-self.bullet_y)**2)
            if distance < 20:
                self.bullet_y = self.y
                self.bullet_x = self.x
                self.bullet_state = "ready"
                self.score_count += 1

    class Player2:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.vel = 5
            self.bullet_vel = 6
            self.player = pygame.image.load("space_ship.png")
            self.player_img = pygame.transform.rotate(self.player, -90)
            self.bullet = pygame.image.load("bullet.png")
            self.bullet_img = pygame.transform.scale(self.bullet, (20, 20))
            self.bullet_x = self.x
            self.bullet_y = self.y
            self.score_count = 0
            self.max_bullets = []
            
        def draw_players(self):    
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render(f"score: {int(self.score_count)}", True, (255, 255, 255))
            win.blit(text, (20, 20))
            win.blit(self.player_img, (self.x, self.y)) # 370, 500

        def handle_bullets(self, other_x, other_y):
            for i in self.max_bullets:
                win.blit(self.bullet_img, (i.x, i.y))
                i.x += self.bullet_vel

                distance = math.sqrt((other_x-i.x)**2+(other_y-i.y)**2)
                if distance < 30:
                    self.max_bullets.remove(i)
                    self.score_count += 1


                if i.x >= 1100:
                    self.max_bullets.remove(i)

        def is_win(self):
            if self.score_count == 10:
                font = pygame.font.Font('freesansbold.ttf', 40)
                text = "Left player win!"
                text_d = font.render(text, True, (0,255,0))
                win.blit(text_d, (370, 300))

                pygame.display.update()
                pygame.time.delay(3000)
                main()

        def move(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                self.y -= self.vel

            if key[pygame.K_s]:
                self.y += self.vel

            if key[pygame.K_a]:
                self.x -= self.vel

            if key[pygame.K_d]:
                self.x += self.vel
            
            if self.x <= 0:
                self.x = 0

            if self.x >= 500:
                self.x = 500
            
            if self.y <= 0: 
                self.y = 0

            if self.y >= 570:
                self.y = 570

            self.draw_players()
        


    run = True
    p = Player(1030, 300)
    p2 = Player2(50, 300)
    bg = pygame.image.load("background.png")

    while run:
        win.blit(bg, (0, 0))
        p.draw_players()
        p2.draw_players()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and len(p2.max_bullets) < 3:
                    bullet = win.blit(p2.bullet_img, (p2.x, p2.y))
                    p2.max_bullets.append(bullet)
                
                if event.key == pygame.K_RCTRL and len(p.max_bullets) < 3:
                    bullet = win.blit(p.bullet_img, (p.x, p.y))
                    p.max_bullets.append(bullet)

        p.move()
        p2.move()
        p.handle_bullets(p2.x, p2.y)
        p2.handle_bullets(p.x, p.y)
        pygame.draw.line(win, (0, 0, 0), (530, 0), (530, 600), 10)
        p.is_win()
        p2.is_win()
        pygame.display.update()

main()