import random

a=int(input("enter a value within 10"))
b= random.randrange(0,10)
if(a==b):
    print("winner",a,b)
else:
    print("better luck next time")
    
'''
SAMPLE OUTPUT:
enter a value 2
better luck next time
----------------------------------
enter a value 1
('winner', 1, 1)
   
 '''
