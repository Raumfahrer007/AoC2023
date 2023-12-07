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

hand_values = {
    "5": 6000000000000,
    "41": 5000000000000,
    "32": 4000000000000,
    "311": 3000000000000,
    "221": 2000000000000,
    "2111": 1000000000000,
    "11111": 0
}

def part_one(input):
    sum = 0
    hands = []

    for line in input:
        hand = line.split(" ")[0]
        bid = line.split(" ")[1]

        hand_count = {}
        hand_number = 0
        k = 10000000000
        for card in hand:
            hand_number += int(card_values[card]) * k
            k //= 100
            if not card in hand_count.keys():
                hand_count[card] = 1
            else:
                hand_count[card] += 1

        sorted_hand_count = "".join(str(card) for card in sorted(hand_count.values(), reverse=True))

        hand_number += hand_values[sorted_hand_count]
        hands.append([hand_number, int(bid)])

    sorted_hands = sorted(hands, key=lambda l:l[0])
    
    for i, hand in enumerate(sorted_hands):
        sum += hand[1] * (i+1)

    print(f"Sum PartOne: {sum}")

def part_two(input):
    pass


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

    part_one(input)
    #part_two(input)