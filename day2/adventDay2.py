from os import path


def main():
    filepath = path.abspath(path.join(__file__, "..", "input"))
    data = read_data(filepath)

    part_one(data)
    part_two(data)


def read_data(filename):
    with open(filename) as file:
        return [x.rstrip().split(" ") for x in file.readlines()]


def part_one(data):
    pos = (0, 0)
    for x in data:
        pos = func_table[x[0]](pos, int(x[1]))

    print(pos[0] * pos[1])


def part_two(data):
    pos = (0, 0, 0)
    for x in data:
        pos = func_table1[x[0]](pos, int(x[1]))

    print(pos[0] * pos[1])


def f1(pos, x):
    return (pos[0] + x, pos[1] + (x * pos[2]), pos[2])


def u1(pos, z):
    return (pos[0], pos[1], pos[2] - z)


def d1(pos, z):
    return (pos[0], pos[1], pos[2] + z)


def forward(pos, x):
    return (pos[0] + x, pos[1])


def up(pos, y):
    return (pos[0], pos[1] - y)


def down(pos, y):
    return (pos[0], pos[1] + y)


func_table = {
    "forward": forward,
    "up": up,
    "down": down
}

func_table1 = {
    "forward": f1,
    "up": u1,
    "down": d1
}


if __name__ == "__main__":
    main()
