import pygame, sys
from characterPage import secondPage
from pygame import mixer
pygame.init() #initializes pygame

mixer.init()
mixer.music.load("soundtrack.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()

screen = pygame.display.set_mode((800,600)) # sets dimensions of screen

pygame.display.set_caption("The Battle Of The Marauders") #sets window title

bg_img = pygame.image.load("assets/title_screen_grey.jpg")
bg_rect = bg_img.get_rect()  # get coordinates

screen.blit(bg_img, bg_rect)  # places image on screen

#load button images
play_button_img = pygame.image.load("assets/play_button.png").convert_alpha()
quit_button_img = pygame.image.load("assets/quit_button.png").convert_alpha()

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self):
        action = False
        #get mouse position
        mouse_pos = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        # draw button on the screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action 

#create button instances
quit_button = Button(200,400, quit_button_img, 0.5)
play_button = Button(470, 400, play_button_img, 0.5)

running = True

# Game Loop

while running:
    if play_button.draw():
        print("Play")
        secondPage()
    if quit_button.draw():
        print("Quit")
        running = False
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()