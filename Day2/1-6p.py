def print_right_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)  


height = int(input())
print_right_triangle(height)