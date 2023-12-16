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
                print('#', end='')
            if board_state[i][j] == 0:
                print(' ', end='')
        print('|', end='')
        print()
    print('-' * (len(board_state[0]) + 2))


render(random_state(30,20))




