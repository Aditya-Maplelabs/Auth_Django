from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from .models import Sample,User
from django.contrib.auth.hashers import make_password, check_password


# def InsertRecord(request):
#     if request.method == 'POST':
#         if request.POST.get('name'):
#             save_data = Sample()
#             save_data.name = request.POST.get('name')
#             save_data.save()
#             messages.success(request,'Record saved successfully')

#             return render(request,'index.html')

#         else:
#             messages.error(request,'Name field empty')

#     return redirect('/otp',otp='1234')

    # return render(request,'index.html')

def Register(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            #check if user exists
            try:
                User.objects.get(username=request.POST.get('username'))
                messages.error(request,'Username Already exists, try logging in!')
            except User.DoesNotExist:
                user = User()
                user.username = request.POST.get('username')
                user.password = make_password(request.POST.get('password'))
                user.save()
                messages.success(request,'User registered successfully')
                

        else:
            messages.error(request,'All fields are required')


    return render(request,'register.html')


def Login(request):
    if request.method == 'POST':
        #check if user exists 
        try:
            user = User.objects.get(username=request.POST.get('username'))
            user = user.get_user()
            if check_password(request.POST.get('password'),user['password']):
                # messages.success(request,'Login successfully')
                #Set user in the session, so he remain logged in
                request.session['username'] = user['username']
                return redirect('/home')  
            else:
                messages.error(request,'Password does not match.')

        except User.DoesNotExist:
            print("Not FOUND")
            pass

    return render(request,'login.html')

def Logout(request):
    del request.session['username']
    messages.success(request,'Logout successful !')
    return redirect('/login')

def Home(request):
    if 'username' in request.session:
        context = {"username":request.session['username']}
        return render(request,'home.html',context)    
    messages.error(request,"Please login !!")
    return redirect('/login')

def OtpVerify(request):
    print(request.GET)
    if request.method == 'POST':
        pass

    return render(request,'otp.html')