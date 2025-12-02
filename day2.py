# Part 1
invalid = []
for i in ids:
    start = int(i.split('-')[0])
    end = int(i.split('-')[1])
    for j in range(start,end+1):
        if not len(str(j)) % 2:
            midpoint = int(len(str(j)) / 2)
            if str(j)[:midpoint] == str(j)[midpoint:]:
                invalid += [str(j)]
                
print(sum([int(e) for e in invalid]))

# Part 2
invalid = []
for i in ids:
    start = int(i.split('-')[0])
    end = int(i.split('-')[1])
    for j in range(start,end+1):
        num = str(j)
        for z in range(1,9):
            if len(num) > z:
                seq = num[:z]
                if num.replace(seq,'') == '':
                    invalid += [num]
                    break
print(sum([int(e) for e in invalid]))
