import os
folder = os.path.join(os.path.dirname(__file__),"ordner")
filename = os.path.join(os.path.dirname(__file__),"ordner","unterordner","datei.txt")
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    if os.path.isdir(file_path):
        print(file_path + "ist ein Ordner")
    else:
        print(file_path + " ist eine Datei")

with open (filename, "r") as file:
    for line in file:
        print(line)