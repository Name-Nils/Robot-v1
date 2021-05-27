def distance(dist):
    distance = dist * 200 #add wheel diameter
    return distance

def direction(direction):
    if direction == "w":
        return [True, True]
    if direction == "s":
        return [False, False]
    if direction == "a":
        return [False, True]
    if direction == "d":
        return [True, False]

