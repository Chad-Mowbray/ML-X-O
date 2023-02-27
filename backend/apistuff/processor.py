
import pickle

def guess(data):
    model = pickle.load(open("current_model.pickle", "rb"))
    return model.predict([data])[0]

if __name__ == "__main__":
    data = [[1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1]]
    print(guess(data))

    rawLineData = [
    [
        {
            "x": 25.247726440429688,
            "y": 23.217666625976562
        },
        {
            "x": 26.064849853515625,
            "y": 24.851913452148438
        },
        {
            "x": 27.92156982421875,
            "y": 27.172821044921875
        },
        {
            "x": 29.889678955078125,
            "y": 30.124984741210938
        },
        {
            "x": 32.48915100097656,
            "y": 33.764251708984375
        },
        {
            "x": 33.71482849121094,
            "y": 34.98992919921875
        },
        {
            "x": 36.834197998046875,
            "y": 38.10929870605469
        },
        {
            "x": 39.43367004394531,
            "y": 41.748565673828125
        },
        {
            "x": 42.55303955078125,
            "y": 44.86793518066406
        },
        {
            "x": 45.67240905761719,
            "y": 47.9873046875
        },
        {
            "x": 48.132537841796875,
            "y": 50.939453125
        },
        {
            "x": 49.35821533203125,
            "y": 52.165130615234375
        },
        {
            "x": 53.19273376464844,
            "y": 55.999664306640625
        },
        {
            "x": 53.8988037109375,
            "y": 56.705718994140625
        },
        {
            "x": 55.64424133300781,
            "y": 58.014801025390625
        },
        {
            "x": 56.86991882324219,
            "y": 59.240478515625
        },
        {
            "x": 57.57598876953125,
            "y": 59.946563720703125
        },
        {
            "x": 57.90129089355469,
            "y": 60.2718505859375
        },
        {
            "x": 58.25431823730469,
            "y": 60.977935791015625
        },
        {
            "x": 58.579620361328125,
            "y": 61.30322265625
        }
    ],
    [
        {
            "x": 71.64241027832031,
            "y": 22.830047607421875
        },
        {
            "x": 70.93634033203125,
            "y": 22.830047607421875
        },
        {
            "x": 69.79399108886719,
            "y": 22.830047607421875
        },
        {
            "x": 69.46868896484375,
            "y": 23.155349731445312
        },
        {
            "x": 68.32633972167969,
            "y": 23.916915893554688
        },
        {
            "x": 67.18399047851562,
            "y": 24.678482055664062
        },
        {
            "x": 66.47792053222656,
            "y": 25.384552001953125
        },
        {
            "x": 65.7718505859375,
            "y": 25.737579345703125
        },
        {
            "x": 64.62950134277344,
            "y": 26.118362426757812
        },
        {
            "x": 63.923431396484375,
            "y": 26.824432373046875
        },
        {
            "x": 63.21736145019531,
            "y": 27.177459716796875
        },
        {
            "x": 62.07501220703125,
            "y": 27.93902587890625
        },
        {
            "x": 61.36894226074219,
            "y": 28.29205322265625
        },
        {
            "x": 60.226593017578125,
            "y": 29.053619384765625
        },
        {
            "x": 59.08424377441406,
            "y": 29.815185546875
        },
        {
            "x": 57.94189453125,
            "y": 30.195968627929688
        },
        {
            "x": 57.23582458496094,
            "y": 30.548995971679688
        },
        {
            "x": 56.093475341796875,
            "y": 31.310562133789062
        },
        {
            "x": 54.95112609863281,
            "y": 31.69134521484375
        },
        {
            "x": 54.24505615234375,
            "y": 32.04437255859375
        },
        {
            "x": 53.10270690917969,
            "y": 32.805938720703125
        },
        {
            "x": 51.960357666015625,
            "y": 33.18672180175781
        },
        {
            "x": 50.81800842285156,
            "y": 33.5675048828125
        },
        {
            "x": 49.6756591796875,
            "y": 34.329071044921875
        },
        {
            "x": 48.96958923339844,
            "y": 34.682098388671875
        },
        {
            "x": 47.827239990234375,
            "y": 35.06288146972656
        },
        {
            "x": 47.12117004394531,
            "y": 35.41590881347656
        },
        {
            "x": 46.41510009765625,
            "y": 35.76893615722656
        },
        {
            "x": 45.70903015136719,
            "y": 36.475006103515625
        },
        {
            "x": 45.002960205078125,
            "y": 36.828033447265625
        },
        {
            "x": 44.29689025878906,
            "y": 37.53410339355469
        },
        {
            "x": 43.154541015625,
            "y": 38.29566955566406
        },
        {
            "x": 41.928863525390625,
            "y": 39.52134704589844
        },
        {
            "x": 40.70318603515625,
            "y": 40.74702453613281
        },
        {
            "x": 39.56083679199219,
            "y": 41.50859069824219
        },
        {
            "x": 38.33515930175781,
            "y": 42.73426818847656
        },
        {
            "x": 36.70091247558594,
            "y": 43.5513916015625
        },
        {
            "x": 34.3800048828125,
            "y": 45.408111572265625
        },
        {
            "x": 33.23765563964844,
            "y": 45.78889465332031
        },
        {
            "x": 31.603408813476562,
            "y": 46.60601806640625
        },
        {
            "x": 29.969161987304688,
            "y": 47.42314147949219
        },
        {
            "x": 28.334915161132812,
            "y": 48.240264892578125
        },
        {
            "x": 27.19256591796875,
            "y": 49.0018310546875
        },
        {
            "x": 26.050216674804688,
            "y": 49.763397216796875
        },
        {
            "x": 23.868423461914062,
            "y": 51.072479248046875
        },
        {
            "x": 23.162353515625,
            "y": 51.778533935546875
        },
        {
            "x": 22.456283569335938,
            "y": 52.484619140625
        },
        {
            "x": 21.230606079101562,
            "y": 53.710296630859375
        },
        {
            "x": 20.5245361328125,
            "y": 54.416351318359375
        },
        {
            "x": 19.762969970703125,
            "y": 55.5587158203125
        },
        {
            "x": 19.437667846679688,
            "y": 55.884002685546875
        },
        {
            "x": 18.731597900390625,
            "y": 56.590087890625
        },
        {
            "x": 18.731597900390625,
            "y": 56.915374755859375
        },
        {
            "x": 18.406295776367188,
            "y": 57.240692138671875
        }
    ]
]
