def print_star_pattern():
    for i in range(7): 
        
        for j in range(i):
            print("  ", end="")
        
        for k in range(7 - i):
            print("* ", end="")
        print() 

print_star_pattern()
