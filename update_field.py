from create_field import start_field, number_of_rows, number_of_columns


def cell_equal_to_zero(selected_cell_list, bomb_field, visible_field, starting_position):
    if visible_field[starting_position[0], starting_position[1]] == 0:
        cells_checked = selected_cell_list.copy()
        while len(selected_cell_list) != 0:
            for cell in selected_cell_list:
                selected_cell_row, selected_cell_column = cell[0], cell[1]
                selected_cell_list.remove((selected_cell_row, selected_cell_column))
                if bomb_field[selected_cell_row, selected_cell_column] == 0:
                    for i in range(selected_cell_row - 1, selected_cell_row + 2):
                        for j in range(selected_cell_column - 1, selected_cell_column + 2):
                            if i >= 0 and j >= 0 and i < number_of_rows and j < number_of_columns:
                                visible_field[i, j] = bomb_field[i, j]
                                if (i, j) not in cells_checked:
                                    cells_checked.append((i, j))
                                    selected_cell_list.append((i, j))


def update_cells_around_selected_cell(selected_cell, bomb_field, visible_field):
    selected_cell_row, selected_cell_column = selected_cell[0], selected_cell[1]
    if bomb_field[selected_cell_row, selected_cell_column] != 9:
        new_cells_coordinates = []
        visible_field[selected_cell_row, selected_cell_column] = bomb_field[selected_cell_row, selected_cell_column]
        for i in range(selected_cell_row - 1, selected_cell_row + 2):
            for j in range(selected_cell_column - 1, selected_cell_column + 2):
                if i >= 0 and j >= 0 and i < number_of_rows and j < number_of_columns:
                    if bomb_field[i, j] == 0:
                        visible_field[i, j] = bomb_field[i, j]
                        new_cells_coordinates.append((i, j))

    cell_equal_to_zero(new_cells_coordinates, bomb_field, visible_field, selected_cell)
    return visible_field


def update_field():
    visible_field, bomb_field, starting_position = start_field()
    cell_equal_to_zero([starting_position], bomb_field, visible_field, starting_position)
    visible_field = update_cells_around_selected_cell(starting_position, bomb_field, visible_field)
    return visible_field, bomb_field, starting_position
