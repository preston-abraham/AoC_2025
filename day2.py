ids = input.split(',')

check_map = {
    1:[],
    2:[1],
    3:[1],
    4:[1,2],
    5:[1],
    6:[1,2,3],
    7:[1],
    8:[1,2,4],
    9:[1,3],
    10:[1,2,5]
}

def day2(part2 = False):
    invalid = []
    for i in ids:
        start = int(i.split('-')[0])
        end = int(i.split('-')[1])
        for j in range(start,end+1):
            num = str(j)
            if part2:
                check_nums = check_map[len(num)]
            else:
                if len(num) % 2:
                    check_nums = []
                else:
                    check_nums = [int(len(num) / 2)]
            for z in check_nums:
                seq = num[:z]
                if num.replace(seq,'') == '':
                    invalid += [num]
                    break
    return(sum(map(int,invalid)))

print(f'Part 1: {day2(False)} Part 2: {day2(True)}')
