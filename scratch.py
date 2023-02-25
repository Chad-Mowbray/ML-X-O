import pickle

# stuff = pickle.load(open("draw-search-api/stuff.pickle", "rb"))
# print(stuff[0])
# print(len(stuff))
# print(len(stuff[0]))

cleaned = [
  [
      [
          9,
          1
      ],
      [
          9,
          1
      ],
      [
          9,
          2
      ],
      [
          0,
          4
      ],
      [
          1,
          5
      ],
      [
          3,
          7
      ],
      [
          4,
          8
      ],
      [
          5,
          0
      ],
      [
          8,
          3
      ],
      [
          0,
          5
      ],
      [
          2,
          7
      ],
      [
          3,
          8
      ],
      [
          4,
          0
      ],
      [
          6,
          2
      ],
      [
          7,
          3
      ],
      [
          8,
          4
      ],
      [
          9,
          5
      ],
      [
          9,
          6
      ],
      [
          0,
          7
      ],
      [
          0,
          8
      ],
      [
          0,
          8
      ],
      [
          1,
          9
      ],
      [
          1,
          0
      ],
      [
          1,
          0
      ],
      [
          1,
          0
      ],
      [
          1,
          1
      ],
      [
          1,
          2
      ],
      [
          1,
          2
      ]
  ]
]

cleaned = cleaned[0]
# print(cleaned)


base = [ [[0] for x in range(0,10) ] for y in range(0,10)]
# print(base)

for x,y in cleaned:
    base[x][y] = [1]
    # print(x,y)
    # print(base[x][y])

# print(base)

flattened_res = [x[0] for y in base for x in y]
print(flattened_res)
print(len(flattened_res))

# ready = 