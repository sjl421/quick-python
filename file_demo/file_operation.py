fo = open("csdn_100.csv", "r")
print("filename: ", fo.name)

results = fo.readlines()
for i in range(5):
    tmp = results[i].split('')
    print(tmp[0])
    print(tmp[1])
    print(tmp[2])


# line = fo.read(1000)
# print("stirng: %s" % (line))
# fo.close()

