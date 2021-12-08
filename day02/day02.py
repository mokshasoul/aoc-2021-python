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

depth_coords = (0,0)
input_validation = re.compile(r'(forward|down|up) \d+')
for line in (Path(__file__).parent / 'input.txt').read_text().splitlines():
# while True:
    # print("Please enter where submarine should move to:") 
    # print("Examples: <direction> <value>")
    # print("To exit please type exit")
    # user_input = str(input("Please enter now:"))
    user_input = line
    if input_validation.fullmatch(user_input):
        direction, value = user_input.split(" ")
        depth_coords = movement(depth_coords, direction=direction, value=int(value))
    elif user_input.lower() == "exit":
        break
    else:
        print("WRONG INPUT PLEASE TRY AGAIN")
        continue

x,y = depth_coords
print(f"FINAL DEPTH: {x*y}")