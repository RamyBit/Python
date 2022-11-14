import os
filename = os.path.join(os.path.dirname(__file__),"umlaute.txt")
with open(filename,"r", encoding= "UTF-8") as file:
    for line in file:
        print(line)
filename_out = os.path.join(os.path.dirname(__file__),"umlaute_out.txt")
with open(filename_out,"w", encoding="UTF-8") as file:
    file.write("Müller")