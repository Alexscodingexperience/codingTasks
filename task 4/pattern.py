height = 5

for i in range(1, 2 * height):
    if i <= height:
        print('*' * i)
    else:
        print('*' * (2 * height -i))