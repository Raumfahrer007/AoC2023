def part_one(input):
    sum = 0
    for line in input:
        history = generate_history(line)

        history[-1].append(0)

        for i in reversed(range(len(history) - 1)):
            difference = history[i][-1] + history[i + 1][-1]
            history[i].append(difference)

        sum += history[0][-1]

    print(f"Sum PartOne: {sum}")
        

def part_two(input):
    sum = 0
    for line in input:
        history = generate_history(line)

        history[-1].insert(0, 0)

        for i in reversed(range(len(history) - 1)):
            difference = history[i][0] - history[i + 1][0]
            history[i].insert(0, difference)

        sum += history[0][0]

    print(f"Sum PartTwo: {sum}")


def generate_history(line):
    history = [[int(value) for value in line.replace("\n", "").split(" ")]]
    all_zero = False
    i = 0

    while not all_zero:
        all_zero = True
        current_history_line = history[i]
        new_history_line = []

        for j in range(len(current_history_line) - 1):
            difference = current_history_line[j+1] - current_history_line[j]
            new_history_line.append(difference)

            if not difference == 0:
                all_zero = False

        history.append(new_history_line)
        i += 1

    return history


test_1 = [
    "0 3 6 9 12 15\n",
    "1 3 6 10 15 21\n",
    "10 13 16 21 30 45\n"
]


if __name__ == "__main__":
    data = open("day09Input.txt", "r")
    input = data.readlines()
    data.close()

    part_one(input)
    part_two(input)