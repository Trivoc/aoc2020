from time import time


def read_input_split(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def parse_line(line):
    list = [i for i, c in enumerate(line) if c == '#']
    hash = sum(2**i for i in list)
    flipped_hash = sum(2**(9-i) for i in list)
    return hash, flipped_hash, list



def parse_tile(tile):
    borders = {}
    borders['UP'] = parse_line(tile[0])
    borders['DOWN'] = parse_line(tile[9])
    borders['LEFT'] = parse_line([row[0] for row in tile])
    borders['RIGHT'] = parse_line([row[9] for row in tile])
    return borders


def count_occurence(occ_dict, hash, tile):
    if hash not in occ_dict:
        occ_dict[hash] = [tile]
    else:
        occ_dict[hash].append(tile)


def build_tiles(inp):
    tiles = {}
    for tile_string in inp:
        tile = tile_string.split('\n')
        current_tile = int(tile[0][:-1].split(' ')[1])
        tiles[current_tile] = parse_tile(tile[1:])
    return tiles

def build_hash_ref(tiles):
    occurrences = {}
    for tile, borders in tiles.items():
        for h, f_hash, border in borders.values():
            count_occurence(occurrences, h, tile)
            count_occurence(occurrences, f_hash, tile)
    return occurrences


def solve_part_1(inp):
    tiles = build_tiles(inp)
    hash_ref = build_hash_ref(tiles)
    free_side_count = {}

    for h, tile in ((h, tile) for h, tile in hash_ref.items() if len(tile) == 1):
        if tile[0] in free_side_count:
            free_side_count[tile[0]] += 1
        else:
            free_side_count[tile[0]] = 0
    result = 1
    for tile, count in free_side_count.items():
        if count > 1:
            result = tile * result
            print('Corner found, tile id', tile)
    return result


def invert(dir):
    reverse = {
        'UP': 'DOWN',
        'DOWN': 'UP',
        'LEFT': 'RIGHT',
        'RIGHT': 'LEFT'
    }
    return reverse[dir]



def orient_neigbour(neighbouring_tile, hsh, hash_target_dir):
    pass



def find_neighbour(dir, tile_id, tiles, hash_ref):
    tile = tiles[tile_id]
    hsh, _, border = tile[dir]
    neighbouring_tile = [h for h in hash_ref[hsh] if h != tile_id][0]
    print(tiles[neighbouring_tile])

    hash_target_dir = invert(dir)
    orient_neigbour(neighbouring_tile, hsh, hash_target_dir)



def solve_part_2(inp):
    tiles = build_tiles(inp)
    hash_ref = build_hash_ref(tiles)

    #Flip first tile to be in top left, for simplicity of use.
    # 1327 is, by default orientation, top left. Can write code to automate finding later.
    print(tiles[1327  ])
    find_neighbour('RIGHT', 1327, tiles, hash_ref)






split_input = read_input_split('\n\n')

start = time()
solution1 = solve_part_1(split_input)
solution2 = solve_part_2(split_input)
stop = time()

print(f'Part 1 solution: {solution1}')
print(f'Part 2 solution: {solution2}')
print(f'Total time: {stop - start}')
