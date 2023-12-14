def part_one(input):
    """
    Expand Universe
    """
    expanded_universe = []
    for line in input:
        expanded_universe.append([*line.replace("\n", "")])
        if not "#" in line:
            expanded_universe.append([*line.replace("\n", "")])

    j = 0
    while j < len(expanded_universe[0]):
        column = []
        for line in expanded_universe:
            column.append(line[j])
        
        if not "#" in column:
            j += 1
            for i in range(len(expanded_universe)):
                expanded_universe[i].insert(j, ".")

        j += 1

    galaxies = get_galaxies(expanded_universe)

    sum = get_galaxy_distances_sum(galaxies)

    print(f"Sum PartOne: {sum}")



def part_two(input):
    """
    Get empty lines and columns
    """
    empty_rows = []
    empty_columns = []

    for i, line in enumerate(input):
        input[i] = input[i].replace("\n", "")
        if not "#" in line:
            empty_rows.append(i)

    for j in range(len(input[0])):
        empty = True
        for line in input:
            if line[j] == "#":
                empty = False
                break

        if empty:
            empty_columns.append(j)

    galaxies = get_galaxies(input)
    
    """
    Expand Universe by manipulating Galaxy coordinates
    """
    for i, galaxy in enumerate(galaxies):
        new_x = galaxy[0]
        new_y = galaxy[1]
        for row in empty_rows:
            if galaxy[0] > row: #Expansion before Galaxy
                new_x += 999999
            else:
                break

        for column in empty_columns:
            if galaxy[1] > column:
                new_y += 999999
            else:
                break

        galaxies[i] = [new_x, new_y]

    sum = get_galaxy_distances_sum(galaxies)

    print(f"Sum PartTwo: {sum}")


def get_galaxies(universe):
    """
    Get coordinates of Galaxies
    """
    galaxies = []

    for i, line in enumerate(universe):
        for j, column in enumerate(line):
            if column == "#":
                galaxies.append([i, j])

    return galaxies


def get_galaxy_distances_sum(galaxies):
    """
    Calculate Distances between Galaxies and return sum of distances
    """
    sum = 0

    for i, galaxy in enumerate(galaxies):
        for j in range(i+1, len(galaxies)):
            distance = abs(galaxies[j][0] - galaxy[0]) + abs(galaxies[j][1] - galaxy[1])
            sum += distance

    return sum



test_1 = [
    "...#......\n",
    ".......#..\n",
    "#.........\n",
    "..........\n",
    "......#...\n",
    ".#........\n",
    ".........#\n",
    "..........\n",
    ".......#..\n",
    "#...#.....\n"
]


if __name__ == "__main__":
    data = open("day11Input.txt", "r")
    input = data.readlines()
    data.close()

    part_one(input)
    part_two(input)