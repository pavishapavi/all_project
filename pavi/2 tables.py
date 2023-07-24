number=int(input("enter the tables:"))
for i in range(1,11):
    product=number*i
    print(number,"x",i,"=",product)

##
print("even number")

for i in range(1,101):
     if(i%2==0):
         print(i)
    
print("odd number")
for i in range(1,101):
    if(i%2==1):
        print(i)
    

for i in range (100,0,-1):
    print(i)

for num in range (1,26):
    print(num,end=" ")
    if(num % 5==0):
        print()
  

        
##for num in range (1,10):
##    print(num,end=" ")
##    if(num % 3==0):
##        print()
