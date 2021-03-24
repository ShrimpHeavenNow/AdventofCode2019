with open('input') as f:
    poop = [line.rstrip() for line in f]
wires = []
for q in poop:  # I feel like I knew how to do this not shittily before.
    q = q.split(",")
    wires.append(q)

print(wires)


def find_points(wire):
    points = set()
    x = 0
    y = 0
    for z in wire:
        if z[0] == "U":
            for _ in range(int(z[1:])):
                y += 1
                points.add((x, y))
        if z[0] == "D":
            for _ in range(int(z[1:])):
                y -= 1
                points.add((x, y))
        if z[0] == "L":
            for _ in range(int(z[1:])):
                x -= 1
                points.add((x, y))
        if z[0] == "R":
            for _ in range(int(z[1:])):
                x += 1
                points.add((x, y))
    return points


line_a = find_points(wires[0])
line_b = find_points(wires[1])
common = line_a & line_b
print("farts")
print(common)
