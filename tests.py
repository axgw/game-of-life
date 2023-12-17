import unittest
from game_of_life import next_board_state


class LifeTestCases(unittest.TestCase):
    # TEST 1: dead cells with no live neighbors should stay dead
    def test_stay_dead(self):
        init_state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        expected_next_state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        result = next_board_state(init_state)
        self.assertTrue(result == expected_next_state)

    # TEST 2: dead cells with exactly 3 neighbors should come alive
    def test_reproduction(self):
        init_state = [
            [0, 0, 1],
            [0, 1, 1],
            [0, 0, 0]
        ]
        expected_next_state = [
            [0, 1, 1],
            [0, 1, 1],
            [0, 0, 0]
        ]
        result = next_board_state(init_state)
        self.assertTrue(result == expected_next_state)

    # TEST 3: live cells die when they have more than 3 live neighbors
    def test_death_by_overpopulation(self):
        init_state = [
            [1, 1, 0],
            [0, 1, 1],
            [0, 1, 0]
        ]
        expected_next_state = [
            [1, 1, 0],
            [0, 0, 1],
            [0, 1, 0]
        ]
        result = next_board_state(init_state)
        self.assertTrue(result == expected_next_state)

    # TEST 4:
    def test_death_by_underpopulation(self):
        init_state = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        expected_next_state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        result = next_board_state(init_state)
        self.assertTrue(result == expected_next_state)

    # TEST 5: any live cell with 2 or 3 live neighbors stays alive
    def test_survival(self):
        init_state = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        expected_next_state = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        result = next_board_state(init_state)
        self.assertTrue(result == expected_next_state)


if __name__ == '__main__':
    unittest.main()
