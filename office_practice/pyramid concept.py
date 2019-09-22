def full_pyramid(rows):
    print('full pyramid')
    for i in range(rows):
        print(' '*(rows-i-1) + '*'*(2*i+1))
full_pyramid(5)

def half_pyramid(rows):
    print('half pyramid')
    for i in reversed(range(rows)):
        print('*'*(i+1))
half_pyramid(5)