name="python"
age=20
gender="female"

if(age<18 and age>5):
    print(f" hi {name} your the student so will not get job")
elif(age>=18 and gender=="female"):
    print(f" hi {name} so will get female job")
elif(age>=18 and gender=="male"):
    print(f" hi {name} so you will get male job")
else:
    print("not get a job")
