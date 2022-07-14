"""Defined a function that takes in a grid containing '#' and '-'
on each postion that contains a '-' determine if the adjacent positions
contain a '#' and count them. A new grid is created that is the same size as
the grid received and the number of adjacent hashes is stored in the same
position where its '-' position was. If the character in the position is a
'#' set the value in the new grid on the same position to '#'. """
def minesweeper(grid):
    num_rows = len(grid)
    num_col = len(grid[0])
    new_grid = [[0] * num_col for _ in range(num_rows)]
    hash_count = 0
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "#":
                new_grid[y][x] = "#"
            else:
                if y >= 0 and y < len(grid)-1:
                    if grid[y+1][x] == "#":
                        hash_count += 1
                if y > 0 and y <= len(grid)-1:
                    if grid[y-1][x] == "#":
                        hash_count += 1
                        
                if x >= 0 and x < len(row)-1:
                        if row[x+1] == "#":
                            hash_count += 1
                if x > 0 and x <= len(row)-1:
                        if row[x-1] == "#":
                            hash_count += 1 
                            
                if y >= 0 and y < len(grid)-1 and x >= 0 and x < len(row)-1:
                    if grid[y+1][x+1] == "#":
                        hash_count += 1
                if y >= 0 and y < len(grid)-1 and x > 0 and x <= len(row)-1:
                    if grid[y+1][x-1] == "#":
                        hash_count += 1
                        
                if y > 0 and y <= len(grid)-1 and x >= 0 and x < len(row)-1:
                    if grid[y-1][x+1] == "#":
                        hash_count += 1
                if y > 0 and y <= len(grid)-1 and x > 0 and x <= len(row)-1:
                    if grid[y-1][x-1] == "#":
                        hash_count += 1
                
                new_grid[y][x] = str(hash_count) 
                hash_count = 0
    
    return new_grid

grid = [["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"]]

# Print the rows of the new grid    
for row in minesweeper(grid):
    print(row)
