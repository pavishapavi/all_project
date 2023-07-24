pay=0
small=120
medium=150
large=180
print("1.small\n2.medium\n3.large ")
size=int(input("choose the pizza size:"))
total=int(input(" how many pizza:"))
if(size==1):
    print(f" how much rupee {small} pizza")
    pay=small * total
elif(size==2):
    print(f" how much rupee {medium} pizza")
    pay=medium * total
elif(size==3):
    print(f" how much rupee {large} pizza")
    pay=large * total
#==========
tp=str(input("do you want topping yes or no:"))

if(tp=="yes"):
    pay +=(pay/100)*10
    print(pay)
 
    
ch=str(input("do you want chess yes or no:"))
if(ch=="yes"):
    pay +=(pay/100)*5
    print(pay)
  





#=================
print(f"you have to pay Rs.{pay}")



print(10**2/2*5+6-7)

    
