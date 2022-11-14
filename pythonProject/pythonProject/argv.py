import sys
print(sys.argv)
print(len(sys.argv))
if len(sys.argv) >=2:
    fileName=sys.argv[1]
    with open(fileName,"r") as file:
        counter = 0
        for line in file:
            counter+=1

    print(counter)

else:
    print("File missing Error")