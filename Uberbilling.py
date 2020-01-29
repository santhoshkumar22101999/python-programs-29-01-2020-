def bill(destination):
    cost=destination*7
    print("cost of 1 km is RS 7")
    print "your bill is rs",cost

s=int(raw_input("enter your destination..\n POONAMALLEE to \n1.MADURAVOYAL \n2.CMBT \n3.ANNA NAGAR \n4.RETTERI\n"))
if(s==1):
    bill(8)
elif(s==2):
    bill(12)
elif(s==3):
    bill(16)
elif(s==4):
    bill(20)
else:
    print("enter valid destination")
    
'''
SAMPLE OUTPUT:
enter your destination..
 POONAMALLEE to 
1.MADURAVOYAL 
2.CMBT 
3.ANNA NAGAR 
4.RETTERI 
1
cost of 1 km is RS 7
your bill is rs 56
-------------------------------
enter your destination..
 POONAMALLEE to 
1.MADURAVOYAL 
2.CMBT 
3.ANNA NAGAR 
4.RETTERI 
2
cost of 1 km is RS 7
your bill is rs 84
-------------------------------
enter your destination..
 POONAMALLEE to 
1.MADURAVOYAL 
2.CMBT 
3.ANNA NAGAR 
4.RETTERI 
3
cost of 1 km is RS 7
your bill is rs 112
---------------------------------
enter your destination..
 POONAMALLEE to 
1.MADURAVOYAL 
2.CMBT 
3.ANNA NAGAR 
4.RETTERI 
4
cost of 1 km is RS 7
your bill is rs 140

'''
