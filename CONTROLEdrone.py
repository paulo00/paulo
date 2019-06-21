import numpy as np 
import cv2
import urllib
import math

x = [0,30,50,60,70,80]
y = [0,40,40,50,60,70]
xa = 1
xb = 1
ya = 1
yb = 40
n = 0
d= 0
a=0
d1=0
i=0
d2=0
d3=0
d4=0
d5=0
d8=0
d7=0
agulodrone=0
angulo=0
an = 0

for n in range(6):

      if (n == 0):
           
           d = (x[1]-x[0])**2+(y[1]-y[0])**2
           d1=math.sqrt(d)
           a = (y[1]-y[0])/d1
                   
      if (a == 1):
       
           print "avancar:", d1  
      
      else:
          
           print "rotaciona:", a
           print " avanca:", d1  


      if (n % 2 == 0 and n < 5):

           d2 = (x[n+1]-x[n])**2+(y[n+1]-y[n])**2
           d3=math.sqrt(d2)
   
              

      if ( n % 3 == 0 and n < 5 ):
         
           d4 = (x[n+1]-x[n])**2+(y[n+1]-y[n])**2
           d5 = math.sqrt(d4)

           d7 = (x[n]-x[n-3])**2+(y[n]-y[n-3])**2
           d8 = math.sqrt(d7)
      
           angulo = (((d2)**2 + (d3)**2 - (d8)**2)/(2*d2*d3))
           an = math. sinh(angulo)
           agulodrone = an - 180

           print "avancar", d5
           print "angulo", angulodrone
