def print_rectangle(height, width):
    for _ in range(height):
        print('*' * width)

ht = int(input())
wd = int(input())
print_rectangle(ht, wd)