import pygame
import time
import random

pygame.init()

W, H = 550, 550
win = pygame.display.set_mode((W, H))

pygame.display.set_caption("Time for revenge")

bg_menu = pygame.image.load('Texturs\Menu\Menu.png').convert()
bg_death = pygame.image.load('Texturs\Background\BG_Death.png').convert()
bg_victory = pygame.image.load('Texturs\Background\BG_Victory.png').convert()
bg_level_1 = pygame.image.load('Texturs\Background\BG_level_1.png').convert()
bg_level_2 = pygame.image.load('Texturs\Background\BG_level_2.png').convert()
bg_level_3 = pygame.image.load('Texturs\Background\BG_level_3.png').convert()
bg_level_4 = pygame.image.load('Texturs\Background\BG_level_4.png').convert()

m_tank_1 = [pygame.image.load('Texturs\Tanks\Main_tank\MT_1\MT_1_DOWN.png'), pygame.image.load('Texturs\Tanks\Main_tank\MT_1\MT_1_UP.png'), pygame.image.load('Texturs\Tanks\Main_tank\MT_1\MT_1_LEFT.png'), pygame.image.load('Texturs\Tanks\Main_tank\MT_1\MT_1_RIGHT.png')]
m_tank_2 = [pygame.image.load('Texturs\Tanks\Main_tank\MT_2\MT_2_DOWN.png'), pygame.image.load('Texturs\Tanks\Main_tank\MT_2\MT_2_UP.png'), pygame.image.load('Texturs\Tanks\Main_tank\MT_2\MT_2_LEFT.png'), pygame.image.load('Texturs\Tanks\Main_tank\MT_2\MT_2_RIGHT.png')]
m_tank_3 = [pygame.image.load('Texturs\Tanks\Main_tank\MT_3\MT_3_DOWN.png'), pygame.image.load('Texturs\Tanks\Main_tank\MT_3\MT_3_UP.png'), pygame.image.load('Texturs\Tanks\Main_tank\MT_3\MT_3_LEFT.png'), pygame.image.load('Texturs\Tanks\Main_tank\MT_3\MT_3_RIGHT.png')]
m_tanks_list = [m_tank_1, m_tank_2, m_tank_3]

e_tank_1 = [pygame.image.load('Texturs\Tanks\Enemy_tank\ET_1\ET_1_DOWN.png'), pygame.image.load('Texturs\Tanks\Enemy_tank\ET_1\ET_1_UP.png'), pygame.image.load('Texturs\Tanks\Enemy_tank\ET_1\ET_1_LEFT.png'), pygame.image.load('Texturs\Tanks\Enemy_tank\ET_1\ET_1_RIGHT.png')]
e_tank_2 = [pygame.image.load('Texturs\Tanks\Enemy_tank\ET_2\ET_2_DOWN.png'), pygame.image.load('Texturs\Tanks\Enemy_tank\ET_2\ET_2_UP.png'), pygame.image.load('Texturs\Tanks\Enemy_tank\ET_2\ET_2_LEFT.png'), pygame.image.load('Texturs\Tanks\Enemy_tank\ET_2\ET_2_RIGHT.png')]
e_tank_3 = [pygame.image.load('Texturs\Tanks\Enemy_tank\ET_3\ET_3_DOWN.png'), pygame.image.load('Texturs\Tanks\Enemy_tank\ET_3\ET_3_UP.png'), pygame.image.load('Texturs\Tanks\Enemy_tank\ET_3\ET_3_LEFT.png'), pygame.image.load('Texturs\Tanks\Enemy_tank\ET_3\ET_3_RIGHT.png')]
e_tanks_list = [e_tank_1, e_tank_2, e_tank_3]

bullet = pygame.image.load('Texturs\Add_animations\Bullet.png')

clock = pygame.time.Clock()

