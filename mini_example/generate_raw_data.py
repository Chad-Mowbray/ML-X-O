import random
import csv

def too_hot(): return {"response": "too hot", "temp": random.randrange(72,100)}
def just_right(): return {"response": "just right", "temp": random.randrange(65, 75)}
def too_cold(): return {"response": "too cold", "temp": random.randrange(40, 68)}

raw = [too_hot() for _ in range(300)] + [just_right() for _ in range(75)] + [too_cold() for _ in range(300)]

random.shuffle(raw)
random.shuffle(raw)
random.shuffle(raw)


with open("raw_data.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["response", "temp"])
    writer.writeheader()
    writer.writerows(raw)




