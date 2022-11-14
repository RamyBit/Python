import os
folder = os.path.join(os.path.dirname(__file__),"names")
counter = 0
for filename in os.listdir(folder):
    filedir= os.path.join(folder, filename)
    with open (filedir,"r", encoding="utf-8") as file:
        for line in file:
            data = line.strip().split(" ")
            if data[0] == "Max":
                counter += 1

print (counter)