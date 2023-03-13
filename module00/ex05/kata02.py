kata = (2019, 9, 25, 23, 30)

if (len(kata) != 5):
    print("error")
    exit()
if (4 < len(str(kata[0])) < 1):
    print("error")
    exit()
for i in range(1, 4):
    if (2 < len(str(kata[i])) < 1):
        print("error")
        exit()
s = "{}/{:02d}/{:02d} {:02d}:{}".format(kata[0], kata[1], kata[2], kata[3], kata[4])
print(s)
