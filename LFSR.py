
# LFSR.py                                                
'''
Modeling a Linear Feedback Shift Register (LFSR)
'''

def spinLFSR(init='0001', taps=[4,3,1]):
    '''Given the initial state of an LFSR and its feedback taps, return the
    number of cycles until the initial state is repeated.

    >>> spinLFSR()
    15
    '''
    L = len(init)  # length of the shift register
    
    # convert string to [list of ints]
    SR0 = [int(init[i]) for i in range(L)]   # initial state [1, 1, 0, 1]
    SR = SR0[:]    # copy initial state
        
    # print SR, taps

    for clk in range(1, 2**L):      # {1, 2, ... 16}
        
        FB = 0
        for i in taps: FB ^= SR[i-1]  # compute the feedback bit
        
        SR = ([FB] + SR)[0:L]       # shift right
        print (SR)

        if SR == SR0:
            return clk

def findtaps(L=4):
    '''Find tap positions that generate a maximum period in an LFSR of length L.

    >>> findtaps()
    [3, 0] 15 *
    [3, 1] 6 
    [3, 2] 15 *
    '''
    # Look for solutions with only two taps. First tap must always be at L-1.
    
    for taps in [[L-1,n] for n in range(L-1)]:  # [[3,0], [3,1], [3,2]]
        init = L * '1'                          # '1111'
        period = spinLFSR(init, taps)
        if (period == 2**L-1): flag = "*"
        else: flag = ""
        print (taps, period, flag)                # [3,2] 15 *


### Define an LFSR object, more versatile that the simple functions above. Size
#   and taps of the LFSR should be instance variables.
        
class LFSR(object):
    '''
    Linear Feedback Shift Register
    '''
    def __init__(self, state='000000', size=6, taps=[1,2,3,5,6]):
        "Save initial state and design of the LFSR"

        if size == 0: size = len(state)           # default size 4
        assert size >= len(state)   # only first few bits are needed
        
        if taps == None: taps = [size-1, size-2]  # default taps [3,2]
        assert taps[0] == size - 1  # first tap is always on the last stage
    
        init = size * [0]           # set up initial state
        for i in range(len(state)):
            if   state[i] == '0': init[i] = 0
            elif state[i] == '1': init[i] = 1
            else: return "Bad initial state"           

        self.init  = init          # [1, 1, 0, 1]
        self.state = init
        self.taps  = taps          # [3, 2]
        self.size  = size          # 4
        self.clock = 0             # cummulative clock count

    def spin(self, N):
        "Advance the state by N clock cycles.  Stop if init is repeated."
        
        for n in range(N):
            self.clock += 1
            
            FB = 0
            for i in self.taps:         # compute the feedback bit
                FB ^= self.state[i]

            self.state = ([FB] + self.state)[0:self.size]  # shift right
            
            if (self.state == self.init):
                return "Initial state repeats at %s" % self.clock
                
        return self.state

import math



def main():
    print("Hello World!")
    spinLFSR()

if __name__ == "__main__":
    main()
    