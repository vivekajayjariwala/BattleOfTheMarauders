from levelOne import *
import pygame
from os import listdir
from os.path import isfile, join
from upgrade import *

pygame.init()

def upgradeWindow(window):

    window = pygame.display.set_mode((800, 600))
  
    clock = pygame.time.Clock()
    background, bg_image = get_background("shop_background.png")

    block_size = 96

    
    shop_image = pygame.image.load("Assets/inventory/blank_shop.png")
    shop_rect = pygame.Rect(0, 0, shop_image.get_width(), shop_image.get_height())
   
    player = Player(100, 100, 50, 50)
    sword = Sword(2900, HEIGHT - block_size - 255, 26, 25)
    sword.on()
    objects = [
        Block(block_size * 0, HEIGHT - block_size * 1, block_size),
        Block(block_size * 1, HEIGHT - block_size * 1, block_size), #Player Lands
        Block(block_size * 2, HEIGHT - block_size * 1, block_size),
        Block(block_size * 3, HEIGHT - block_size * 1, block_size),
        Block(block_size * 4, HEIGHT - block_size * 1, block_size),
        Block(block_size * 5, HEIGHT - block_size * 1, block_size),
        Block(block_size * 6, HEIGHT - block_size * 1, block_size),
        Block(block_size * 7, HEIGHT - block_size * 1, block_size),
        Block(block_size * 8, HEIGHT - block_size * 1, block_size),
        
        sword
    ]
    offset_x = 0
    scroll_area_width = 0

    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_h:
                    print("IDK")
                    # SS.toggleInventory()
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()

        player.loop(FPS)
        sword.loop()
        handle_move(player, objects)
        

        
        bg_image.blit(shop_image, (600,340))
        end_point = 600
        if player.rect.right >= end_point:
            upgradePage()
        
        draw(window, background, bg_image, player, objects, offset_x)

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel

        

    pygame.quit()
    quit()


if __name__ == "__main__":
    upgradeWindow(window)