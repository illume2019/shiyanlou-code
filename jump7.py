j = 0
while a < 0:
    j = j + 1
    if j % 7 == 0:
        continue
    if j % 10 == 7:
        continue
    if j // 10 ==7:
        continue
    print(j)
