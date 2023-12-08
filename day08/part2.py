import re
import math

num_regex = re.compile(r"\w+")


def get_step_cycle(map, dirs, initial_node):
    current = initial_node
    step_count = 0
    dir = dirs[0]
    z_cycle_step = None

    while z_cycle_step is None:
        if current.endswith("Z"):
            z_cycle_step = step_count
        step_count += 1
        l_child, r_child = map[current]
        current = l_child if dir == "L" else r_child
        dir = dirs[step_count % len(dirs)]

    return z_cycle_step


def parse_line(line):
    node, l_child, r_child = num_regex.findall(line)
    return node, (l_child, r_child)


def main():
    with open("./input.txt") as f:
        puzzle_input = f.read()

    dirs, rest = puzzle_input.split("\n\n")

    map = dict(parse_line(line) for line in rest.splitlines())
    cycles = [
        get_step_cycle(map, dirs, node) for node in map.keys() if node.endswith("A")
    ]
    answer = math.lcm(*cycles)
    print("answer", answer)


if __name__ == "__main__":
    main()
