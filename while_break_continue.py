i = 1 
while i <= 10:
    if i == 5:
        print("stopping loop")
        break
    print(i)
    i += 1


i = 1

while i <= 10:
    if i > 5 and i < 8:
        i += 1
        continue
    print(i)
    i += 1
