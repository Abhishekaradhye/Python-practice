#A painter wants kniw the amount of paint to paint needed to paint only interior of walls and 
#  interor side of door in a room. Choosen paint covers 100 sq.ft of area per liter. 
#  The room has two windows. Test the code with following data :
#     Room is 12 ft long, 10 ft wide, 8 ft tall
#     Two windows are 5x3 & 6x2 ft respectively
#     One liter paint covers 100 sq.ft of area.
#     Tyoe a code to give required quantity of paint.     
l=float(input('Enter the length of the room='))
w=float(input('Enter the width of the room='))
h=float(input('Enter the height of the room='))
wl1=float(input('Enter the length of the window1='))
wh1=float(input('Enter the height of the window1='))
wl2=float(input('Enter the length of the window2='))
wh2=float(input('Enter the height of the window2='))

def room_area():
    long_wall = l*h
    wide_wall = w*h
    total_area = long_wall + wide_wall
    return total_area

def reduced_area():
    window1_area = wl1*wh1
    window2_area = wl2*wh2
    window_area = window1_area + window2_area
    return window_area

room_area()
reduced_area()

paint_required = (room_area() + reduced_area())/100

print(f'The amount of paint required to paint the interior of given room is{paint_required} liters:')