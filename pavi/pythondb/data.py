from python import col




q=input("enter the question:")
ans=input("enter the ans: ")

option1=input("enter your option:")
option2=input("enter your option:")
option3=input("enter your option:")
options=[option1, option2,option3,ans]



data={"question":q,"options":options,"answer":ans}
col.insert_one(data)
