import random


def dead_state(width: int, height: int):
    return [[0 for _ in range(width)] for _ in range(height)]


def random_state(width: int, height: int):
    state = dead_state(width, height)
    for i in range(height):
        for j in range(width):
            state[i][j] = 0 if random.random() > 0.5 else 1
    return state


def render(board_state: []):
    print('-' * (len(board_state[0]) + 2))
    for i in range(len(board_state)):
        print('|', end='')
        for j in range(len(board_state[i])):
            if board_state[i][j] == 1:
                print('O', end='')
            if board_state[i][j] == 0:
                print('.', end='')
        print('|', end='')
        print()
    print('-' * (len(board_state[0]) + 2))


def next_board_state(initial_state: []):
    width, height = len(initial_state[0]), len(initial_state)
    next_state = dead_state(width, height)

    for x in range(0, height):
        for y in range(0, width):
            next_state = next_cell_value((x, y), initial_state)
    return next_state


def next_cell_value(coords, initial_state):
    width, height = len(initial_state[0]), len(initial_state)
    x, y = coords[0], coords[1]
    live_neighbor_count = 0

    neighbours = [
                (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                (x - 1, y),                     (x + 1, y),
                (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
            ]


            # for nx, ny in neighbours:
            #     if 0 <= nx < len(initial_state) and 0 <= ny < len(initial_state[0]):






