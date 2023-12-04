def part_one(input):
    sum = 0

    for line in input:
        line = line[line.find(":"):]
        line = line.replace(":  ", ": ").replace(": ", "").replace("  ", " ").replace("\n", "")
        numbers = line.split(" | ")[0].split(" ")
        winning_numbers = line.split(" | ")[1].split(" ")

        match_count = 0
        for number in numbers:
            if number in winning_numbers:
                match_count += 1

        if match_count > 0:
            sum += 2**(match_count-1)

    print(f"Sum PartOne: {sum}")


def part_two(input):
    card_count = 0

    scratchcards = []
    for line in input:
        line = line[line.find(":"):]
        line = line.replace(":  ", ": ").replace(": ", "").replace("  ", " ").replace("\n", "")
        scratchcards.append([line, 1])

    for i, scratchcard in enumerate(scratchcards):
        numbers = scratchcard[0].split(" | ")[0].split(" ")
        winning_numbers = scratchcard[0].split(" | ")[1].split(" ")

        match_count = 0
        for number in numbers:
            if number in winning_numbers:
                match_count += 1

        number_of_cards = scratchcard[1]
        for j in range(match_count):
            scratchcards[i+j+1][1] += number_of_cards

        card_count += number_of_cards

    print(f"Sum PartTwo: {card_count}")




test_1 = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

data = open("day04Input.txt", "r")
input = data.readlines()
data.close()

#part_one(input)
part_two(input)