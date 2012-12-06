from figure import Figure

class Glass:    
    rows_num = 20
    cols_num = 10        
    rows = range(0, rows_num)
    cols = range(0, cols_num)    
    glass_matrix = [[0]*cols_num]*rows_num
    complete_row = [1]*cols_num
    empty_row = [0]*cols_num
    
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

    def getNumberOfCompleteLines(self):        
        return sum([1 if self.glass_matrix[i] == self.complete_row else 0 for i in self.rows])

    def getNumberOfHoles(self):
        numbOfHoles = 0
        for i in self.cols:
            elementPresent = False
            for j in reversed(self.rows):
                if self.glass_matrix[j][i] == 1: #and self.glass_matrix[j] != self.complete_row:
                    elementPresent = True
                if (self.glass_matrix[j][i] == 0) and (elementPresent == True):
                    numbOfHoles += 1
        return numbOfHoles

    def getMaxHeight(self):
        return max( [ max ([j+1 if self.glass_matrix[j][i] == 1 else 0 for j in self.rows ]) for i in self.cols ] )

    def getGlassRange(self):
        return self.getSurfaceRange()*12 + self.getNumberOfHoles()*20 + self.getMaxHeight()*2 - self.getNumberOfCompleteLines()*20


    def numbOfElems(self):        
        return sum ( [ sum ( [self.glass_matrix[i][j] for j in self.cols ] ) for i in self.rows ] )

    def findSolution(self, figure, x, y):        
        bestConfiguration = self.dropFigure(figure, x, y)
        bestGlassPoint = bestConfiguration.getGlassRange()        
        bestX = x
        bestR = 0
        
        for curr_x in self.cols:
            for curr_r in range(0,4):
                testFigure = figure.rotate(curr_r)
                solution = self.dropFigure(testFigure, curr_x, y)
                print "solution range:", solution.getGlassRange()
                if solution.numbOfElems() == self.numbOfElems() + figure.numbOfElems():                                
                    if solution.getGlassRange() < bestGlassPoint:                    
                        bestGlassPoint = solution.getGlassRange()
                        bestConfiguration = solution
                        bestX = curr_x   
                        bestR = curr_r                         
        return bestX, bestR, bestConfiguration

    def dropFigure(self, figure, x, y):
        curr_y = 0               
        while True:                        
            curr_y+=1
            currGlass = self.addFigure(figure, x, curr_y)                                   
            if currGlass.numbOfElems() == self.numbOfElems() + figure.numbOfElems() or curr_y >= self.rows_num:
                return currGlass
        

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
