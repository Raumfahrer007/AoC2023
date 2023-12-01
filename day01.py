def part_one(input):
    sum = 0


    for line in input:
        number = ""
        for char in line:
            if char.isnumeric():
                number += char
                break
        for i in reversed(range(len(line))):
            if line[i].isnumeric():
                number += line[i]
                sum += int(number)
                break
    print(f"Sum partOne: {sum}")


def part_two(input):
    numbers = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    ]

    sum = 0

    for line in input:
        number = ""
        for i in range(len(line)):
            if line[i].isnumeric():
                line_part = line[:i]
                if any(num in line_part for num in numbers):
                    number += return_first_string_number(line_part, numbers)
                    break
                else:
                    number += line[i]
                    break

        for i in reversed(range(len(line))):
            if line[i].isnumeric():
                line_part = line[i:]
                if any(num in line_part for num in numbers):
                    number += return_last_string_number(line_part, numbers)
                    break
                else:
                    number += line[i]
                    break

        if not number:
            number = return_first_string_number(line, numbers) + return_last_string_number(line, numbers)
        
        sum += int(number)
        
    print(f"Sum partTwo: {sum}")

def return_first_string_number(input, numbers):
    min_index = len(input)
    first_number = ""
    for i, number in enumerate(numbers):
        index = input.find(number)
        if not index == -1:
            if index < min_index:
                min_index = index
                first_number = str(i)
    return first_number

def return_last_string_number(input, numbers):
    max_index = 0
    last_number = ""
    for i, number in enumerate(numbers):
        index = 0
        temp_input = input
        new_index = temp_input.find(number)
        while not new_index == -1:
            index = new_index
            string_list = [*temp_input]
            string_list[index] = "_"
            temp_input = "".join(string_list)
            new_index = temp_input.find(number)

        if index > max_index:
            max_index = index
            last_number = str(i)
    return last_number



test_1 = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
]

test_2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]

data = open("day01Input.txt", "r")
input = data.readlines()
data.close()

#partOne(input)
part_two(input)