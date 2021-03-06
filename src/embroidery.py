#!/usr/bin/env python3

from UIClass import UserInput
from jef import Jef

from collections import defaultdict

class Embroidery:
    '''
    Will implement the embroidery design
    '''
    def __init__(self):
        qdata = defaultdict(dict)
        
        intro = "Please answer the following questions:\n"
        qdata['level']['question'] = "What level of complexity do you want for the fractal?"
        qdata['level']['convert'] = int
        
        qdata['stitch']['question'] = "What stitch count do you want"
        qdata['stitch']['convert'] = int

        qdata['filename']['question'] = 'What would you like to call the Jef file? (do not include .jef)'
        qdata['filename']['convert'] = str

        ui = UserInput(qdata,intro)
        
        self.qdata = ui.askQuestions()#Ask the user questions

        #create the jef object
        self.jef = Jef(stitch=self.qdata['stitch']['data'])

        self.data = [] #will hold the data for the stitches

    def createStitches(self):
        '''
        This method will create all of the stitch patterns and output
        the stitches
        Output:
            - Stitch pattern
        '''
        
        #start out the sowing by changing the mode to sowing mode
        self.data += self.jef.changeState(2)
        

        #draw a circle
        self.data += self.jef.move(50,200)
        self.data += self.jef.circle(5)

        #currently at: -5mm,5mm
        #draw a circle
        self.data += self.jef.move(50,-25)
        self.data += self.jef.zigZag(self.jef.circle(5))

        #currently at: 0mm,2.5mm
        self.data += self.jef.move(50,15)
        self.data += self.jef.triangle(5)
        
        #currently at: 5mm,4mm

        #Chnage the thread
        self.data += self.jef.changeState(1)
        self.data += self.jef.changeState(2)#change back to sow
        #Now we can make our fractal
        level = self.qdata['level']['data']
        self.data += self.jef.sqFractal(-50,-20,8,level)

        #Currently at 0mm,0mm


        #change thread and draw a circle
        self.data += self.jef.changeState(1)
        self.data += self.jef.move(-50,-30)


        
        
        

        #Create last stich code
        self.data += self.jef.changeState(16)
        #now we can create the header
        header = self.jef.getHeader(len(self.data)//2)



        #Write the file
        stitch = bytes(header) + bytes(self.data)
        filename = self.qdata['filename']['data']
        with open('output/{}.jef'.format(filename),'wb') as f:
            f.write(stitch)


if __name__ == '__main__':
    emb = Embroidery()
    emb.createStitches()









        
        




        


        



