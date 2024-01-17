import numpy as np
from update_field import number_of_columns, number_of_rows, update_cells_around_selected_cell, cell_equal_to_zero


def count_bombs_around(visible_field, bomb_field):
    ones_positions = list(zip(np.where(visible_field != 0)[0], np.where(visible_field != 0)[1]))
    for position in ones_positions:
        unclicked_positions_count, bomb_count = 0, 0
        row, column = position[0], position[1]
        unclicked_positions_coordinate = []
        for i in range(row - 1, row + 2):
            for j in range(column - 1, column + 2):
                if i >= 0 and j >= 0 and i < number_of_rows and j < number_of_columns:
                    if i != row or j != column:
                        if visible_field[i, j] == 12:
                            bomb_count += 1
                        elif visible_field[i, j] == 13:
                            unclicked_positions_coordinate.append([i, j])
                            unclicked_positions_count += 1

        if unclicked_positions_count == visible_field[row, column]-bomb_count and visible_field[row, column] != 0:
            for unclicked_position in unclicked_positions_coordinate:
                visible_field[unclicked_position[0], unclicked_position[1]] = 12

        if bomb_count == visible_field[row, column]:
            for unclicked_position in unclicked_positions_coordinate:
                update_cells_around_selected_cell(unclicked_position, bomb_field, visible_field)

'''
        if bomb_count == visible_field[row, column]:
            visible_field[unclicked_positions_coordinate[0], unclicked_positions_coordinate[1]] = 12
'''
def mark_flag(visible_field):
    ones_positions = list(zip(np.where(visible_field == 1)[0], np.where(visible_field == 1)[1]))
    for position in ones_positions:
        unclicked_positions_count, bomb_count = 0, 0
        row, column = position[0], position[1]
        for i in range(row - 1, row + 2):
            for j in range(column - 1, column + 2):
                if i >= 0 and j >= 0 and i < number_of_rows and j < number_of_columns:
                    if i != row or j != column:
                        if visible_field[i, j] == 12:
                            bomb_count += 1
                        elif visible_field[i, j] == 13:
                            unclicked_positions_coordinate = [i, j]
                            unclicked_positions_count += 1

def mark_as_flag(position, list_, bomb_count, visible_field):
    row, column = position[0], position[1]
    if list_ != 0 and bomb_count == 1:
        for i in range(row - 1, row + 2):
            for j in range(column - 1, column + 2):
                if i >= 0 and j >= 0 and i < number_of_rows and j < number_of_columns and visible_field[i, j] == 13:
                    if i != row or j != column:
                        visible_field[i, j] = 12


def one_bomb(visible_field, bomb_field):
    """
    Identifies positions with a value of 1 in the visible_field array and checks the surrounding squares.
    If there is only one unclicked square and no bombs, it marks that square as a bomb.
    
    Returns:
    visible_field (numpy.ndarray): Updated visible_field array.
    """
    count_bombs_around(visible_field, bomb_field)

    '''
    for index, position in enumerate(ones_positions):
        mark_as_flag(position, position_bomb_count[index], bomb_count, row, column)
    '''
    return visible_field