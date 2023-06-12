import pygame
import time
import pygame.gfxdraw
from levelOne import *
from controls import controls

pygame.init()

# Initialize the screen with width = 800 and height = 600
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))


def secondPage(): 
   
   # Setting colors
   archer_color = (59, 150, 44, 255)  # green
   warrior_color = (105, 105, 105, 255)  # dark grey
   wizard_color = (0, 76, 255, 255)  # blue
   
   background_color = (211, 211, 211)  # light grey

   #screen.fill(background_color)
   screen.fill(background_color)

   # Load the images
   scale_x = 200
   scale_y = 200

   archer_img = pygame.image.load('assets/Character_Selection_Archer.png')
   archer_img = pygame.transform.scale(archer_img, (scale_x, scale_y))

   warrior_img = pygame.image.load('assets/Character_Selection_Warrior.png')
   warrior_img = pygame.transform.scale(warrior_img, (scale_x, scale_y))

   wizard_img = pygame.image.load('assets/Character_Selection_Wizard.png')
   wizard_img = pygame.transform.scale(wizard_img, (scale_x, scale_y))

   # Create a font object
   font = pygame.font.Font('assets/8-bit-hud.ttf', 20)

   # Render the text as an image surface
   text_surface = font.render("Choose Your Character", True, (0, 0, 0))

   # set the text for "Next" and "Quit"
   next_text = font.render("Next", True, (0, 0, 0))
   quit_text = font.render("Quit", True, (0, 0, 0))

   next_rect = next_text.get_rect()
   quit_rect = quit_text.get_rect()
   next_rect.center = (screen_width//2 + 100, screen_height-50)
   quit_rect.center = (screen_width//2 - 100, screen_height-50)


   # Calculate the center of the screen
   center_x = screen_width // 2
   center_y = screen_height // 2

   # Calculate the top-left position of the image
   archer_width, archer_height = archer_img.get_size()

   archer_x = center_x - archer_width // 2
   archer_y = center_y - archer_height // 2

   warrior_x = archer_x - archer_width // 2 - 100
   warrior_y = center_y - archer_height // 2

   wizard_x = archer_x + archer_width // 2 + 100
   wizard_y = center_y - archer_height // 2

   # Set the size of the images
   img_width, img_height = archer_img.get_size()
   img_width //= 2  # make the images half the size

   # Calculate the top-left position of the image
   image_width, image_height = archer_img.get_size()
   image_x = center_x - image_width // 2
   image_y = center_y - image_height // 2

   # Draw the images onto the screen
   screen.blit(text_surface, (center_x - text_surface.get_width() // 2, 100))
   screen.blit(archer_img, (image_x, image_y))
   screen.blit(warrior_img, (warrior_x, warrior_y))


   # call flip to refresh the screen
   pygame.display.flip()

   # Render the text as an image surface
   def showCharacter(character):
      if character == "Wizard":
         text = font.render(character, True, wizard_color)
      if character == "Archer":
         text = font.render(character, True, archer_color)
      if character == "Knight":
         text = font.render(character, True, warrior_color)
      return text


   def printCharacter(character):
      # Define the area where the text will be displayed
      text_rect = pygame.Rect(0, 0, 600, 135)
      text_rect.centerx = screen.get_rect().centerx
      text_rect.bottom = screen.get_rect().bottom

      # Draw a filled rectangle over the area where the text was previously displayed
      pygame.draw.rect(screen, background_color, text_rect)

      if character == "Wizard":
         new_color = wizard_color
      elif character == "Archer":
         new_color = archer_color
      else:
         new_color = warrior_color

      # Render and display the new text
      text1 = font.render(character, True, new_color)
      text2 = font.render(" has been selected!", True, (0, 0, 0))
      text_width = text1.get_width() + text2.get_width()
      text_rect.center = screen.get_rect().center
      text_rect.bottom = screen.get_rect().bottom
      text_rect.left = text_rect.left + (text_rect.width - text_width) / 2
      screen.blit(text1, (text_rect.left, text_rect.top))
      screen.blit(text2, (text_rect.left + text1.get_width(), text_rect.top))
      screen.blit(next_text, next_rect)
      screen.blit(quit_text, quit_rect)
      pygame.display.update()
   # The Game Loop
   running = True
   while running:

      # Event loop
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
               running = False
         elif event.type == pygame.MOUSEBUTTONDOWN:
               mouse_x, mouse_y = pygame.mouse.get_pos()
               if image_x <= mouse_x <= image_x + image_width and image_y <= mouse_y <= image_y + image_height:
                  setLvl1Character("Archer")
                  printCharacter("Archer")
                  
               elif warrior_x <= mouse_x <= warrior_x + image_width and warrior_y <= mouse_y <= warrior_y + image_height:
                  setLvl1Character("Knight")
                  printCharacter("Knight")
                  
               elif wizard_x <= mouse_x <= wizard_x + image_width and wizard_y <= mouse_y <= wizard_y + image_height:
                  setLvl1Character("Wizard")
                  printCharacter("Wizard")
                  

               mouse_pos = pygame.mouse.get_pos()
               if next_rect.collidepoint(mouse_pos):
                  print("Next")
                  controls()

                  # perform next action here
               elif quit_rect.collidepoint(mouse_pos):
                  print("Quit")
                  running = False

      # Game Logic
      mouse_x, mouse_y = pygame.mouse.get_pos()

      show_archer_text = False
      if image_x <= mouse_x <= image_x + image_width and image_y <= mouse_y <= image_y + image_height:
         # if the mouse is touching the archer image
         show_archer_text = True
         screen.blit(showCharacter("Archer"), (image_x + image_width // 2 - showCharacter("Archer").get_width() // 2, image_y + image_height))
      else:
         # clear the area where the text was drawn
         screen.fill(background_color, (image_x, image_y + image_height, showCharacter("Archer").get_width() + 150, showCharacter("Archer").get_height()))
         screen.blit(archer_img, (image_x, image_y))

      show_warrior_text = False
      if warrior_x <= mouse_x <= warrior_x + image_width and warrior_y <= mouse_y <= warrior_y + image_height:
         # if the mouse is touching the warrior image
         show_warrior_text = True
         screen.blit(showCharacter("Knight"), (warrior_x + image_width // 2 - showCharacter("Knight").get_width() // 2, warrior_y + image_height))
      else:
         # clear the area where the text was drawn
         screen.fill(background_color, (warrior_x, warrior_y + image_height, showCharacter("Knight").get_width() + 50, showCharacter("Knight").get_height()))
         screen.blit(warrior_img, (warrior_x, warrior_y))

      show_wizard_text = False
      if wizard_x <= mouse_x <= wizard_x + image_width and wizard_y <= mouse_y <= wizard_y + image_height:
         # if the mouse is touching the wizard image
         show_wizard_text = True
         screen.blit(showCharacter("Wizard"), (wizard_x + image_width // 2 - showCharacter("Wizard").get_width() // 2, wizard_y + image_height))
      else:
         # clear the area where the text was drawn
         screen.fill(background_color, (wizard_x, wizard_y + image_height, showCharacter("Wizard").get_width() + 50, showCharacter("Wizard").get_height()))
         screen.blit(wizard_img, (wizard_x, wizard_y))

      if not show_archer_text and not show_warrior_text and not show_wizard_text:
         screen.blit(text_surface, (center_x - text_surface.get_width() // 2, 100))

      # Render
      # --> flip to refresh
      pygame.display.flip()

      # slow down the loop a little bit to be able to see the effects
      time.sleep(0.05)
   pygame.quit()