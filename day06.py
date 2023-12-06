def part_one(input):
    races = []
    for i, line in enumerate(input):
        line = line[line.find(":"):].replace(":", "")

        while "  " in line:
            line = line.replace("  ", " ")

        values = line[1:].split(" ")
        for j, value in enumerate(values):
            if i == 0:
                races.append([value])
            else:
                races[j].append(value)

    sum = get_winning_count(races)

    print(f"Sum PartOne: {sum}")


def part_two(input):
    race = []
    for line in input:
        line = line[line.find(":"):].replace(":", "").replace(" ", "")
        race.append(int(line))

    winnings = get_winning_count([race])

    print(f"Winnings PartTwo: {winnings}")


def get_winning_count(races):
    sum = 1
    
    for race in races:
        win_counter = 0
        race_time = int(race[0])
        record_distance = int(race[1])

        for push_time in range(race_time + 1):
            travel_time = race_time - push_time
            distance = push_time * travel_time

            if distance > record_distance:
                win_counter += 1

        sum *= win_counter

    return sum



test_1 = [
    "Time:      7  15   30",
    "Distance:  9  40  200"
]


if __name__ == "__main__":
    data = open("day06Input.txt", "r")
    input = data.readlines()
    data.close()

    part_one(input)
    part_two(input)