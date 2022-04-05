
class Point():

    def __init__(self, value, row, col, max_row=4, max_col=5):
        self.value = value
        self.col = col
        self.row = row
        self.max_row = max_row
        self.max_col = max_col

    def get_value(self):
        return self.value

    def get_neighbors_pos(self):
        neighbor_up = self.row - 1 if self.row > 0 else None
        neighbor_down = self.row + 1 if self.row < self.max_row else None
        neighbor_left = self.col - 1 if self.col > 0 else None
        neighbor_right = self.col + 1 if self.col < self.max_col else None
        return(
                (self.col, neighbor_up),
                (self.col, neighbor_down),
                (neighbor_left, self.row),
                (neighbor_right, self.row)
               )

    def get_position(self):
        return (self.col, self.row)
    
    def __str__(self):
        return f"({self.value}, {self.col}, {self.row})"
