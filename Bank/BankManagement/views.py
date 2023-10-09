from django.shortcuts import  render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.hashers import make_password, check_password




def Register_user(request):
    print("hey")
    if request.method =="POST":
        print("hello")
        FirstName = request.POST.get("FirstName")
        LastName = request.POST.get("LastName")
        email = request.POST.get("email") 
        password1 =  request.POST.get("password1") 
        password2 =  request.POST.get("password2")
        
        password=make_password(password1)
        print(password)
        if password1 != password2:
            return HttpResponse('password did not match')
        else:
            user = Register.objects.create(FirstName = FirstName, LastName = LastName,email = email, password1 = password , password2 = password2)
            print(user)
            return redirect(succes)
    return render(request,"Register.html")

def succes(request):
    return HttpResponse('succesfull uploaded')


def login(request):
    if request.method =="GET":
        if "email" in request.session:
            return render(request, "index.html")
        else:
            return render(request, "Login.html")
    if request.method =="POST":
        
        c_email = request.POST.get("email")
        password = request.POST.get("password")
        
       
        Email = Register.objects.filter(email = c_email).exists()
        if Email:
            User = Register.objects.get(email = c_email)
            
            if not check_password(password, User.password1):
                return HttpResponse("Invalid Password")
            else:
                request.session['email'] = c_email
                request.session['password'] = password

                Curr = Currency.get_all_currency()
                return render(request, "index.html" , {'Currency' : Curr, 'user':User})
        else:
            return HttpResponse('Invalid User')

    return render(request,"Login.html")



def edit_profile(request):
    print("hey")
    if request.method =="GET":
        print("hhhhhhhh")
        if "email" in request.session:
            email = request.session['email']
            print(email)
            # get_all_Register()
            check_email = Register.objects.get(email= email)
            return render(request, "changepass.html",{'check_email':check_email})
        
           
        
    return render(request,"index.html")

def checkpass(request):
    if request.method=="POST":
        oldpass = request.POST.get("oldpassword")

        oldpasscheck = Register.objects.filter(password2 = oldpass).exists()
        if oldpasscheck:
            Register.objects.filter['password1'].update(newpassword)
            Register.objects.filter(password2).update(conformpassword)
            # oldpassword = Register.objects.get(email = c_email)
        else:
            return HttpResponse("invalid user")


    return render(request,"changepass.html")

def forgetpas(request):
    
    print("herrr")
    Email = ""
    if request.method=="POST":
        print("tytyty")
        data = request.POST
        print(data)
        emailcheck = request.POST.get("Checkemail")
        print(emailcheck)
        Email = Register.objects.filter(email = emailcheck).exists()
        print(Email)
        if Email:
            print("hey")
            User = Register.objects.get(email = emailcheck)
            print(User)
            u_Pass = request.POST.get("new_password")
            u_conpass = request.POST.get("cnew_password")
            print(u_conpass)
            if u_Pass == u_conpass:
                Register.objects.filter(email=emailcheck).update(password1 = u_Pass,password2 = u_conpass)
                return HttpResponse("succesfully changed password")
            else:
                return HttpResponse("paassword and conform password will be same")
            return render(request,"Updatepass.html")
        else:
            return HttpResponse("invalid email if u r not user plz register")
        return render(request,"forgetpass.html",{'Email':Email})
    return render(request,"forgetpass.html")



def qty(request,id):
    if request.method=="POST":
       qtycheck = request.POST.get("qty") 
       print(qtycheck)
       qty = Currency.objects.get(QTY)
       print(qty)


    return render(request, "qty.html")



def logout(request):
    del request.session['email']
    del request.session['password']
    return redirect(login)


