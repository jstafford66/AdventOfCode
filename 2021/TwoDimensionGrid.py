
class TwoDGrid:

    def __init__(self, default_value=0):
        #Dictionary to hold grid, x,y coord is key
        self.grid = {}
        self.default = default_value
    
    def SetPointVal(self, point, value):
        self.grid[point] = {'value':value, 'visited':False, 'distance':-1}
    
    def GetPoint(self, point):
        return self._getPoint(self.grid, point)
    
    def DeletePoint(self, point):
        self.grid.pop(point, None)
    
    def PeekPoint(self, point):
        return self._peekPoint(self.grid, point)

    def SnapShot(self):
        self.snap_shot = self.grid.copy()

    def GetSnapShotPoint(self, point):
        return self._getPoint(self.snap_shot, point)
    
    def PeekSnapShotPoint(self, point):
        return self._peekPoint(self.snap_shot, point)

    def getXBounds(self):
        x_vals = [p[0] for p in self.grid.keys()]
        return min(x_vals), max(x_vals)
    
    def getYBounds(self):
        y_vals = [p[1] for p in self.grid.keys()]
        return min(y_vals), max(y_vals)

    def getZBounds(self):
        z_vals = [p[2] for p in self.grid.keys()]
        return min(z_vals), max(z_vals)

    def getWBounds(self):
        w_vals = [p[3] for p in self.grid.keys()]
        return min(w_vals), max(w_vals)

    def countWithValue(self, value):
        count = 0
        for key, data in self.grid.items():
            if data['value'] == value:
                count += 1
        
        return count
    
    def getPointsWithValue(self, value):
        points = []
        for key, data in self.grid.items():
            if data['value'] == value:
                points.append(key)
        
        return points
    
    def getPointsGreaterThan(self, value):
        points = []
        for key, data in self.grid.items():
            if data['value'] > value:
                points.append(key)
        
        return points

    def rotate90Clockwise(self):
        x_min, x_max = self.getXBounds()
        y_min, y_max = self.getYBounds()

        for i in range(x_max // 2):
            for j in range(i, x_max - i - 1):
                p = (i, j)
                hold = self.grid[p]
                self.grid[p]= self.grid[(x_max - 1 - j, i)]
                self.grid[(x_max-1-j, i)] = self.grid(x_max-1-i,x_max-1-j)
                self.grid[(x_max-1-i,x_max-1-j)] = self.grid(j,x_max-1-i)
                self.grid[(j,x_max-1-i)] = hold
    
    def _getPoint(self, grid, point):
        value = self.default

        if point in grid:
            value = grid[point]['value']
        else:
            grid[point]= {'value':self.default, 'visited':False, 'distance':-1}
        
        return value
    
    def _peekPoint(self, grid, point):
        value = self.default
        if point in grid:
            value = grid[point]['value']
        return value

    def ShortestPath(point1, point2):
        
        return None
    
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
                txt += self.GetPoint(point) if point in self.grid else str(self.default)
            
            print (txt)
    
    def print2D(self, z=0):
        xmin, xmax = self.getXBounds()
        ymin, ymax = self.getYBounds()

        y = ymin
        while y <= ymax:
            txt = ''
            x = xmin
            while x <= xmax:
                txt += str(self.GetPoint((x,y,z)))
                x+=1
            print(txt)
            y+=1
    
    def print3D(self):
        z_min, z_max = self.getZBounds()

        z = z_min
        while z <= z_max:
            print('Z =', z)
            self.print2D(z)    
            z+=1       