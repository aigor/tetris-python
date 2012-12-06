import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import urlparse
import os
import time
from glass import Glass
from figure import *


def make_decision(params):       
    x = int(params['x'][0])
    y = int(params['y'][0])
    figure_name = params['figure'][0]
    glass_str = params['glass'][0]    
    print "x:", x, " y:", y, "figure:", figure_name    

    figure = Figures[figure_name]
    glass = Glass(glass_str)

    glassWithFigure = glass.addFigure(figure, x, y)
    glassWithFigure.printGlass()    

    print "Current surface range:", glass.getSurfaceRange()   
    print "Current overal range:", glass.getGlassRange()   
    solution = glass.findSolution(figure, x, y)   
    print "Solution surface range:", solution[2].getSurfaceRange()
    print "Solution complete lines:", solution[2].getNumberOfCompleteLines()
    print "Solution number of holes:", solution[2].getNumberOfHoles()
    print "Solution max height:", solution[2].getMaxHeight()
    print "Solution overal range:", solution[2].getGlassRange()   
    
    figure.printFigure()    
    
    solutionPhrase = ("left=" + str(x - solution[0]) if (solution[0] <= x) else ("right=" + str(solution[0] - x)))
    solutionPhrase += ", rotate=" + str(solution[1])
    solutionPhrase += ", drop"    
    print "Solution phrase:", solutionPhrase     
    return solutionPhrase

def handle_request(path):    
    return make_decision(urlparse.parse_qs(path[2:]))    

class TetrisService(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        baseTime = time.time() 
        print("======== Request handling started ===============================================")
        if self.path.startswith("/"):            
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            self.wfile.write(handle_request(self.path))
        else:
            self.send_error(404, notfound)
        print "======== Request handling finished [time: ", time.time() - baseTime,"] =================="

    def log_request(self, code=None, size=None):
        pass

    def log_message(self, format, *args):
        pass



