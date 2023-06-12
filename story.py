import pygame
import time
import pygame.gfxdraw
from levelOne import *

pygame.init()

# Initialize the screen with width = 800 and height = 600
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))


def story():

    # screen.fill(background_color)
    bg_img = pygame.image.load("assets/story_screen.jpg")
    bg_rect = bg_img.get_rect()  # get coordinates
    screen.blit(bg_img, bg_rect)  # places image on screen

    # Create a font object
    font = pygame.font.Font('assets/8-bit-hud.ttf', 20)

    # set the text for "Next" and "Quit"
    play_button_img = pygame.image.load(
        "assets/begin_your_journey_button.png").convert_alpha()

    class Button():
            def __init__(self, x, y, image, scale):
                width = image.get_width()
                height = image.get_height()
                self.image = pygame.transform.scale(
                    image, (int(width*scale), int(height*scale)))
                self.rect = self.image.get_rect()
                self.rect.topleft = (x, y)
                self.clicked = False

            def draw(self):
                action = False
                # get mouse position
                mouse_pos = pygame.mouse.get_pos()
                # check mouseover and clicked conditions
                if self.rect.collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                        self.clicked = True
                        action = True

                    if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False

                # draw button on the screen
                screen.blit(self.image, (self.rect.x, self.rect.y))
                return action

    # Calculate the center of the screen
    center_x = screen_width // 2
    center_y = screen_height // 2

    # call flip to refresh the screen
    pygame.display.flip()
    play_button = Button(430, 510, play_button_img, 0.3)
    # The Game Loop
    running = True
    while running:

        if play_button.draw():
            print("Play")
            main(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Render
        # --> flip to refresh
        pygame.display.flip()

        # slow down the loop a little bit to be able to see the effects
        time.sleep(0.05)
    pygame.quit()
