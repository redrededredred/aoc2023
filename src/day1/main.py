def part1():
    with open("input.txt", "r") as file:
        sum = 0
        for line in file.readlines():
            combined_number = "" 
            for char in line.strip():
                if char.isdigit():
                    combined_number += char
                    break
            for char in reversed(line.strip()):
                if char.isdigit():
                    combined_number += char
                    break
            sum += int(combined_number)
    
    return num

def part2():
    with open("input.txt", "r") as file:
        sum = 0
        possible_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        for line in file.readlines():
            combined_number = ""
            if possible_numbers in

print(part1())