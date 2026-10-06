import math
import heapq
import json
import sys
with open("position.json", "r") as info:
    data = json.load(info)


class Car:
    def __init__(self):
        self.parent_i = 0
        self.parent_j = 0
        self.f = float('inf')
        self.g = float('inf')
        self.h = 0


ROW = 10
COLUMN = 10

def is_destination(row, col, dest_row, dest_col):
    return int(row) == int(dest_row) and int(col) == int(dest_col)

def is_valid(row, col):
    return (int(row) >= 0) and (int(row) < ROW) and (int(col) >=0) and (int(col) < COLUMN)

def calculate_h (row, col, dest_row, dest_col):
    return abs(int(dest_row) - int(row)) + abs(int(dest_col) - int(col))

def trace_path (cell_details, dest_row, dest_col):
    row = int(dest_row)
    col = int(dest_col)
    path = []
    print("The Path is ")

    while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
        path.append((row,col))
        temp_row = cell_details[row][col].parent_i
        temp_col = cell_details[row][col].parent_j
        row = temp_row
        col = temp_col
    
    path.append((row,col))
    path.reverse()

    data["x_position"] = sys.argv[2]
    data["y_position"] = sys.argv[3]
    with open("position.json", "w") as info:
        json.dump(data, info)

    for i in path:
        print("->", i, end = " ")
    print()

def calculate_path(row, col, dest_row, dest_col):
    if not is_valid(row, col) or not is_valid(dest_row, dest_col):
        print("Source or destination is wrong")
        return 
    
    if is_destination(row, col, dest_row, dest_col):
        print("You are already at the destination")
        return
    
    dest_flag = False

    closed_list = [[False for _ in range(COLUMN)] for _ in range(ROW)]
    cell_details = [[Car() for _ in range(COLUMN)] for _ in range(ROW)]

    i = int(row)
    j = int(col)
    cell_details[i][j].f = 0
    cell_details[i][j].g = 0
    cell_details[i][j].h = 0
    cell_details[i][j].parent_i = i
    cell_details[i][j].parent_j = j


    open_list = []
    heapq.heappush(open_list, (0.0, i, j))



    while(len(open_list) > 0):
        p = heapq.heappop(open_list)

        i = p[1]
        j = p[2]
        closed_list[i][j] = True

        direction = [(1,0), (0,1), (-1,0), (0,-1)]

        for dir in direction:
            new_i = i + dir[0]
            new_j = j + dir[1]

            if is_valid(new_i, new_j) and not closed_list[new_i][new_j]:
                if is_destination(new_i, new_j, dest_row, dest_col):
                    cell_details[new_i][new_j].parent_i = i
                    cell_details[new_i][new_j].parent_j = j
                    print("The destination is found")
                    trace_path(cell_details, dest_row, dest_col)
                    dest_flag = True
                    return
                else:
                    g_new = cell_details[i][j].g + 1.0
                    h_new = calculate_h(new_i, new_j, dest_row, dest_col)
                    f_new = g_new + h_new

                    if(cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new):
                        heapq.heappush(open_list, (f_new, new_i, new_j))

                        cell_details[new_i][new_j].f = f_new
                        cell_details[new_i][new_j].g = g_new
                        cell_details[new_i][new_j].h = h_new
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j

    if not dest_flag:
        print("Failed to find the destination cell")
                      



    





    


