"""
2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


line = [2, 2, 2, 2, 2]

row = []

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    row = list(line)
    
#move zero
    for i in range(2):
        for i in range(len(row)-1): 
            if row[i] == 0:
                row[i] = row[i+1]
                row[i+1] = 0

#add
    for i in range(len(row)-1):
        if row[i] == row[i+1]:
            row[i] = row[i] + row[i+1]
            row[i+1] = 0

    
    for i in range(2):
        for i in range(len(row)-1): 
            if row[i] == 0:
                row[i] = row[i+1]
                row[i+1] = 0

    

    return row
            
#print (merge(line))
    

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for col in range(self.grid_width)]
                   for row in range(self.grid_height)]
        
        self.new_tile()
    

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return "Hello, please to meet you"
    

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        
        line1 = []
        line2 = []
        line3 = []
        line4 = [] 
        line_all = []
        
        #up
        if direction == UP:
            r = 0
            for step in range(4):
                row1 = 0 + step * OFFSETS[direction][0]
                col1 = 0 + step * OFFSETS[direction][1]
                
                line1.append(self.grid[row1][col1])
            
                row2 = 0 + step * OFFSETS[direction][0]
                col2 = 1 + step * OFFSETS[direction][1]
            
                line2.append(self.grid[row2][col2])
            
                row3 = 0 + step * OFFSETS[direction][0]
                col3 = 2 + step * OFFSETS[direction][1]
            
                line3.append(self.grid[row3][col3])
            
                row4 = 0 + step * OFFSETS[direction][0]
                col4 = 3 + step * OFFSETS[direction][1]
                
                line4.append(self.grid[row4][col4])
                
        elif direction == DOWN:
            r = 1
            for step in range(4):
                row1 = 0 + (step+1) * OFFSETS[direction][0]
                col1 = 0 + (step+1) * OFFSETS[direction][1]
                
                line1.append(self.grid[row1][col1])
            
                row2 = 0 + (step+1) * OFFSETS[direction][0]
                col2 = 1 + (step+1) * OFFSETS[direction][1]
            
                line2.append(self.grid[row2][col2])
            
                row3 = 0 + (step+1)*OFFSETS[direction][0]
                col3 = 2 + (step+1)*OFFSETS[direction][1]
            
                line3.append(self.grid[row3][col3])
            
                row4 = 0 + (step+1)*OFFSETS[direction][0]
                col4 = 3 + (step+1)*OFFSETS[direction][1]
                
                line4.append(self.grid[row4][col4])
        
        elif direction == LEFT:
            r = 0
            for step in range(4):
                row1 = 0 + step * OFFSETS[direction][0]
                col1 = 0 + step * OFFSETS[direction][1]
                
                line1.append(self.grid[row1][col1])
            
                row2 = 1 + step * OFFSETS[direction][0]
                col2 = 0 + step * OFFSETS[direction][1]
            
                line2.append(self.grid[row2][col2])
            
                row3 = 2 + step * OFFSETS[direction][0]
                col3 = 0 + step * OFFSETS[direction][1]
            
                line3.append(self.grid[row3][col3])
            
                row4 = 3 + step * OFFSETS[direction][0]
                col4 = 0 + step * OFFSETS[direction][1]
                
                line4.append(self.grid[row4][col4])
            
        elif direction == RIGHT:
             r = 1 
             for step in range(4):
                row1 = 0 + (step+1) * OFFSETS[direction][0]
                col1 = 0 + (step+1) * OFFSETS[direction][1]
                
                line1.append(self.grid[row1][col1])
            
                row2 = 1 + (step+1) * OFFSETS[direction][0]
                col2 = 0 + (step+1) * OFFSETS[direction][1]
            
                line2.append(self.grid[row2][col2])
            
                row3 = 2 + (step+1) * OFFSETS[direction][0]
                col3 = 0 + (step+1) * OFFSETS[direction][1]
            
                line3.append(self.grid[row3][col3])
            
                row4 = 3 + (step+1) * OFFSETS[direction][0]
                col4 = 0 + (step+1) * OFFSETS[direction][1]
                
                line4.append(self.grid[row4][col4])
       
            
        line_all.append(line1)
        line_all.append(line2)
        line_all.append(line3)
        line_all.append(line4)
            

        for line in range(len(line_all)):
            self.grid[line] = line_all[line]  
        
        #call merge
    
        for time in range(4):
            self.grid[time] = merge(line_all[time])
            
        # merfe done
        if r == 1:
            for time in range(4):
                self.grid[time].reverse()
                
        elif r == 0:
            newlist = []
            i = 0
            while i < len(self.grid):
                j = 0
                colvec = []
                while j < len( self.grid):
                    colvec.append( self.grid[j][i])
                    j = j + 1
                newlist.append(colvec)
                i = i + 1
            self.grid = newlist    
            

        self.new_tile_play()          
        return self.grid
    
    def new_tile_play(self):
        row = random.randrange(4)
        col = random.randrange(4)
        
        if self.grid[row][col] == 0:
            random_num = random.random()
            tile_num1 = 0
            if random_num <0.9:
                tile_num = 2
            else:
                tile_num = 4
            self.grid[row][col] = tile_num
    


    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        global grid
        
        
        
        for new_tile in range(2):
            row = random.randrange(4)
            col = random.randrange(4)
        
            if self.grid[row][col] == 0:
                random_num = random.random()
                tile_num1 = 0
                if random_num <0.9:
                    tile_num = 2
                else:
                    tile_num = 4
                self.grid[row][col] = tile_num 

                
        

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self.grid[row][col] = value
        return self.grid[row][col]

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]


    
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
