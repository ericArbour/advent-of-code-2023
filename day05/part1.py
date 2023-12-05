import re
from dataclasses import dataclass

num_regex = re.compile(r"\d+")


@dataclass(frozen=True)
class Translator:
    src_range: tuple[int]
    dst_range: tuple[int]


@dataclass(frozen=True)
class AlmanacMap:
    translators: list[Translator]


def line_to_translator(line):
    dst_range_start, src_range_start, range_len = [int(x) for x in line.split(" ")]
    src_range = (src_range_start, src_range_start + range_len - 1)
    dst_range = (dst_range_start, dst_range_start + range_len - 1)
    return Translator(src_range, dst_range)


def map_section_str_to_almanac_map(map_section_str):
    _, *range_strs = map_section_str.splitlines()
    translators = [line_to_translator(line) for line in range_strs]
    sorted_translators = sorted(translators, key=lambda x: x.src_range[0])
    return AlmanacMap(sorted_translators)


def process_seed(seed, almanac_maps: list[AlmanacMap]):
    for almanac_map in almanac_maps:
        for translator in almanac_map.translators:
            if translator.src_range[0] <= seed <= translator.src_range[1]:
                seed = translator.dst_range[0] + seed - translator.src_range[0]
                break

    return seed


def main():
    with open("input.txt", "r") as f:
        puzzle_input = f.read()

    seeds_section_str, *map_section_strs = puzzle_input.split("\n\n")
    seeds = [int(seed) for seed in num_regex.findall(seeds_section_str)]
    almanac_maps = [
        map_section_str_to_almanac_map(map_section_str)
        for map_section_str in map_section_strs
    ]

    answer = min(process_seed(seed, almanac_maps) for seed in seeds)
    print("answer", answer)


if __name__ == "__main__":
    main()
