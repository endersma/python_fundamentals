import random
def randInt(min= 0, max= 100):
    if min > max:
        return False
    elif max < 0:
        return False
    range = max - min
    return round(random.random() * range + min)

print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
