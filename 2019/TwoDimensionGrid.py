import networkx as nx

class TwoDGrid:

    def __init__(self, default_value=0):
        #Dictionary to hold grid, x,y coord is key
        self.grid = {}
        self.default = default_value
    
    def SetPointVal(self, point, value):
        self.grid[point] = value
    
    def GetPoint(self, point):
        value = self.default

        if point in self.grid:
            value = self.grid[point]
        else:
            self.grid[point] = self.default
        
        return value
    
    def print(self):

        xvals = [p[0] for p in self.grid.keys()]
        yvals = [p[1] for p in self.grid.keys()]

        xmin = min(xvals)
        ymin = min(yvals)

        xmax = max(xvals)
        ymax = max(yvals)

        xoffset = 0
        if xmin < 0:
            xoffset = abs(xmin)
        
        yoffset = 0
        if ymin < 0:
            yoffset = abs(ymin)

        for row in range(ymax + yoffset + 1):
            txt = ''
            for col in range(xmax + xoffset + 1):
                point = (col - xoffset, row - yoffset)
                txt += self.grid[point] if point in self.grid else self.default
            
            print (txt)
