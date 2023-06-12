import pygame
import os
import random

from levelSeven import *

pygame.init() #initialize pygame

screen = pygame.display.set_mode((800,600)) #sets dimensions of screen
pygame.display.set_caption("The Battle Of The Marauders") #sets window title

def battleSystemFirePage(givenName, startingPoints, newPower, newHealth):

    setLvl7Character(givenName)

    clock = pygame.time.Clock()
    fps = 60

    #initialization

    current_character = 1
    total_characters = 2
    action_cooldown = 10
    action_wait_time = 90
    attack = False
    clicked = False
    end_game_signal = 0 

    #define font
    font = pygame.font.Font('assets/8-bit-hud.ttf', 15)


    white = (255, 255, 255)
    green = (0,255,0)
    red = (255, 0, 0)
    dark_green = (1,50,32)
    dark_red = (139, 0, 0)
    blue = 	(0,0,255)


    # drawing text
    def draw_text(text, font, text_color, x, y):
        img = font.render(text, True, text_color)
        screen.blit(img, (x, y))


    #load background
    background_img = pygame.image.load("assets/scene/scene_11_modified.png").convert_alpha()

    panel_img = pygame.image.load("assets/panel/panel_1.png").convert_alpha()

    if givenName == "Knight":
        pointer_img = pygame.image.load("assets/pointer/sword_pointer.png").convert_alpha()
    elif givenName == "Archer":
        pointer_img = pygame.image.load("assets/pointer/arrow_pointer.png").convert_alpha()
    else:
        pointer_img = pygame.image.load("assets/pointer/wand_pointer.png").convert_alpha()

    victory_img = pygame.image.load("assets/panel/panel_victory.png").convert_alpha()

    game_over_img = pygame.image.load("assets/panel/panel_defeat.png").convert_alpha()

    #draw background function
    def draw_background():
        screen.blit(background_img, (0, 0))

    newName = "Pyro"

    #draw background function
    def draw_panel():
        #draw panel
        screen.blit(panel_img, (0, 0))
        #show stats
        draw_text(f'{hero.name.capitalize()} HP: {hero.health}', font, white, 100, 470)
        for count, i in enumerate(enemy_list):
            #show name and health
                draw_text(f'{newName.capitalize()} HP: {i.health}', font, white, 430, (470) + count * 55)
        draw_text(f'Score: {hero.points} points', font, white, 100, 525)

        
    #Character class
    class Character():
        def __init__(self, x, y, name, max_health, power, scale, points):
            self.name = name
            self.max_health = max_health
            self.health = max_health


            self.power = power
            self.alive = True
            self.animation_list = []
            self.frame_index = 0
            self.action = 0 #idle, 1 is attack, 2 is hurt, 3 is death
            self.points = points


            #load images
            self.update_time = pygame.time.get_ticks()


            #folder path for idle
            folder_path_idle = f"assets/{self.name}/idle"
            folder_path_attack = f"assets/{self.name}/attack"
            folder_path_hurt = f"assets/{self.name}/hurt"
            folder_path_death = f"assets/{self.name}/death"


            # Initialize a counter for the number of files
            file_count_idle = 0
            file_count_attack = 0
            file_count_hurt = 0
            file_count_death = 0


            # Loop through all files in the idle folder
            for filename in os.listdir(folder_path_idle):
                if os.path.isfile(os.path.join(folder_path_idle, filename)):
                    file_count_idle += 1


            # Loop through all files in the attack folder
            for filename in os.listdir(folder_path_attack):
                if os.path.isfile(os.path.join(folder_path_attack, filename)):
                    file_count_attack += 1

            # Loop through all files in the hurt folder
            for filename in os.listdir(folder_path_hurt):
                if os.path.isfile(os.path.join(folder_path_hurt, filename)):
                    file_count_hurt += 1

            # Loop through all files in the death folder
            for filename in os.listdir(folder_path_death):
                if os.path.isfile(os.path.join(folder_path_death, filename)):
                    file_count_death += 1

            #load all the animation frames during idle      
            temp_list = []
            for i in range(file_count_idle):
                img = pygame.image.load(f'assets/{self.name}/idle/{self.name}_idle_{i}.png')
                img = pygame.transform.scale(img, (img.get_width()*scale, img.get_height()*scale))
                temp_list.append(img)
            self.animation_list.append(temp_list)


            #load all the animation frames during attack      
            temp_list = []
            for i in range(file_count_attack):
                img = pygame.image.load(f'assets/{self.name}/attack/{self.name}_attack_{i}.png')
                img = pygame.transform.scale(img, (img.get_width()*scale, img.get_height()*scale))
                temp_list.append(img)
            self.animation_list.append(temp_list)

            #load all the animation frames during hurt      
            temp_list = []
            for i in range(file_count_hurt):
                img = pygame.image.load(f'assets/{self.name}/hurt/{self.name}_hurt_{i}.png')
                img = pygame.transform.scale(img, (img.get_width()*scale, img.get_height()*scale))
                temp_list.append(img)
            self.animation_list.append(temp_list)

            #load all the animation frames during death      
            temp_list = []
            for i in range(file_count_death):
                img = pygame.image.load(f'assets/{self.name}/death/{self.name}_death_{i}.png')
                img = pygame.transform.scale(img, (img.get_width()*scale, img.get_height()*scale))
                temp_list.append(img)
            self.animation_list.append(temp_list)

            self.image = self.animation_list[self.action][self.frame_index]
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)


        def idle(self):
            self.action = 0
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

        
        def attack(self, opponent):
            #deal damage to enemy
            randomNumber = random.randint(-2,2)
            damage = self.power + randomNumber
            if self.name == givenName:
                self.points += damage
            opponent.health += -damage            
            opponent.hurt()
            if opponent.health < 1:
                opponent.health = 0
                opponent.alive = False
                opponent.death()
            damage_value = DamageValues(opponent.rect.centerx, opponent.rect.y, str(damage), blue)
            damage_values_group.add(damage_value)
            self.action = 1
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

        def pointsChange(self, amount, count):
            if count == 0:
                self.points += amount

        def hurt(self):
            self.action = 2
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

        def death(self):
            self.action = 3
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

        def draw(self):
            screen.blit(self.image, self.rect)


        def update(self):
            animation_cooldown=100
            #animation handling and update the image
            self.image = self.animation_list[self.action][self.frame_index]
            # get time when last updated, and difference is greater than 100 ms, time to update to next stage
            if pygame.time.get_ticks() - self.update_time > animation_cooldown:
                self.update_time = pygame.time.get_ticks()
                self.frame_index +=1

            # when the loop gets to the length of the list, set it back to zero to avoid error
            if self.frame_index >= len(self.animation_list[self.action]):
                if self.action == 3:
                    self.frame_index = len(self.animation_list[self.action]) - 1
                else:
                    self.idle()

    class HealthBar():
        def __init__(self, x, y, health, max_health):
            self.x=x
            self.y=y
            self.health = health
            self.max_health = max_health


        def draw(self, health, color, secondary_color):
            self.health = health
            ratio_of_health = self.health / self.max_health
            pygame.draw.rect(screen, secondary_color, (self.x, self.y, 200, 20))
            pygame.draw.rect(screen, color, (self.x, self.y, 200*ratio_of_health, 20))

    class Invisible():
        def __init__(self, x, y, scale):
            self.x=x
            self.y=y
            img = pygame.image.load("assets/skeleton/invisible/skeleton_invisible_0.png")
            revised_img = pygame.transform.scale(img, (img.get_width()*scale, img.get_height()*scale))
            self.image = revised_img
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            
        def draw(self):
            screen.blit(self.image, self.rect)

    class DamageValues(pygame.sprite.Sprite):
        def __init__ (self, x, y, damageAmount, color):
            pygame.sprite.Sprite.__init__(self)
            self.image = font.render(damageAmount, True, color)
            self.rect = self.image.get_rect()
            self.rect.center = (x,y)
            self.counter = 0
        
        def update(self):
            self.rect.y -= 1
            self.counter += 1
            if self.counter > 35:
                self.kill()

        
    counter = 0
    damage_values_group = pygame.sprite.Group()


    if givenName == "Knight":
        hero = Character(200, 306, givenName, newHealth, newPower, 0.25, startingPoints)
    elif givenName == "Archer":
        hero = Character(200, 306, givenName, newHealth, newPower, 0.25, startingPoints)
    elif givenName == "Wizard":
        hero = Character(200, 295, givenName, newHealth, newPower, 0.13, startingPoints)

    enemy1 = Character(560, 303, 'fire', 33, 15, 0.2, 0)

    invisible_enemy_1 = Invisible(560, 303, 0.2)

    invisible_enemy_list = []
    invisible_enemy_list.append(invisible_enemy_1)


    enemy_list = []
    enemy_list.append(enemy1)


    hero_health_bar = HealthBar(100, 500, hero.health, hero.max_health)
    enemy1_health_bar = HealthBar(430, 500, enemy1.health, enemy1.max_health)

    number = 0 
    running = True #variable for game loop


    # Game Loop


    while running:

        global nextLevel
        global gameQuit
        gameQuit = False
        nextLevel = False

        clock.tick(fps)

        draw_background()
        draw_panel()

        hero_health_bar.draw(hero.health, green, dark_green)
        enemy1_health_bar.draw(enemy1.health, red, dark_red)
        
        #draw characters
        hero.update()
        hero.draw()

        #draw enemeies
        for enemy in enemy_list:
            enemy.update()
            enemy.draw()
    
        for invisible in invisible_enemy_list:
            invisible.draw()


        damage_values_group.update()
        damage_values_group.draw(screen)

        #controls and action vars
        attack = False
        opponent = None

        if end_game_signal == 0:

            pygame.mouse.set_visible(True)
            mouse_pos = pygame.mouse.get_pos()
            for count, invisible in enumerate(invisible_enemy_list):
                if invisible.rect.collidepoint(mouse_pos):
                    pygame.mouse.set_visible(False)
                    screen.blit(pointer_img, mouse_pos)
                    if clicked == True:
                        opponent = enemy_list[count]
                        if opponent.alive == True:
                            attack = True

            #player action
            if hero.alive == True:
                if current_character == 1: # wizards turn
                    action_cooldown += 1
                    if action_cooldown >= action_wait_time:
                        #look for player action
                        #attack
                        if attack == True and opponent != None:
                            hero.attack(opponent)
                            current_character +=1
                            action_cooldown = 0
            else:
                end_game_signal = -1

            for count, enemy in enumerate(enemy_list):
                if current_character == 2 + count:
                    if enemy.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait_time:
                            enemy.attack(hero)
                            current_character += 1
                            action_cooldown = 0
                    else:
                        current_character += 1


            if current_character > total_characters:
                current_character = 1

        alive_enemies = 0
        for enemy in enemy_list:
            if enemy.alive == True:
                alive_enemies += 1
        if alive_enemies == 0:
            end_game_signal = 1

        if end_game_signal != 0:
            if end_game_signal == 1:
                screen.blit(victory_img, (75,15))
                hero.pointsChange(hero.health, number)
                number += 1
                
                getUpgrade(hero.points,hero.power + 1,hero.max_health)
                
                
                nextLevel = True
                #main(window)

                
            if end_game_signal == -1:
                screen.blit(game_over_img, (75,15))
                gameQuit = True

        
        
        
        for event in pygame.event.get():
            # lets you leave the while loop when you click exit
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
            else:
                clicked = False
    
        pygame.display.update()

        if(nextLevel):
            counter += 1
            if counter > 200:
                main(window)

        if (gameQuit):
            counter += 1
            if counter > 200:
                running=False

    pygame.quit()
