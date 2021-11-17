f = open("C:/C/고인물이 다시 고이는 법 1-140.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()
