import numpy

def part_one(input):
    network = get_network(input)
    instructions = input[0][0:-1]

    current_place = "AAA"
    step_counter = 0
    i = 0

    while not current_place == "ZZZ":
        if i == len(instructions):
            i = 0

        if instructions[i] == "L":
            current_place = network[current_place][0]
        else:
            current_place = network[current_place][1]

        step_counter += 1
        i += 1

    print(f"StepCount Part One: {step_counter}")


def part_two(input):
    network = get_network(input)
    instructions = input[0][0:-1]
    current_positions = []
    steps = []

    for node in network.keys():
        if node[-1] == "A":
            current_positions.append(node)
            steps.append(0)

    i = 0
    for j in range(len(current_positions)):
        print(f"RUN {j}")
        while not current_positions[j][-1] == "Z":
            if i == len(instructions):
                i = 0
    
            if instructions[i] == "L":
                current_positions[j] = network[current_positions[j]][0]
            else:
                current_positions[j] = network[current_positions[j]][1]
            
            steps[j] += 1
            i += 1

    lcm = numpy.lcm.reduce(steps, dtype=object)
    print(f"StepCount Part Two: {lcm}")


def get_network(input):
    network = {}
    for i, line in enumerate(input):
        if i < 1:
            continue

        key = line[:3]
        next_steps = [
            line[7:10],
            line[12:15]
        ]
        
        network[key] = next_steps

    return network


test_1 = [
    "LR\n",

    "11A = (11B, XXX)",
    "11B = (XXX, 11Z)",
    "11Z = (11B, XXX)",
    "22A = (22B, XXX)",
    "22B = (22C, 22C)",
    "22C = (22Z, 22Z)",
    "22Z = (22B, 22B)",
    "XXX = (XXX, XXX)"
]


if __name__ == "__main__":
    data = open("day08Input.txt", "r")
    input = data.readlines()
    data.close()

    part_one(input)
    part_two(input)