import multiprocessing

def part_one(input):
    str_seeds = input[0].replace("seeds: ", "").split(" ")
    seeds = [int(str_seed) for str_seed in str_seeds]
    maps = get_maps(input)

    location_numbers = []
    for seed in seeds:
        source_value = seed
        for map in maps:
            for entry in map:
                if source_value >= entry[1][0] and source_value <= entry[1][1]:
                    difference = source_value - entry[1][0]
                    source_value = entry[0][0] + difference
                    break

        location_numbers.append(source_value)
        seed += 1

    location_numbers.sort()
    print(f"Lowest LocationNumber: {location_numbers[0]}")


def part_two(input):
    str_seeds = input[0].replace("seeds: ", "").split(" ")
    seeds_ranges = []
    for i in range(0, len(str_seeds) - 1, 2):
        seeds_ranges.append([int(str_seeds[i]), int(str_seeds[i]) + int(str_seeds[i+1]) - 1])

    maps = get_maps(input)

    manager = multiprocessing.Manager()
    lowest_locations = manager.list()
    step = -20
    while not lowest_locations:
        step += 20
        jobs = []
        for i in range(20):
            location_range = [(step+i) * 500000, ((step+i+1) * 500000) - 1]
            process = multiprocessing.Process(target=find_lowest_possible_location, args=(location_range, maps, seeds_ranges, lowest_locations, i))
            jobs.append(process)
            process.start()

        for process in jobs:
            process.join()

    lowest_locations.sort()
    print(f"Lowest LocationNumber: {lowest_locations[0]}")


def find_lowest_possible_location(location_range, maps, seeds_ranges, lowest_locations, i):
    print(f"Start Thread {i} - {location_range}")
    location = location_range[0]
    while location <= location_range[1]:
        destination_value = location
        possible = False

        for map in reversed(maps):
            for entry in map:
                if destination_value >= entry[0][0] and destination_value <= entry[0][1]:
                    difference = destination_value - entry[0][0]
                    destination_value = entry[1][0] + difference
                    break
        
        for seed_range in seeds_ranges:
            if destination_value >= seed_range[0] and destination_value <= seed_range[1]:
                possible = True
                break

        if possible:
            lowest_locations.append(location)
            break
        else:
            location += 1

    print(f"End Thread {i}")


def get_maps(input):
    maps = []
    j = -1
    k = 0

    for i in range(1, len(input)):
        line = input[i]

        if "map" in line:
            j += 1
            k = 0
            maps.append([])
            continue

        if line == "\n":
            continue

        map_values = line.split(" ")
        maps[j].append([])
        maps[j][k].append([int(map_values[0]), int(map_values[0]) + int(map_values[2]) - 1])
        maps[j][k].append([int(map_values[1]), int(map_values[1]) + int(map_values[2]) - 1])
        k += 1

    return maps



test_1 = [
    "seeds: 79 14 55 13",

    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",

    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",

    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",

    "water-to-light map:",
    "88 18 7",
    "18 25 70",

    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",

    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",

    "humidity-to-location map:",
    "60 56 37",
    "56 93 4"
]

if __name__ == "__main__":
    data = open("day05Input.txt", "r")
    input = data.readlines()
    data.close()

    part_one(input)
    part_two(input)