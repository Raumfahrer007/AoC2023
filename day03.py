def part_one(input):
    sum = 0
    operations = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    i = 0

    while i < len(input):
        line = input[i]
        j = 0
        while j < len(line):
            engine_number = False

            if line[j].isnumeric():
                number_start = j
                number_end = -1
                number_str = line[j]

                try:
                    while line[j+1].isnumeric():
                        j += 1
                        number_str += line[j]
                except IndexError:
                    pass
                finally:
                    number_end = j

                for k in range(number_start, number_end + 1):
                    for operation in operations:
                        if i + operation[0] < 0 or i + operation[0] >= len(input) or k + operation[1] < 0 or k + operation[1] >= len(line):
                            continue

                        field_to_check = input[i + operation[0]][k + operation[1]]
                        if not field_to_check.isnumeric() and not field_to_check == "." and not field_to_check == "\n":
                            engine_number = True
                            break
                    
                    if engine_number:
                        sum += int(number_str)
                        break 

            j += 1
        i += 1
    print(f"Sum PartOne: {sum}")



def part_two(input):
    sum = 0
    i = 0
    GEAR = "*"
    operations = [[-1, -1], [0, 1], [1, -1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    line_operations = [-1, 1]

    for i, line in enumerate(input):
        j = 0
        for j in range(len(line)):
            if line[j] == GEAR:
                numbers = []

                if line[j + 1].isnumeric(): #Right
                    str_number = get_number_right(line, j+1, "")
                    numbers.append(int(str_number))

                if line[j - 1].isnumeric(): #Left
                    str_number = get_number_left(line, j-1, "")
                    numbers.append(int(str_number))

                for operation in line_operations:
                    if i + operation < 0 or i + operation >= len(input):
                        continue

                    line_to_check = input[i + operation]
                    if line_to_check[j].isnumeric():
                        str_number = get_number_right(line_to_check, j, "")
                        str_number = get_number_left(line_to_check, j - 1, str_number)
                        numbers.append(int(str_number))

                    else:
                        try:
                            if line_to_check[j + 1].isnumeric():
                                str_number = get_number_right(line_to_check, j + 1, "")
                                numbers.append(int(str_number))
                        except IndexError:
                            pass

                        try:
                            if line_to_check[j - 1].isnumeric():
                                str_number = get_number_left(line_to_check, j - 1, "")
                                numbers.append(int(str_number))
                        except IndexError:
                            pass

                if len(numbers) == 2:
                    sum += (numbers[0] * numbers[1])

    print(f"Sum PartTwo: {sum}")


def get_number_right(line, k, str_number):
    while line[k].isnumeric():
        str_number += line[k]
        k += 1
        if k >= len(line):
            break
    return str_number

def get_number_left(line, k, str_number):
    while line[k].isnumeric():
        str_number = line[k] + str_number
        k -= 1
        if k < 0:
            break
    return str_number
                    


                    
                    
                    


test_1 = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

data = open("day03Input.txt", "r")
input = data.readlines()
data.close()

part_one(input)
part_two(input)