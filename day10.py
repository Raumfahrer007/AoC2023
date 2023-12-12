operations = {
    "U": [-1, 0],
    "R": [0, 1],
    "D": [1, 0],
    "L": [0, -1]
}


x_y_move_tile_map = {   # maps an x- and y-movement between two tiles to a tube part
    -1: {
        -1: "7",
        0: "|",
        1: "F"
        
    },
    0: "-",
    1: {
        -1: "J",
        0: "|",
        1: "L"
    },
    2: "|"
}


direction_tile_map = {  # maps a movement direction to the corresponding parts
    "U": ["|", "7", "F"],
    "R": ["-", "J", "7"],
    "D": ["|", "J", "L"],
    "L": ["-", "L", "F"]
}


tile_direction_map = {  # maps a tube part and an inside direction to the outside direciton
    "|": {
        "U": "U",
        "D": "D"
    },
    "-": {
        "L": "L",
        "R": "R"
    },
    "L": {
        "D": "R",
        "L": "U"
    },
    "J": {
        "D": "L",
        "R": "U"
    },
    "7": {
        "U": "L",
        "R": "D"
    },
    "F": {
        "U": "R",
        "L": "D"
    }
}


def part_one(input):
    maze, starting_point = get_maze_and_start(input)
    loop_way = get_loop(maze, starting_point)

    print(f"Longest Way in Loop {len(loop_way) // 2}")


def part_two(input):
    maze, starting_point = get_maze_and_start(input)
    loop_way = get_loop(maze, starting_point)

    """
    replaces tube-parts that are not part of the loop with ground tiles
    """
    for i, line in enumerate(maze):
        for j, tile in enumerate(line):
            if not tile == ".":
                coordinate = [i, j]
                if not coordinate in loop_way:
                    maze[i][j] = "."

    inside_counter = 0
    maze = replace_start_tile(maze, loop_way)

    """
    Looks for every ground tile if it's inside.
    Looks at every tile in the column from top to the ground tile.
    If a tile is '-': inside changes
    If a tile is 'F' or '7', it checks if the next corner part goes in the opposite direction
        If so, inside changes
    """
    for i, line in enumerate(maze):
        for j in range(len(line)):
            if maze[i][j] == ".":
                inside = False

                k = 0
                while k <= i:
                    if maze[k][j] == "-":
                        inside = not inside
                        k += 1

                    elif maze[k][j] == "F":
                        k += 1
                        while maze[k][j] == "|":
                            k += 1
                        if maze[k][j] == "J":
                            inside = not inside

                    elif maze[k][j] == "7":
                        k += 1
                        while maze[k][j] == "|":
                            k += 1
                        if maze[k][j] == "L":
                            inside = not inside

                    else:
                        k += 1

                if inside:
                    maze[i][j] = "I"
                    inside_counter += 1

                else:
                    maze[i][j] = "0"

    print(f"Tiles inside: {inside_counter}")


def get_maze_and_start(input):
    """
    returns maze and coordinates of 'S'
    """
    maze = []
    starting_point = 0

    for i, line in enumerate(input):
        for j, char in enumerate(line):
            if char == "S":
                starting_point = [i, j]
        maze.append([*line.replace("\n", "")])

    return maze, starting_point


def get_loop(maze, starting_point):
    """
    Returns the coordinates of the loop, starting at 'S'.
    Starts by going in every of the four directions from 'S' and looks if the next tile fits.
    If so, it starts check_way()
    """
    potential_loops = []

    i = 0
    loop_way = None
    for operation in operations.items():
        if starting_point[0] + operation[1][0] in range(len(maze)) or starting_point[1] + operation[1][1] in range(len(maze[0])):
            next_position = [starting_point[0] + operation[1][0], starting_point[1] + operation[1][1]]
            next_tile = maze[next_position[0]][next_position[1]]

            if next_tile in direction_tile_map[operation[0]]:
                potential_loops.append([starting_point])
                loop_way = check_way(current_position=next_position, last_move=operation[0], move_list=potential_loops[i], maze=maze)
                if loop_way:
                    break
                i += 1

    return loop_way


def check_way(current_position, last_move, move_list, maze):
    """
    Goes throug loops until hitting a dead-end, earth-tile or S
    """
    loop = False

    while True:
        current_tile = maze[current_position[0]][current_position[1]]
        next_move = tile_direction_map[current_tile][last_move]
        next_operation = operations[next_move]

        if current_position[0] + next_operation[0] in range(len(maze)) or current_position[1] + next_operation[1] in range(len(maze[0])):
            next_position = [current_position[0] + next_operation[0], current_position[1] + next_operation[1]]
            next_tile = maze[next_position[0]][next_position[1]]

            if next_tile in direction_tile_map[next_move]:
                move_list.append(current_position)
                current_position = next_position
                last_move = next_move

            elif next_tile == "S":
                move_list.append(current_position)
                loop = True
                break

            else:
                break

        else:
            break

    if loop:
        return move_list
    
    else:
        return None
    

def replace_start_tile(maze, move_list):
    """
    replaces 'S' with its correspongin tube part
    """
    x_move = move_list[1][0] - move_list[-1][0]
    y_move = move_list[1][1] - move_list[-1][1]

    if x_move == 0 or x_move == 2:
        start_tile = x_y_move_tile_map[x_move]
    else:
        start_tile = x_y_move_tile_map[x_move][y_move]

    maze[move_list[0][0]][move_list[0][1]] = start_tile

    return maze


test_1 = [
    "...........\n",
    ".S-------7.\n",
    ".|F-----7|.\n",
    ".||.....||.\n",
    ".||.....||.\n",
    ".|L-7.F-J|.\n",
    ".|..|.|..|.\n",
    ".L--J.L--J.\n",
    "...........\n"
]

test_2 = [
    "..........\n",
    ".S------7.\n",
    ".|F----7|.\n",
    ".||....||.\n",
    ".||....||.\n",
    ".|L-7F-J|.\n",
    ".|..||..|.\n",
    ".L--JL--J.\n",
    "..........\n"
]

test_3 = [
    "FF7FSF7F7F7F7F7F---7\n",
    "L|LJ||||||||||||F--J\n",
    "FL-7LJLJ||||||LJL-77\n",
    "F--JF--7||LJLJ7F7FJ-\n",
    "L---JF-JLJ.||-FJLJJ7\n",
    "|F|F-JF---7F7-L7L|7|\n",
    "|FFJF7L7F-JF7|JL---7\n",
    "7-L-JL7||F7|L7F-7F7|\n",
    "L.L7LFJ|||||FJL7||LJ\n",
    "L7JLJL-JLJLJL--JLJ.L\n"
]


if __name__ == "__main__":
    data = open("day10Input.txt", "r")
    input = data.readlines()
    data.close()

    part_one(input)
    part_two(input)