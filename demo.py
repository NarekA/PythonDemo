###################################################################
#   Python tutorial
#   demo.py
#   Narek Amirbekian April 2011
#
#   The puropse of this file is to teach you all the basic
#   math, physics, and plotting tools you will need in for Physics 142
#   
#   If you try to run this whole file, it probably won't run, 
#   but the individual snippets of code are very useful
###################################################################



###################################################################
#   How to turnin assignments
#       Zip up directory with all necessary files
#       Name the file in the following manner:
#           NarekAmirbekianAsg1
#       Put in directory:
#               ../public/homework
#
#
#   ASG 1, What to turnin:
#       README PDF
#           Explaination of what every file is
#           Analysis of your results
#           You may put your plots in the PDF if you wish
#           Concluding remarks
#       Any code
#           Include a simple header for all source files
#       Plot, Wavefunction over time
#       Single plot with <E>, <K>, and <V> over time
#       Animation of wavefunction
#       Anything else that is pertinent
###################################################################


#   Python is case, indent, and line sensatinve, no semicolans, no brackets
#   Python does not execute the last iteration of a loop


for i in range(0,10):   # i = 0,1,... ,9 not 10! 
    print i

###################################################################
#   Complex numbers
###################################################################

a = complex(3,4)

print a.real
print a.imag
print abs(a)
print complex(3,4)+5+6j

#   Notice the use of j
#   When a number is followed by j as in 5j, it is complex
#       However 5*j does not work

###################################################################
#   Vectors and Matrices:
###################################################################

#   In practice, people use (nested) lists as matrices when 
#   the math is simple and computation time is not important

matrix = [  [5,4,7,11],[3,3,8,17]  ]
row=0
while row<2:
    col=0
    while col<4:
        print matrix[row][col]
        col=col+1
    row=row+1

###################################################################
#   This is inefficent it is better to use the numpy matrices
#   The difference between a list and array/matrix is the way they are stored in memory
#   data type because it is parallelized and it has many useful methods (functions)
#       Subclass of Numpy arrays
#   This is how to use numpy Arrays:
###################################################################
import numpy

M = numpy.matrix('1 2; 3 4')
print M

#   Indexing/Accessing elements:

M[1,0]  # Single element
M[0]    # Row
M[:,0]  # Col

#   Initalization:
M_zeros = numpy.zeros( (9,9) )

M_ones = numpy.ones( (9,9) )

M_empty = numpy.empty( (9,9) )

#   Some useful matrix methods in Python:

# Get the determinant
numpy.linalg.det(M)

# Transpose
numpy.transpose(M)
# or:
M.T

# Inverse
M.I

#   Matrix Multiplication
M_empty * M_zeros

#   Solving linear equations
solve(A, Y)

###################################################################
#   Plotting
###################################################################

# here are some examples on how to plot

import pylab

t = numpy.arange(0.0, 1.0+0.01, 0.01)   # Create a list of t-values
s = numpy.cos(2*2*numpy.pi*t)           # Creats a list of s(t) values
pylab.plot(t, s)

pylab.xlabel('time (s)')
pylab.ylabel('voltage (mV)')
pylab.title('About as simple as it gets, folks')
pylab.grid(True)
pylab.savefig('simple_plot.jpeg')

pylab.show()

#   Histograms

x = pylab.randn(10000)      # Generates 10000 points from gaussian dist
pylab.hist(x, 100)
pylab.savefig('hist.jpeg')

###################################################################
#   Animation
###################################################################

#   Here is a simple code for animatinplots, however this does not save the output
from pylab import *                 # Alternative way to import libraries
#   import pylab as pl
import time

tstart = time.time()               # for profiling
x = arange(0,2*pi,0.01)            # x-array
line, = plot(x,sin(x))
for i in arange(1,200):
    line.set_ydata(sin(x+i/10.0))  # update the data
    draw()                         # redraw the canvas

#   What we need to do is save the figures as jpeg's using: 

x = arange(0,2*pi,0.01)            # x-array
line, = plot(x,sin(x))
for i in arange(100,300):          # note the range this is for the file name length
    line.set_ydata(sin(x+i/10.0))  # update the data

    # Notice these two new lines:
    FileName = 'plot' + str(i) + '.jpeg'     # Create a string-type variable
    draw()                         # redraw the canvas
    savefig( FileName )       #   Use that string var in savefig

#   If you are working on your own computer you may use the following tools
#   to encode the jpegs into mpegs http://code.google.com/p/pyffmpeg/ or
#   http://pymedia.org/

#   If you are unable to install that library, you can encode the mpegs using
#   bash (UNIX terminal) you can use imagemagick with the following:

#   convert plot*.jpeg wave.mpeg 
#   rm plot*.jpeg
