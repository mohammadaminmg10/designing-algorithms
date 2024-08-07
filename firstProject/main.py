from game import *

playground = [
    ['2', 'X', '!', '5', '0'],
    ['1', '9', '!', 'X', '3'],
    ['1', '3', '1', '6', '2'],
    ['2', 'X', '5', '1', 'X'],
    ['8', '4', '!', '!', '1'],
]

player_path = [
    (0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3), (4, 4)
]

playground = initialize_matrix(playground)
print(calculate_gold(playground, player_path))
print(dynamic_collect_gold(playground))
print(greedy_collect_gold(playground))
