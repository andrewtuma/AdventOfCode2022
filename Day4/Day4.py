with open('Day4/test_input2.txt') as f:
    lines = f.readlines()

data = [x[:-1] for x in lines]
data = [x for xs in data for x in xs.split(',')]
data = [x for xs in data for x in xs.split('-')]
data = [ int(x) for x in data ]

def part1(results):
    count1 = 0
    i = 0
    while i <= len(results)-3:
        if (results[i] <= results[i+2]) and (results[i+1] >= results[i+3]):
            # print(f'{results[i]}-{results[i+1]}, {results[i+2]}-{results[i+3]}')
            count1 += 1

        elif (results[i] >= results[i+2]) and (results[i+1] <= results[i+3]):
            # print(f'{results[i]}-{results[i+1]}, {results[i+2]}-{results[i+3]}')
            count1 += 1
        i += 4
    print("Part 1 count: ", count1)



def overlap(start1, end1, start2, end2):
    return (
        start1 <= start2 <= end1 or
        start1 <= end2 <= end1 or
        start2 <= start1 <= end2 or
        start2 <= end1 <= end2
        )

def part2(result):
    count2 = 0
    i = 0
    while i <= len(result)-3:
        if overlap(result[i], result[i+1], result[i+2], result[i+3]):
            count2 += 1
        i += 4
    print("Part 2 count: ", count2)


part1(data)
part2(data)
