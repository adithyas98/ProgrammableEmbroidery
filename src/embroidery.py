#!/usr/bin/env python3

from UIClass import UserInput
from jef import Jef as j

from collections import defaultdict

class Embroidery:
    '''
    Will implement the embroidery design
    '''
    def __init__(self):
        qdict = defaultdict(dict)
        
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

    def createStitches(self):
        '''
        This method will create all of the stitch patterns and output
        the stitches
        Output:
            - Stitch pattern
        '''

        




        


        



