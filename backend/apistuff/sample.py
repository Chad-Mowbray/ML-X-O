import pickle


def prepare(data):
    prepared = [ map(lambda x: x % 10, coord) for coord in data ]
    print("prepared: ", prepared)
    base = [ [[0] for _ in range(0,10) ] for _ in range(0,10)]
    print("base: ", base)
    for x,y in prepared:
        base[x][y] = [1]
    flattened_res = [x[0] for y in base for x in y]
    return flattened_res

def add_sample(data, category):
    category = category
    processed = prepare(data)
    print(processed)
    return {"processed": processed, "category": category}


if __name__ == "__main__":
    d = [[16, 24], [16, 24], [16, 26], [16, 27], [16, 29], [16, 32], [16, 34], [16, 35], [16, 38], [16, 40], [16, 41], [16, 43], [16, 45], [16, 47], [17, 49], [17, 50], [19, 52], [20, 53], [21, 55], [24, 56], [25, 57], [29, 58], [31, 59], [34, 59], [38, 59], [41, 59], [45, 59], [46, 59], [49, 59], [51, 59], [54, 59], [55, 59], [56, 58], [57, 58], [58, 56], [59, 55], [59, 53], [60, 52], [60, 49], [61, 46], [61, 43], [61, 39], [61, 35], [60, 30], [58, 26], [56, 21], [53, 17], [51, 13], [49, 12], [47, 10], [45, 8], [42, 7], [40, 6], [38, 5], [36, 5], [34, 5], [31, 5], [30, 5], [28, 5], [27, 5], [25, 5], [24, 5], [23, 5], [21, 5], [20, 6], [19, 8], [18, 9], [16, 11], [14, 13], [13, 16], [11, 17], [10, 20], [8, 22], [6, 25], [5, 27], [4, 28], [3, 30], [2, 31], [2, 32], [1, 33], [1, 34], [1, 34], [1, 36], [1, 36]]
    add_sample(d, "x")