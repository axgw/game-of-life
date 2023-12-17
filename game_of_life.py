import random
import time
import sys
import os

DEAD = 0
ALIVE = 1


def dead_state(width, height):
    return [[DEAD for _ in range(height)] for _ in range(width)]


def random_state(width, height):
    state = dead_state(width, height)
    for x in range(0, len(state)):
        for y in range(0, len(state[0])):
            random_number = random.random()
            if random_number > 0.85:
                cell_state = ALIVE
            else:
                cell_state = DEAD
            state[x][y] = cell_state
    return state


def next_cell_value(cell_position, state):
    width, height = len(state), len(state[0])
    x, y = cell_position[0], cell_position[1]
    live_neighbours = 0

    neighbours = [
                (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                (x - 1, y),                     (x + 1, y),
                (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
            ]

    for nx, ny in neighbours:
        if 0 <= nx < width and 0 <= ny < height:
            if nx == x and ny == y:
                continue
            if state[nx][ny] == ALIVE:
                live_neighbours += 1

    if state[x][y] == ALIVE:
        if live_neighbours <= 1:
            return DEAD
        elif live_neighbours <= 3:
            return ALIVE
        else:
            return DEAD
    else:
        if live_neighbours == 3:
            return ALIVE
        else:
            return DEAD


def next_board_state(state):
    width, height = len(state), len(state[0])
    next_state = dead_state(width, height)
    for y in range(0, height):
        for x in range(0, width):
            next_state[x][y] = next_cell_value((x, y), state)
    return next_state


def render(state):
    width, height = len(state), len(state[0])
    display_as = {DEAD: ' ', ALIVE: 'o'}
    lines = []
    for x in range(0, width):
        line = ''
        for y in range(0, height):
            line += display_as[state[x][y]]
        lines.append(line)
    print("\n".join(lines))


def life_loop(start):
    next_state = start
    while True:
        try:
            render(next_state)
            next_state = next_board_state(next_state)
            time.sleep(0.3)
            os.system('cls')
        except KeyboardInterrupt:
            print("Conway's Game of Life")
            sys.exit()


if __name__ == "__main__":
    init_state = random_state(75, 30)
    life_loop(init_state)
