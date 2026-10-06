import json
import sys
import pathfinding

with open("position.json", "r") as info:
    data = json.load(info)


if sys.argv[1] == "move":
    pathfinding.calculate_path(data["x_position"], data["y_position"], sys.argv[2], sys.argv[3])

if sys.argv[1] == "status":
    print(data)

if sys.argv[1] == "end":
    data.update({"x_position": "0", "y_position": "0", "Ob_x_position": "0", "Ob_y_position": "0"})
    with open("position.json", "w") as info:
        json.dump(data, info)
    print(data)





