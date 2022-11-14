import os
print(os.listdir("."))
print(__file__)
print(os.path.dirname(__file__))
fileName = os.path.join(os.path.dirname(__file__),"test.txt")
with open(fileName,"r")  as file:
    for line in file:
        print(line)