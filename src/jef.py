#!/usr/bin/env python3

import math

class Jef:
    '''
    This class will implement basic shapes that can be used to build 
    the final design
    '''
    def __init__(self,stitch=10):
        self.mode = None #This will hold the current mode
        self.stitch = stitch #The length of the steps we make


    def changeState(self,state):
        '''
        This method will change the state of the current sow
        Input:
            - state: the state to change to:
                    - 1: Change to next thread in list
                    - 2: Move 
                    - 16: Last Stitch
        Output:
            - the code to change the state
        '''
        assert state in [1,2,16], "State seems to be incorrect make sure it is in 1,2,or 16"
        #change the state
        self.mode = state
        #We can now return the state
        return [128,state]
    def square(self,dim):
        '''
        Will create a square at the specified position. The position will be at
        the center of the square
        Inputs:
            - dim
        Output:
            - Code to make a square
        '''
        squareStitches = []
        #convert dim into an int
        dim = int(dim)
        for i in range(0,dim): 
            squareStitches += [ self.stitch, 0,]
        for i in range(0,dim): 
            squareStitches += [ 0, self.stitch,]
        for i in range(0,dim): 
            squareStitches += [256-self.stitch, 0,]
        for i in range(0,dim): 
            squareStitches += [0, 256-self.stitch,]
        return squareStitches

    def sqFractal(self,x,y,dim,level):
        '''
        A function that will create the fractal shape. 
        Inputs:
            - x,y: How much to move the bottom left corner of the square
                    before constructing it
            - dim: The dimension of the square
            - level: the level of depth/complexity (int)
        Outputs:
            - the code to create the fractal pattern
        '''
        fractal = []#holds the fractal
        for i in range(level):
            #make the square
            #move the bottom left to the right position
            fractal += self.move(x,y)
            #draw the square
            fractal += self.square(dim)
            #Now we want to dynamically update the parameters
            x = int(dim/2)
            y = int(dim/2)
            dim = int(dim/2)
        return fractal
    def triangle(self,dim): 
        '''
        This method will output the stitches to make an equilateral triangle
        Input:
            -dim: the dimension of the triangle
        Output:
            - the codes to make a triangle
        '''
        triangleStitches = []
        for t in range(0,dim):
            triangleStitches += [ int(self.stitch*math.cos(math.pi/3)), int(self.stitch*math.sin(math.pi/3)),]
        for t in range(0,dim):
            triangleStitches += [ int(self.stitch*math.cos(math.pi/3)), 256-int(self.stitch*math.sin(math.pi/3)),]
        for t in range(0,dim): 
            triangleStitches += [256-self.stitch, 0,]
        return triangleStitches

    def circle(self,radius):
        '''
        Creates a circle with the specified radius
        Input:
            - radius: the radius of the circle to create
        output:
            - the code to sow the circle
        '''
        circleStitches = []
        for t in range(0, int(2*math.pi*100), self.stitch): 
            x = int(math.cos(t/100)*radius)
            y = int(math.sin(t/100)*radius)
            if x < 0:
                x = 256 + x 
            if y < 0:
                y = 256 + y 
            circleStitches += [x, y]
        return circleStitches

    def zigZag(self,stitches): 
        '''
        This method will take any list of stitches and conver the individual 
        stitches into a zig-zag pattern
        Input:
            - stitches: a list of stitches to import
        Ouptut:
            - zig zag
        '''
        zigStitches = []
        for i in range(0,len(stitches)-1,2): 
            in1x = stitches[i+1]
            in1y = stitches[i]
            in2x = stitches[i]-stitches[i+1] 
            in2y = stitches[i+1]-stitches[i]
            if in2x < 0:
                in2x = 256 + in2x
            if in2y < 0:
                in2y = 256 + in2y
            zigStitches += [in1x, in1y, in2x, in2y] 
        return zigStitches
    def move(self,x,y):
        '''
        Will move the needs to the specified location
        Inputs:
            - x: how much to move the stitch in the x direction
            - y: how much to move the stitch in the y direction
        Ouput:
            - code to move the stitch
        '''
        if x < 0:
            #Then we need to subtract from 256
            x = 256 + x
        if y < 0:
            y = 256 + y
        return [0,0,x,y,]

    def getHeader(self,num_stitches):
        '''
        This method will return a list containing the header for the jef file Inputs:
            - 
        Output:
            - list containing header for the Jef file
        '''
        #This code was adopted from the example code given to us by the TAs
        jefBytes = [    128, 0, 0, 0,   # The byte offset of the first stitch
                        10, 0, 0, 0,   # unknown command
                        ord("2"), ord("0"), ord("2"), ord("1"), #YYYY
                        ord("0"), ord("2"), ord("2"), ord("4"), #MMDD
                        ord("1"), ord("5"), ord("2"), ord("1"), #HHMM
                        ord("0"), ord("0"), 99, 0, #SS00
                          2, 0, 0, 0,   # Thread count nr. (nr of thread changes)
                        (num_stitches) & 0xff, (num_stitches) >> 8 & 0xff, 0, 0, # Number of stitches
                          3, 0, 0, 0, # Sewing machine Hoop
                        # Extent 1
                         50, 0, 0, 0,#Left boundary dist from center (in 0.1mm)
                         50, 0, 0, 0,#Top boundary dist from center (in 0.1mm)
                         50, 0, 0, 0,#Right boundary dist from center (in 0.1mm)
                         50, 0, 0, 0,#Bottom boundary dist from center (in 0.1mm)
                        # Extent 2
                         50, 0, 0, 0,#Left boundary dist from center (in 0.1mm)
                         50, 0, 0, 0,#Top boundary dist from center (in 0.1mm)
                         50, 0, 0, 0,#Right boundary dist from center (in 0.1mm)
                         50, 0, 0, 0,#Bottom boundary dist from center (in 0.1mm)
                        # Extent 3
                         50, 0, 0, 0,#Left boundary dist from center (in 0.1mm)
                         50, 0, 0, 0,#Top boundary dist from center (in 0.1mm)
                         50, 0, 0, 0,#Right boundary dist from center (in 0.1mm)
                         50, 0, 0, 0,#Bottom boundary dist from center (in 0.1mm)
                        # Extent 4
                         50, 0, 0, 0,#Left boundary dist from center (in 0.1mm)
                         50, 0, 0, 0,#Top boundary dist from center (in 0.1mm)
                         50, 0, 0, 0,#Right boundary dist from center (in 0.1mm)
                         50, 0, 0, 0,#Bottom boundary dist from center (in 0.1mm)
                        # Extent 5
                         50, 0, 0, 0,#Left boundary dist from center (in 0.1mm)
                         50, 0, 0, 0,#Top boundary dist from center (in 0.1mm)
                         50, 0, 0, 0,#Right boundary dist from center (in 0.1mm)
                         50, 0, 0, 0,#Bottom boundary dist from center (in 0.1mm)
                         5, 0, 0, 0,#Thread Color (white)
                         40, 0, 0, 0, # Thread Color (Pink)
                         14, 0, 0, 0, # Thread Color (Violet)
                    ]
        return jefBytes

if __name__ == '__main__':
    j = Jef()
    t = j.changeState(1)
    sow = j.changeState(2)
    circle = j.zigZag(j.circle(4))
    square = j.square(8)
    head = j.getHeader(len(circle)//2)
    lastStitch = j.changeState(16)
    fractal = j.sqFractal(40,40,16,8)
    data = bytes(head) + bytes(sow)  
    data += bytes(fractal)
    data += bytes(t) + bytes([0,0,]) +  bytes(lastStitch)
    with open('circle.jef','wb') as f:
        f.write(data)

