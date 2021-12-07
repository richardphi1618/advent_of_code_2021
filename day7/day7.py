def min_fuel_used(positions :list [int], min_pos: int, max_pos: int, start_pos: int, fuel_used) -> int:
	left = (start_pos - 1 + min_pos) // 2
	fuel_left = fuel_used(left, positions)

	right = (start_pos + 1 + max_pos) // 2
	fuel_right = fuel_used(right, positions)

	if right - left <= 1:
		return min(fuel_left, fuel_right)

	if fuel_left < fuel_right:
		return min_fuel_used(positions, min_pos, start_pos - 1, left, fuel_used)
	else:
		return min_fuel_used(positions, start_pos + 1, max_pos, right, fuel_used)


def fuel_used_1(new_pos: int, positions: list[int]) -> int:
    val = 0
    for i in positions:
       val += abs(new_pos - i)
    
    return val

def fuel_used_2(new_pos: int, positions: list[int]) -> int:
    val = 0
    for i in positions:
        #https://math.stackexchange.com/questions/593318/factorial-but-with-addition/593323
        n = abs(new_pos - i)
        val += (n * (n + 1)) // 2

    return val

def load_file(filename:str) -> list:
    my_file = open(filename, 'r')
    content = my_file.read()
    output = content.split(",")
    my_file.close()  

    for i in range(0, len(output)):
        output[i] = int(output[i])
    
    return output

def part1(filename:str) -> object:
    data = load_file(filename)
    start_pos = sum(data) / len(data)
    min_pos = min(data)
    max_pos = max(data)
    min_fuel = min_fuel_used(data, min_pos, max_pos, int(start_pos), fuel_used_1)

    print(min_fuel)
    return None

def part2(filename:str) -> None:
    data = load_file(filename)
    start_pos = sum(data) / len(data)
    min_pos = min(data)
    max_pos = max(data)
    min_fuel = min_fuel_used(data, min_pos, max_pos, int(start_pos), fuel_used_2)

    print(min_fuel)
    return None

if __name__ == '__main__':
    print("---------- Part 1 ----------")
    part1('day7/sampleset_ex.txt')
    print("---------- Part 2 ----------")
    part2('day6/sampleset_ex.txt')