def part_one(input):
    rules = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    sum = 0

    for line in input:
        draws = line[line.find(":"):].replace(":", "").replace(" ", "").replace("\n", "").split(";")
        possible_game = True

        for draw in draws:
            if not possible_game:
                break

            parts = draw.split(",")

            for part in parts:
                i = 0
                number_str = ""
                while(part[i].isnumeric()):
                    number_str = number_str + part[i]
                    i += 1

                color = part[i:]

                if int(number_str) > rules[color]:
                    possible_game = False
                    break

        if possible_game:
            sum += int(line[:line.find(":")].replace("Game ", "").replace(":", ""))

    print(f"Sum PartOne: {sum}")


def part_two(input):
    sum = 0

    for line in input:
        draws = line[line.find(":"):].replace(":", "").replace(" ", "").replace("\n", "").split(";")
        min_amount = {
            "red": 0,
            "blue": 0,
            "green": 0
        }

        for draw in draws:
            parts = draw.split(",")

            for part in parts:
                i = 0
                number_str = ""
                while(part[i].isnumeric()):
                    number_str = number_str + part[i]
                    i += 1

                color = part[i:]

                if min_amount[color] < int(number_str):
                    min_amount[color] = int(number_str)

        power = 1
        for _, amount in min_amount.items():
            power = power * amount
    
        sum += power

    print(f"Sum PartTwo: {sum}")
    


test_1 = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

data = open("day02Input.txt", "r")
input = data.readlines()
data.close()

part_one(input)
part_two(input)