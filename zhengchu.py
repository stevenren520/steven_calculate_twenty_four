re_list = []
for i in range(9):
    for j in range(9):
        num = '8' + str(i) + '5' + str(j)
        if int(num) % 36 == 0:
            re_list.append(num)

print('re_list = ', re_list)