def main_game():
    run = True
    level_is = 1
    select_tank = 0
    x = W - 300
    y = H - 75
    speed = 3
    e_speed = 2
    bullets = []
    e_bullets = []
    e_tanks = []
    last_move = 'up'
    cd_time = 18
    e_cd_time = 34
    e_tanks_place = 0
    place_time = 20
    e_tanks_place_time = place_time
    max_e_tanks = 3
    tanks_left = 3
    e_tanks_left = 20
    
    
    class bull():
        def __init__(self, x, y, facingx, facingy):
            self.x = x
            self.y = y
            self.facingx = facingx
            self.facingy = facingy
            self.velx = 8 * facingx
            self.vely = 8 * facingy
        def draw(self):
            win.blit(pygame.image.load('Texturs\Add_animations\Bullet.png'), (self.x, self.y))
    
    class e_tank_c():
        def __init__(self, x, y, last_move, e_select_tank, rot_timer, e_cd_time):
            self.x = x
            self.y = y
            self.last_move = last_move
            self.e_select_tank = e_select_tank
            self.rot_timer = rot_timer
            self.e_cd_time = e_cd_time
        def draw(self):
            if self.last_move == 'down':
                win.blit(self.e_select_tank[0], (self.x, self.y))
                if self.y < H - 50 and (self.x + 50 < x or self.x > x + 50 or self.y + 50 < y or self.y > y + 50):
                    self.y += e_speed
            elif self.last_move == 'up':
                win.blit(self.e_select_tank[1], (self.x, self.y))
                if self.y > 0 and (self.x + 50 < x or self.x > x + 50 or self.y + 50 < y or self.y > y + 50):
                    self.y -= e_speed
            elif self.last_move == 'left':
                win.blit(self.e_select_tank[2], (self.x, self.y))
                if self.x > 0 and (self.x + 50 < x or self.x > x + 50 or self.y + 50 < y or self.y > y + 50):
                    self.x -= e_speed
            elif self.last_move == 'right':
                win.blit(self.e_select_tank[3], (self.x, self.y))
                if self.x < W - 50 and (self.x + 50 < x or self.x > x + 50 or self.y + 50 < y or self.y > y + 50):
                    self.x += e_speed
            
            if self.last_move == 'down':
                facingx = 0
                facingy = 1
            elif self.last_move == 'up':
                facingx = 0
                facingy = -1
            elif self.last_move == 'left':
                facingx = -1
                facingy = 0
            elif self.last_move == 'right':
                facingx = 1
                facingy = 0
            
            if len(e_bullets) < 10 and self.e_cd_time <= 0:
                e_bullets.append(bull(round(self.x + 40 // 2), round(self.y + 40 // 2), facingx, facingy))
                self.e_cd_time = e_cd_time
            
            self.e_cd_time -= 1
    
    def message(mess, x, y, font_color, font_size, font_type):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(mess, True, font_color)
        win.blit(text, (x, y))
    
    def draw_window():
        if level_is == 1:
            win.blit(bg_level_1, (0, 0))
        elif level_is == 2:
            win.blit(bg_level_2, (0, 0))
        elif level_is == 3:
            win.blit(bg_level_3, (0, 0))
        else:
            win.blit(bg_level_4, (0, 0))
        
        if last_move == 'down':
            win.blit(select_tank[0], (x, y))
        elif last_move == 'up':
            win.blit(select_tank[1], (x, y))
        elif last_move == 'left':
            win.blit(select_tank[2], (x, y))
        elif last_move == 'right':
            win.blit(select_tank[3], (x, y))
        
        for bullet in bullets:
            bullet.draw()
        
        for e_bullet in e_bullets:
            e_bullet.draw()
        
        for e_tank in e_tanks:
            if e_tank.rot_timer == 0:
                e_tank.rot_timer = random.randrange(20, 50)
                e_tank.last_move = random.choice(['down', 'up', 'left', 'right'])
            e_tank.rot_timer -= 1
            e_tank.draw()
        
        message(f'enemy tanks left: {e_tanks_left}', 15, 15, (200, 200, 200), 30, 'Config\TextL\Rodch.ttf')
        message(f'your tanks left: {tanks_left}', W - 240, H - 40, (200, 200, 200), 30, 'Config\TextL\Rodch.ttf')
        
        pygame.display.update()
    
    def main_menu():
        menu_time = True
        click = False
        sel_tank = 0
        
        while menu_time:
            clock.tick(60)
            
            global select_tank
            
            win.blit(bg_menu, (0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.K_SPACE:
                    menu_time = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                        
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            button_1_KV2 = pygame.Rect(14, 20, 170, 236)
            button_2_M6 = pygame.Rect(192, 20, 170, 236)
            button_3_T34 = pygame.Rect(370, 20, 170, 236)
            button_4_GO = pygame.Rect(150, 324, 255, 159)
            
            if button_1_KV2.collidepoint((mouse_x, mouse_y)):
                if click:
                    sel_tank = 0
            if button_2_M6.collidepoint((mouse_x, mouse_y)):
                if click:
                    sel_tank = 1
            if button_3_T34.collidepoint((mouse_x, mouse_y)):
                if click:
                    sel_tank = 2
            if button_4_GO.collidepoint((mouse_x, mouse_y)):
                if click:
                    return sel_tank
            
            click = False
            pygame.display.update()
    
    def death():
        win.blit(bg_death, (0, 0))
        message('You Dead', W // 3, H // 3, (170, 43, 43), 50, 'Config\TextL\Rodch.ttf')
        message('Press "Enter" to start taking revenge again',  W // 4 - 35, H // 4 + 110, (170, 43, 43), 20, 'Config\TextL\Rodch.ttf')
        check = True
        
        while check:
            clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            key = pygame.key.get_pressed()
            if key[pygame.K_RETURN]:
                main_game()
            
            pygame.display.update()
    
    def victory():
        win.blit(bg_victory, (0, 0))
        message('Victory!', W // 3, H // 3, (40, 200, 120), 50, 'Config\TextL\Rodch.ttf')
        message('Press "Enter" to start taking revenge again',  W // 4 - 35, H // 4 + 110, (40, 200, 120), 20, 'Config\TextL\Rodch.ttf')
        message('Or you can click the "x" on the top of',  W // 4 - 15, H // 4 + 140, (40, 200, 120), 20, 'Config\TextL\Rodch.ttf')
        message('the window to end this HELL!',  W // 4 + 20, H // 4 + 170, (40, 200, 120), 20, 'Config\TextL\Rodch.ttf')
        check = True
        
        while check:
            clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            key = pygame.key.get_pressed()
            if key[pygame.K_RETURN]:
                main_game()
            
            pygame.display.update()
    
    select_tank = m_tanks_list[main_menu()]
    
    while run:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        for bullet in bullets:
            if bullet.x < 550 and bullet.x > 0:
                bullet.x += bullet.velx
            else:
                bullets.pop(bullets.index(bullet))
            
            if bullet.y < 550 and bullet.y > 0:
                
                bullet.y += bullet.vely
            else:
                bullets.pop(bullets.index(bullet))
        
        for e_bullet in e_bullets:
            if e_bullet.x < 550 and e_bullet.x > 0:
                e_bullet.x += e_bullet.velx
            else:
                e_bullets.pop(e_bullets.index(e_bullet))
            
            if e_bullet.y < 550 and e_bullet.y > 0:
                
                e_bullet.y += e_bullet.vely
            else:
                e_bullets.pop(e_bullets.index(e_bullet))
        
        if cd_time != 0:
            cd_time -= 1
            
        e_tanks_place_time = e_tanks_place_time - 1
        
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN] and y < H - 50:
            y += speed
            last_move = 'down'
        elif key[pygame.K_UP] and y > 0:
            y -= speed
            last_move = 'up'
        elif key[pygame.K_LEFT] and x > 0:
            x -= speed
            last_move = 'left'
        elif key[pygame.K_RIGHT] and x < W - 50:
            x += speed
            last_move = 'right'
        if key[pygame.K_SPACE]:
            if last_move == 'down':
                facingx = 0
                facingy = 1
            elif last_move == 'up':
                facingx = 0
                facingy = -1
            elif last_move == 'left':
                facingx = -1
                facingy = 0
            elif last_move == 'right':
                facingx = 1
                facingy = 0
            if len(bullets) < 10 and cd_time == 0:
                bullets.append(bull(round(x + 40 // 2), round(y + 40 // 2), facingx, facingy))
                cd_time = 18
        
        for bullet in bullets:
            for e_tank in e_tanks:
                if bullet.x + 10 > e_tank.x and bullet.x < e_tank.x + 50 and bullet.y + 10 > e_tank.y and bullet.y < e_tank.y + 50:
                    bullets.pop(bullets.index(bullet))
                    e_tanks.pop(e_tanks.index(e_tank))
                    if e_tanks_left != 0:
                        e_tanks_place_time = place_time
                    else:
                        victory()
        for e_bullet in e_bullets:
            if e_bullet.x + 10 > x and e_bullet.x < x + 50 and e_bullet.y + 10 > y and e_bullet.y < y + 50:
                e_bullets.pop(e_bullets.index(e_bullet))
                if tanks_left != 0:
                    x = W - 300
                    y = H - 75
                    tanks_left -= 1
                else:
                    death()
        
        if len(e_tanks) < max_e_tanks and e_tanks_place_time <= 0 and e_tanks_left >= 0:
            if e_tanks_place == 0:
                e_tanks_place_time = place_time
                e_tanks_left -= 1
                e_tanks.append(e_tank_c(round(125), round(25), 'down', e_tanks_list[random.randrange(0, 3)], random.randrange(20, 50), 32))
            elif e_tanks_place == 1:
                e_tanks_place_time = place_time
                e_tanks_left -= 1
                e_tanks.append(e_tank_c(round(W - 175), round(25), 'down', e_tanks_list[random.randrange(0, 3)], random.randrange(20, 50), 32))
            elif e_tanks_place == 2:
                e_tanks_place_time = place_time
                e_tanks_left -= 1
                e_tanks.append(e_tank_c(round(W - 300), round(25), 'down', e_tanks_list[random.randrange(0, 3)], random.randrange(20, 50), 32))
        if e_tanks_place < max_e_tanks:
            e_tanks_place += 1
        else:
            e_tanks_place = 0
        
        draw_window()

main_game()

pygame.quit()