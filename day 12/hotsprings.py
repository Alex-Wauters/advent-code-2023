def is_correct(line, ecc) -> bool:
    if line.count('#') != sum(ecc):
        return False
    groups = [i.count('#') for i in list(filter(lambda i: i != '', line.split('.')))]
    return groups == ecc


def is_partially_correct(line, ecc) -> bool:
    part = line.split('?')[0]
    groups = [i.count('#') for i in list(filter(lambda i: i != '', part.split('.')))]
    if len(groups) == 0:
        return True
    if len(groups) > len(ecc):
        return False
    for i in range(len(groups) - 1):
        if groups[i] != ecc[i]:
            return False
    return groups[len(groups)-1] <= ecc[len(groups)-1]


def count_if_partially_correct(line, ecc) -> int:
    return 0 if not is_partially_correct(line, ecc) else count_sets(line, ecc)

def count_sets(line, ecc) -> int:
    if line.count('?') > 0:
        return count_if_partially_correct(line.replace('?', '#', 1), ecc) + count_if_partially_correct(line.replace('?', '.', 1), ecc)
    return 1 if is_correct(line, ecc) else 0


with open("input.txt", "r") as file:
    lines = file.readlines()
    part1, part2 = 0, 0
    for line in lines:
        parts = line.split(" ")
        part1 += count_sets(parts[0], [int(x) for x in parts[1].split(",")])
    print(part1)
    for i, line in enumerate(lines):
        parts = line.split(" ")
        part2 += count_sets(("?".join([parts[0]]*5)), [int(x) for x in parts[1].split(",")]*5)
        if i % 100 == 0:
            print('completed', i)
    print(part2)
