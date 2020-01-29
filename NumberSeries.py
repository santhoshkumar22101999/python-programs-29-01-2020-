s=int(raw_input("enter your choice.... \n1.odd \n2.even \n3.divisible by 3 \n4.divisible by 4"))
if(s==1):
    for i in range(0,10):
        if(i%2 !=0):
            print(i)
elif(s==2):
    for i in range(0,10):
        if(i%2==0):
            print(i)
elif(s==3):
    for i in range(0,10):
        if(i%3==0):
            print (i)
elif(s==4):
    for i in range(0,10):
        if(i%4==0):
            print(i)
else:
    print("enter valid number")
        

'''
SAMPLE INPUT:
enter your choice.... 
1.odd 
2.even 
3.divisible by 3 
4.divisible by 4
1
SAMPLE OUTPUT:
1
3
5
7
9
----------
enter your choice.... 
1.odd 
2.even 
3.divisible by 3 
4.divisible by 4
2
SAMPLE OUTPUT:
0
2
4
6
8
------------
enter your choice.... 
1.odd 
2.even 
3.divisible by 3 
4.divisible by 4
3
SAMPLE OUTPUT:
0
3
6
9
-----------------
enter your choice.... 
1.odd 
2.even 
3.divisible by 3 
4.divisible by 4
4
SAMPLE OUTPUT:
0
4
8
'''

