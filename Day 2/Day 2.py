with open('input') as f:
    integers = [line.rstrip() for line in f]
x = integers[0].split(',')
integers = []
for y in x:
    integers.append(int(y))  # Wow, what an inefficient way to do that.
integers[1] = 12
integers[2] = 2
print(integers)

input()

def part_one():
    noun = 12
    verb = 2
    intcode(noun, verb)

def intcode(noun, verb):
    integerss = integers.copy()  # There's definitely a better way than this, right?
    address = 0
    integerss[1] = noun
    integerss[2] = verb
    x = 0
    while x != 99:
        x = integers[address]
        print("address: " + str(address))
        print(x)
        if x == 1:
            integerss[integerss[address + 3]] = integerss[integerss[address + 1]] + integerss[integerss[address + 2]]
            address += 4
        if x == 2:
            integerss[integerss[address + 3]] = integerss[integerss[address + 1]] * integerss[integerss[address + 2]]
            address += 4
    return integerss[0]

def part_two():
    noun = 0
    verb = 0
    while True:
        print("noun is " + str(noun))
        print("verb is " + str(verb))
        value = intcode(noun, verb)
        print(value)
        if value == 19690720:
            print(100 * noun + verb)
            break
        if verb < 100:  # This can be better somehow....
            verb += 1
        if verb == 99:
            noun += 1
            verb = 0


# part_one()

part_two()

