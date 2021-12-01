def main():
    data = read_data()

    print(part_the_first(data))
    print(part_the_second(data))


def read_data():
    with open('data') as file:
        return [int(line.strip()) for line in file]


def part_the_first(data):
    return sum(map(lambda x: x[0] < x[1], zip(data, data[1:])))


def part_the_second(data):
    tmp = [x + y + z for x, y, z in zip(data, data[1:], data[2:])]
    return part_the_first(tmp)


if __name__ == "__main__":
    main()
