import numpy as np
import random


size = (30, 30)
number_of_rows, number_of_columns = size
number_of_bombs = int(number_of_rows*number_of_columns//5)

def create_field():
    """
    Creates a field for the MineSweeper game.

    Returns:
    numpy.ndarray: The starting field with all cells initialized to 0.
    """
    starting_field = np.array([[0]*number_of_columns]*number_of_rows)
    return starting_field

def create_bomb_field(number_of_bombs, starting_field):
    """
    Create a bomb field with the specified number of bombs.

    Args:
        number_of_bombs (int): The number of bombs to be placed in the field.

    Returns:
        tuple: A tuple containing the bomb field and the positions of the bombs.
    """
    bomb_field = starting_field.copy()
    for i in range(number_of_bombs):
        bomb_row, bomb_column = random.randint(0, number_of_rows - 1), random.randint(0, number_of_columns - 1)
        bomb_field[bomb_row, bomb_column] = 9

    bombs_position_row, bombs_position_column = np.where(bomb_field == 9)
    bomb_position = []
    for i in range(len(bombs_position_row)):
        bomb_position.append((bombs_position_row[i], bombs_position_column[i]))
        
    return bomb_field, bomb_position

def calculate_number_of_bombs_around(bomb_position, bomb_field):
    for location in bomb_position:
        row, column = location[0], location[1]
        for i in range(row - 1, row + 2):
            for j in range(column - 1, column + 2):
                if i >= 0 and j >= 0 and i < number_of_rows and j < number_of_columns:      
                    if bomb_field[i, j] != 9:
                        bomb_field[i, j] += 1
        
    return bomb_field

def create_visibile_field(bomb_field):
    visible_field = np.array([[13]*number_of_columns]*number_of_rows)
    starting_positions = list(zip(np.where(bomb_field == 0)[0], np.where(bomb_field == 0)[1]))
    starting_position = random.choice(starting_positions)
    visible_field[starting_position[0], starting_position[1]] = bomb_field[starting_position[0], starting_position[1]]

    return visible_field, starting_position

def start_field():
    starting_field = create_field()
    bomb_field, bomb_position = create_bomb_field(number_of_bombs, starting_field)
    bomb_field = calculate_number_of_bombs_around(bomb_position, bomb_field)
    visible_field, starting_position = create_visibile_field(bomb_field)
    visible_field[starting_position[0], starting_position[1]] = bomb_field[starting_position[0], starting_position[1]]
    return visible_field, bomb_field, starting_position