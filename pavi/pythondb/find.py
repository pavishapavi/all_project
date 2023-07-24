
from python import col


data=list(col.find({}))
##print (data)


for i in data:
    ques=i.get("question")
    option=i.get("options")
    ans=i.get("answer")
    print(ques)

    for j in option:
        print("    ",j)


        
    inp=input("enter the answer:")
    if(inp==ans):
        print("the answer is correct")
    else:
        print("the answer is wrong")
    print(ans)
    print('\n')
    



