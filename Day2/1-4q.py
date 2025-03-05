def print_hollow_rectangle(height, width):
    for i in range(height):
        if i == 0 or i == height - 1:
            print('*' * width)  
        else:
            print('*' + ' ' * (width - 2) + '*')  

height = 5
width = 6
print_hollow_rectangle(height, width)