from django.shortcuts import render,HttpResponse,redirect
from .models import uc

# Create your views here.





def home(req):
    data = list(uc.find())
    s = dict(req.session)
    print(s,'*************')
    if not s:
        return redirect('login')

        

    return render(req, 'home.html', {"data": data})

def about(req):
    s = dict(req.session)
    print(s,'*************')
    if not s:
        return redirect('login')
    return render(req,'about.html')


def work(req):

    if(req.method == "POST"):
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        data = {"username": username, "email": email, "password": password}
        print(data)
        uc.insert_one(data)
        return redirect('home')

    return render(req,'work.html')



def login(req):
    if req.method == "POST":
        email = req.POST['email']
        print('---------------',email)
        user = uc.find_one({'email': email})
        
        if(user):
            print(user)
            req.session['docId']= str(user['_id'])
            return redirect('home')
        else:
            return redirect('work')
    return render(req,'login.html')


def logout(req):
    req.session.clear()
    return redirect('login')