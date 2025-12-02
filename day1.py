def day1(part2 = False):
    dial = 50
    tot = 0
    for i in inp.split('\n'):
        spin = int(i[1:])
        if part2:
            pre_spin_dial = dial
            tot += spin // 100
        if i[0] == 'L':
            spin *= -1
        dial = (dial + spin) % 100
        if dial == 0:
            tot += 1
        if part2 and (dial != 0 and pre_spin_dial != 0) and ((spin > 0 and dial < pre_spin_dial) or (spin < 0 and dial > pre_spin_dial)):
            tot += 1
    return tot

print(f'{day1()} {day1(True)}')
