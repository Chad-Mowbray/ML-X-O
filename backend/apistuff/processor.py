from copy import deepcopy
import pickle



def prepare_db_samples_for_training(all_samples):
    return [{"processed": s.data, "category": s.category} for s in all_samples]

def round_points(raw_line_data):
    return [
        [round(coord["x"]), round(coord["y"])]
        for line in raw_line_data
        for coord in line
    ]

def bucket_coord_points(rounded_points):
    return [
        map(lambda x: x % 10, coord) for coord in rounded_points 
    ]

def get_zeroed_array():
    return [ 
        [[0] for _ in range(0,10)] for _ in range(0,10)
    ]

def fill_zeroed_array(zeroed_array, bucketed_points):
    zeroed_copy = deepcopy(zeroed_array)
    for x,y in bucketed_points:
        zeroed_copy[x][y] = [1]
    return zeroed_copy

def flatten_filled_array(filled_array):
    return [x[0] for y in filled_array for x in y]

def transform_raw_line_data(raw_line_data):
    rounded_points = round_points(raw_line_data)
    bucketed_points = bucket_coord_points(rounded_points)
    zeroed_array = get_zeroed_array()
    filled_array = fill_zeroed_array(zeroed_array, bucketed_points)
    flattened_filled_array = flatten_filled_array(filled_array)
    return flattened_filled_array

def guess(data):
    model = pickle.load(open("current_model.pickle", "rb"))
    return model.predict([data])[0]