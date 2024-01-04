from django.shortcuts import render,redirect, get_object_or_404
from fkeyapp.models import Course,Student,Usermember
from django.template.defaultfilters import date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from fnmatch import fnmatchcase
from django.contrib.auth.models import User,auth 
import os
# Create your views here.


def admin_home(request):
    if request.user.is_authenticated and request.user.is_staff:
        print(request.user.id)
        return render(request,'admin_home.html')
    return render(request,'admin_login.html')

def user_home(request):
    if request.user.is_authenticated:

        return render(request,'user_home.html')
    return redirect('/')

def loginhome(request):
        
    return render(request,'admin_login.html')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/')




def admin_login(request):
    
    if request.method=='POST':
        username=request.POST['name']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('admin_home')
            else:
                login(request,user)
                auth.login(request,user)
                messages.info(request,f'Welcome {username}')
                return redirect('user_home')
        else:
            messages.info(request,"Invalid username or password")
            return redirect('/')
    return render(request,'admin_login.html')        



def add_course(request):
    if request.user.is_authenticated:
        return render(request,'add_course.html')

def addcourse(request):
    if request.user.is_authenticated:
        return render(request,'add_course.html')

def addstudent(request):
    
    student=Student.objects.all()
    return render(request,'add_student.html',{'students':student})

def showstudent(request):
    if request.user.is_authenticated:
        student=Student.objects.all()
        return render(request,'show_details.html',{'students':student})

def add_coursedb(request):
    if request.method=='POST':
        course_name=request.POST.get('course')
        course_fee=request.POST.get('fee')
        course=Course(course_name=course_name,fee=course_fee)
        course.save()
        return redirect('add_student')
    
def add_student(request):
    if request.user.is_authenticated:
        courses=Course.objects.all()
        return render(request,'add_student.html',{'course':courses})

def add_studentdb(request):
    
    if request.method=='POST':
        student_name=request.POST['name']
        student_address=request.POST['address']
        age=request.POST['age']
        jdate=request.POST['jdate']
        sel=request.POST['sel']
        course1=Course.objects.get(id=sel)
        student=Student(student_name=student_name,student_address=student_address,student_age=age,joining_date=jdate,course=course1)
        student.save()
        return redirect('show_details')

def show_details(request):
    if request.user.is_authenticated:
        student=Student.objects.all()
        return render(request,'show_details.html',{'students':student})

def signup(request):
    
    courses=Course.objects.all()
    return render(request,'user_register.html',{'course':courses})

def user_register(request):
    if request.user.is_authenticated:
        courses=Course.objects.all()
        return render(request,'user_register.html',{'course':courses})

def addteacher(request):
    
        if request.method=='POST':
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['username']
            password=request.POST['password']
            cpassword=request.POST['cpassword']
            address=request.POST['address']
            age=request.POST['age']
            email=request.POST['email']
            number=request.POST['number']
            image=request.FILES.get('file')
            sel=request.POST['sel']
            course1=Course.objects.get(id=sel)
        
            if password==cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'This username already exists!!!!!')
                    return redirect('user_register')
                else:
                    user=User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        password=password,
                        email=email)
                    user.save()
                    register=Usermember(address=address,age=age,number=number,course=course1,image=image,user=user)
                    register.save()
                    return redirect('/')
            else: 
                messages.info(request,'password doesnt match!!!!')
                return redirect('user_register')
            
        else:
            return render(request,'user_register.html') 



def edit(request,pk):
    if request.user.is_authenticated:
        student=Student.objects.get(id=pk)
        course=Course.objects.all()
        return render(request,'edit.html',{'stud':student,'course':course})
    
def editdb(request,pk):
    if request.user.is_authenticated:
        if request.method=='POST':
            stud=Student.objects.get(id=pk)
            stud.student_name=request.POST.get('name')
            stud.student_address=request.POST.get('address')
            stud.student_age=request.POST.get('age')
            stud.joining_date = date(stud.joining_date, 'Y-m-d')
            sel=request.POST.get('sel')
            course1=Course.objects.get(id=sel)
            stud.course=course1
            course1.save()
            stud.save()
            return redirect('show_details')
        return render(request,"edit.html")


       
def edit_teacher(request,pk):
    if request.user.is_authenticated:
        current_user=request.user.id
        user1=Usermember.objects.get(user=current_user)
        course=Course.objects.all()
        return render(request,'edit_profile.html',{'user':user1,'c':course})  

def editteacher(request,pk):
    if request.user.is_authenticated:
        current_user=request.user.id
        print(current_user)
        user1=Usermember.objects.get(user_id=current_user)
        user2=User.objects.get(id=current_user)
        if request.method=='POST':
            if len(request.FILES)!=0:
                if len(user1.image)>0:
                    os.remove(user1.image.path)
                user1.image=request.FILES.get('file')
       
            user2.first_name=request.POST.get('first_name')
            user2.last_name=request.POST.get('last_name')
            user2.username=request.POST.get('username')
            sel=request.POST.get('sel')
            course1=Course.objects.get(id=sel)
            user1.course=course1
            course1.save()
            user1.address=request.POST.get('address')
            user1.age=request.POST.get('age')
            user2.email=request.POST.get('email')
            user1.number=request.POST.get('number')
            
            user1.save()    
            user2.save()
            return render(request,'profile.html',{'user':user1})
        return redirect('showprofile')
        
    return redirect('/')  

def showteacher(request):
    if request.user.is_authenticated:
        user1=Usermember.objects.all()
        return render(request,'show_teacher.html',{'user':user1})
    return redirect('/')

def showprofile(request,pk):
    if request.user.is_authenticated:
        current_user=request.user.id
        
        user1=Usermember.objects.get(user_id=current_user)
        return render(request,'profile.html',{'user':user1})

def goback(request):
    if request.user.is_authenticated:
        
        return render(request,'user_home.html')

def delete(request,pk):
    if request.user.is_authenticated:
        stud=Student.objects.get(id=pk)
        stud.delete()
        return redirect('show_details')

def delete1(request,pk):
    if request.user.is_authenticated:
        user=Usermember.objects.get(id=pk)
        if user.image:
            user.image.delete()
        user.delete()
        user.user.delete()
        return redirect('showteacher')