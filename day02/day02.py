import re
from pathlib import Path

def movement(coords, direction, value):
    x,y = coords
    if direction == 'forward':
        return (x+value, y)
    elif direction == 'down':
        return (x, y+value)
    elif direction == 'up':
        return (x, y-value)
    else:
        print("Wrong directional input")
        return (x,y)

def aim(coords, aim, direction, value):
    x,y = coords
    if direction == 'forward':
        return (x+value, y+aim*value), aim
    elif direction == 'down':
        return (x, y), aim+value
    elif direction == 'up':
        return (x, y), aim-value
    else:
        print("Wrong directional input")
        return (x,y), aim

depth_coords = (0,0)
aim_coords = (0,0)
aim_val = 0
input_validation = re.compile(r'(forward|down|up) \d+')
for line in (Path(__file__).parent / 'input.txt').read_text().splitlines():
# while True:
#     print("Please enter where submarine should move to:") 
#     print("Examples: <direction> <value>")
#     print("To exit please type exit")
#     user_input = str(input("Please enter now:"))
    user_input = line
    if input_validation.fullmatch(user_input):
        direction, value = user_input.split(" ")
        depth_coords = movement(depth_coords, direction=direction, value=int(value))
        aim_coords, aim_val = aim(aim_coords, aim=aim_val, direction=direction, value=int(value))
    elif user_input.lower() == "exit":
        break
    else:
        print("WRONG INPUT PLEASE TRY AGAIN")
        continue

x,y = depth_coords
x1,y1 = aim_coords
print(f"FINAL DEPTH PART ONE: {x*y}")
print(f"FINAL DEPTH PART TWO: {x1*y1}")