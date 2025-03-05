def print_diamond(height):
   
    for i in range(1, height + 1, 2):  
        sp = ' ' * ((height - i) // 2)  
        st = '*' * i  
        print(sp + st)


    for i in range(height - 2, 0, -2):  
        sp = ' ' * ((height - i) // 2)  
        st = '*' * i  
        print(sp+ st)
height = 5 
print_diamond(height)