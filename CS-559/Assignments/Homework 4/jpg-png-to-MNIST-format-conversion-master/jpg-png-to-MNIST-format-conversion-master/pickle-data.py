import pickle
PIK = "custom-data-pickle.dat"

objects = []
with (open(PIK, "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break

print((objects[0][1][0].shape))