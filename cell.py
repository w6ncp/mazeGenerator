from graphics import Line, Point, Window

class Cell:
    def __init__(self, window:Window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
    
    def draw(self, x1, y1, x2, y2, color = "black"):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")
    
    def draw_move(self, to_cell, undo=False):
        if self._x1 is None or self._x2 is None or self._y1 is None or self._y2 is None:
            raise Exception("Possition of cell not set")
        if self._win is None:
            return
        color = "red"
        if undo:
            color = "gray"
        
        p1 = Point(self._x1 + ((self._x2 - self._x1) // 2),
                   self._y1 + ((self._y2 - self._y1) // 2))
        p2 = Point(to_cell._x1 + ((to_cell._x2 - to_cell._x1) // 2),
                   to_cell._y1 + ((to_cell._y2 - to_cell._y1) // 2))
        line = Line(p1, p2)
        self._win.draw_line(line, color)