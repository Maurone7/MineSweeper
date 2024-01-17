from create_field import number_of_rows, number_of_columns
from update_field import update_cells_around_selected_cell, update_field
import pygame
import numpy as np
from Minesweeper_solver import one_bomb

visible_field, bomb_field, starting_position = update_field()

# Initialize pygame
pygame.init()

# Set up the window
window_size = (window_width, window_height) = (800, 800)
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mine Sweeper")

# Add your game rendering code here
rect_size = (rect_width, rect_height) = (window_width, window_height)
playing_area_size = (playing_area_width, playing_area_height) = (rect_width - 100, rect_height - 100)
rect_x = (window_width - playing_area_width) // 2
rect_y = (window_height - playing_area_height) // 2
little_rect_size = (little_rect_width, little_rect_height) = (playing_area_width // number_of_columns, playing_area_height // number_of_rows)
little_border_thickness = 1
# Render the game
window.fill((100, 100, 100))  # Fill the window with a slightly lighter grey color

restart_button_size = (80, 30)
restart_button = pygame.Rect((window_width/2 -restart_button_size[0], 10, 80, 30))

pygame.draw.rect(window, (150, 150, 150), restart_button)

# Render the text
font = pygame.font.Font(None, 25)
text = font.render("Restart", True, (0, 0, 0))

# Calculate the position to center the text
text_rect = text.get_rect(center=restart_button.center)

# Blit the text onto the window surface
window.blit(text, text_rect)

solve_button = pygame.Rect((window_width/2 + restart_button_size[0]), 10, 80, 30)
pygame.draw.rect(window, (150, 150, 150), solve_button)
text = font.render("Solve", True, (0, 0, 0))
text_rect = text.get_rect(center=solve_button.center)
window.blit(text, text_rect)

def image_load():
    for i in range(number_of_rows):
        for j in range(number_of_columns):
            window.blit(images_dict[visible_field[j, i]], (rect_x + little_rect_width * i, rect_y + little_rect_height * j))

# Load the number images
number_0 = pygame.image.load('Sprites/empty.png')
for i in range(1, 9):
    exec(f'number_{i} = pygame.image.load("Sprites/grid{i}.png")')

# Load the mine image
mine = pygame.image.load('Sprites/mine.png')
clicked_mine = pygame.image.load('Sprites/mineClicked.png')
mine_false = pygame.image.load('Sprites/mineFalse.png')
flag = pygame.image.load('Sprites/flag.png')
not_clicked = pygame.image.load('Sprites/Grid.png')

images_dict = {0: number_0, 1: number_1, 2: number_2, 3: number_3, 4: number_4, 5: number_5, 6: number_6, 7: number_7, 8: number_8, 9: mine, 10: clicked_mine, 11: mine_false, 12: flag, 13: not_clicked}
images_dict = {key: pygame.transform.scale(value, little_rect_size) for key, value in images_dict.items()}

def image_load_fun():
    for i in range(number_of_rows):
        for j in range(number_of_columns):
            image_load(images_dict[visible_field[j, i]])

flag_positions = []
# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            mouse_x, mouse_y = mouse_x - 50, mouse_y - 50
            row_clicked = mouse_y // (playing_area_height // number_of_rows)
            column_clicked = mouse_x // (playing_area_width // number_of_columns)
            if event.button == 1:  # Left mouse button
                if restart_button.collidepoint(event.pos):
                    visible_field, bomb_field, starting_position = update_field()

                elif solve_button.collidepoint(event.pos):
                    visible_field = one_bomb(visible_field, bomb_field)

                elif mouse_x >= playing_area_width or mouse_y >= playing_area_height or mouse_x < 0 or mouse_y < 0:
                    continue

                elif visible_field[row_clicked, column_clicked] == 12:
                    continue

                elif bomb_field[row_clicked, column_clicked] == 9 and visible_field[row_clicked, column_clicked] == 13:
                    visible_field = bomb_field
                    visible_field[row_clicked, column_clicked] = 10
                    for position in flag_positions:
                        if bomb_field[position[0], position[1]] != 9:
                            visible_field[position[0], position[1]] = 11

                elif visible_field[row_clicked, column_clicked] == 13:
                    visible_field[row_clicked, column_clicked] = 12
                    update_cells_around_selected_cell((row_clicked, column_clicked), bomb_field, visible_field)

            elif event.button == 3:  # Right mouse button
                if visible_field[row_clicked, column_clicked] == 9:
                    continue
                elif visible_field[row_clicked, column_clicked] != 12:
                    visible_field[row_clicked, column_clicked] = 12
                    flag_positions.append((row_clicked, column_clicked))
                elif visible_field[row_clicked, column_clicked] == 12:
                    visible_field[row_clicked, column_clicked] = 13
                    if (row_clicked, column_clicked) in flag_positions:
                        flag_positions.remove((row_clicked, column_clicked))

    image_load()
    pygame.display.flip()
    finished = True
    if list(zip(np.where(visible_field == 12)[0], np.where(visible_field == 12)[1])) == list(zip(np.where(bomb_field == 9)[0], np.where(bomb_field == 9)[1])):
        finished == True
        solve_button = pygame.Rect(((window_width - 2 * restart_button_size[0]) / 2 + 2 * restart_button_size[0]),
                                   10, 80, 30)
        pygame.draw.rect(window, (150, 150, 150), solve_button)
        text = font.render("Mauro", True, (0, 0, 0))
        text_rect = text.get_rect(center=solve_button.center)
        window.blit(text, text_rect)
        pygame.display.flip()

# Clean up pygame
pygame.quit()
