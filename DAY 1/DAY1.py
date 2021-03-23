import math
with open('input') as f:
    masses = [int(line.rstrip()) for line in f]

# Part One
# total_mass = 0
# for x in masses:
#     fart = x//3
#     fart -= 2
#     total_mass += fart
#
# print(total_mass)
total_mass = 0
for x in masses:
    fart = x//3
    fart -= 2
    total_mass += fart
    print(fart)
    while fart > 0:
        fart = fart // 3
        fart -= 2
        print(fart)
        if fart > 0:
            total_mass += fart





print(total_mass)
