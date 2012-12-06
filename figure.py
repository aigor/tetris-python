

class Figure:
    rows_num = 5    
    rows = range(0, rows_num)
    x = 0
    y = 0
    repr = [[0]*rows_num]*rows_num

    def __init__(self, x, y, in_repr):
        self.x = x
        self.y = y
        self.repr = [[ 1 if in_repr[i][j] == '*' else 0 for j in self.rows] for i in self.rows]
        self.repr.reverse()

    def printFigure(self):
        print ''.join( ''.join(['*' if self.repr[i][j] == 1 else ' ' for j in self.rows]) + "\n" for i in reversed(self.rows))

    def numbOfElems(self):        
        return sum ( [ sum ( [self.repr[i][j] for j in self.rows ] ) for i in self.rows ] )

    def clone(self):
        emptyFigure = Figure(2,2, ["     ","     ","     ","     ","     "])
        for i in self.rows:
            for j in self.rows:
                emptyFigure.repr[i][j] = self.repr[i][j]
        return emptyFigure

    def rotateOnce(self):
        res = self.clone()
        for i in self.rows:
            for j in self.rows:
                res.repr[i][j] = self.repr[j][self.rows_num - 1 - i]
        return res

    def rotate(self, times):
        res = self.clone()
        for i in range(0, times):
            res = res.rotateOnce()
        return res

I = Figure(2, 2, ["     ",
                  "  *  ",
                  "  *  ",
                  "  *  ",
                  "  *  "])

O = Figure(2, 2, ["     ",
                  "     ",
                  "  ** ",
                  "  ** ",
                  "     "])

L = Figure(2, 2, ["     ",
                  "  *  ",
                  "  *  ",
                  "  ** ",
                  "     "])

J = Figure(2, 2, ["     ",
                  "  *  ",
                  "  *  ",
                  " **  ",
                  "     "])

S = Figure(2, 2, ["     ",
                  "  ** ",
                  " **  ",
                  "     ",
                  "     "])

Z = Figure(2, 2, ["     ",
                  " **  ",
                  "  ** ",
                  "     ",
                  "     "])

T = Figure(2, 2, ["     ",
                  "  *  ",
                  " *** ",
                  "     ",
                  "     "])

Figures = { 'I': I, 
            'O': O,
            'L': L,
            'J': J,
            'S': S,
            'Z': Z,
            'T': T }


