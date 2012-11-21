from figure import Figure

class Glass:    
    rows_num = 20
    cols_num = 10        
    rows = range(0, rows_num)
    cols = range(0, cols_num)    
    glass_matrix = [[0]*cols_num]*rows_num
    
    def __init__(self, str_glass):       
        self.glass_matrix = [[ 1 if str_glass[self.cols_num*i+j] == '*' else 0 for j in self.cols] for i in self.rows]    
                
    def printGlass(self):        
        print ''.join([ "|" 
                        + ''.join(['*' if self.glass_matrix[i][j] == 1 else ' ' for j in self.cols]) 
                        + "|\n" for i in reversed(self.rows)])

    def getSurface(self):
        surface = [ max([j+1 if self.glass_matrix[j][i] == 1 else 0 for j in self.rows ]) for i in self.cols] 
        surfDiff = [ surface[i]-surface[i-1] for i in range(1, self.cols_num)]
        return surfDiff

    def getSurfaceRange(self):        
        return sum([abs(i) for i in self.getSurface()])

    def numbOfElems(self):        
        return sum ( [ sum ( [self.glass_matrix[i][j] for j in self.cols ] ) for i in self.rows ] )

    def dropFigure(self, figure, x, y):
        prevGlass = self.addFigure(figure, x, y)
        currGlass = prevGlass
        curr_y = y
        while currGlass.numbOfElems() == self.numbOfElems() + figure.numbOfElems():            
            prevGlass = currGlass
            curr_y-=1
            currGlass = self.addFigure(figure, x, curr_y)
        return prevGlass            

    def addFigure(self, figure, x, y):                        
        figureFieldMatrix = [ [0 for j in self.cols] for i in self.rows]
        for i in figure.rows:
            for j in figure.rows:  
                f_x = x - figure.x + i 
                f_y = y - figure.y + j
                if f_x in self.cols and f_y in self.rows:                          
                    figureFieldMatrix[f_y][f_x] += figure.repr[j][i]

        resultMatrix = [[ figureFieldMatrix[i][j] or self.glass_matrix[i][j] for j in self.cols] for i in self.rows]
        str_repr = ''.join([ ''.join(['*' if resultMatrix[i][j] == 1 else ' ' for j in self.cols]) for i in self.rows])
        return Glass(str_repr)
