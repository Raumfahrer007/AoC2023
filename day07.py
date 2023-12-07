hand_values = {
    "5": 60000000000,
    "41": 50000000000,
    "32": 40000000000,
    "311": 30000000000,
    "221": 20000000000,
    "2111": 10000000000,
    "11111": 0
}

def part_one(input):
    card_values = {
        "A": 12,
        "K": 11,
        "Q": 10,
        "J": 9,
        "T": 8,
        "9": 7,
        "8": 6,
        "7": 5,
        "6": 4,
        "5": 3,
        "4": 2,
        "3": 1,
        "2": 0
    }

    sum = 0
    hands = []

    for line in input:
        hand = line.split(" ")[0]
        bid = line.split(" ")[1]

        hand_count = {}
        hand_number = 0
        k = 100000000
        for card in hand:
            hand_number += int(card_values[card]) * k
            k //= 100
            if not card in hand_count.keys():
                hand_count[card] = 1
            else:
                hand_count[card] += 1

        sorted_hand_count_string = "".join(str(count) for count in sorted(hand_count.values(), reverse=True))

        hand_number += hand_values[sorted_hand_count_string]
        hands.append([hand_number, int(bid)])

    sorted_hands = sorted(hands, key=lambda l:l[0])
    
    for i, hand in enumerate(sorted_hands):
        sum += hand[1] * (i+1)

    print(f"Sum PartOne: {sum}")

def part_two(input):
    card_values = {
        "A": 12,
        "K": 11,
        "Q": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
        "J": 0,
    }

    sum = 0
    hands = []

    for line in input:
        hand = line.split(" ")[0]
        bid = line.split(" ")[1]

        hand_count = {}
        hand_number = 0
        k = 100000000
        for card in hand:
            hand_number += int(card_values[card]) * k
            k //= 100
            if not card in hand_count.keys():
                hand_count[card] = 1
            else:
                hand_count[card] += 1

        sorted_hand_count = dict(sorted(hand_count.items(), key=lambda item:item[1], reverse=True))

        if "J" in sorted_hand_count.keys():
            if not sorted_hand_count["J"] == 5:
                first_key = list(sorted_hand_count.keys())[0]
                if first_key == "J":
                    first_key = list(sorted_hand_count.keys())[1]

                sorted_hand_count[first_key] += sorted_hand_count["J"]
                del sorted_hand_count["J"]


        sorted_hand_count_string = "".join(str(count) for count in sorted_hand_count.values())

        hand_number += hand_values[sorted_hand_count_string]
        hands.append([hand_number, int(bid)])

    sorted_hands = sorted(hands, key=lambda l:l[0])
    
    for i, hand in enumerate(sorted_hands):
        sum += hand[1] * (i+1)

    print(f"Sum PartTwo: {sum}")


test_1 = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483"
]

if __name__ == "__main__":
    data = open("day07Input.txt", "r")
    input = data.readlines()
    data.close()

    #part_one(input)
    part_two(input)