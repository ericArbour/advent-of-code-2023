import re

num_regex = re.compile(r"\w+")


def traverse(map, dirs):
    current = "AAA"
    step_count = 0
    dir = dirs[0]

    while current != "ZZZ":
        step_count += 1
        l_child, r_child = map[current]
        current = l_child if dir == "L" else r_child
        dir = dirs[step_count % len(dirs)]

    return step_count


def parse_line(line):
    node, l_child, r_child = num_regex.findall(line)
    return node, (l_child, r_child)


def main():
    with open("./input.txt") as f:
        puzzle_input = f.read()

    dirs, rest = puzzle_input.split("\n\n")

    map = dict(parse_line(line) for line in rest.splitlines())
    step_count = traverse(map, dirs)

    print("answer", step_count)


if __name__ == "__main__":
    main()
