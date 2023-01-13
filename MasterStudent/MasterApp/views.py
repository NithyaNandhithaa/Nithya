from django.db.models import Q
from django.shortcuts import render, redirect

from MasterApp.models import Task, Student, Master


# Create your views here.
def home(request):
    return render(request,'home.html')

def stulog(request):
    return render(request,'student_login.html',{'d':''})

def masterlog(request):
    return render(request,'master_login.html',{'d':''})

def sturegis(request):
    return render(request,'student_register.html')

def masregis(request):
    return render(request,'master.register.html')

def task_view(request):
    tasks = Task.objects.all()
    return render(request,'gettask.html',{'data': tasks})

def task_assign(request):
    students = Student.objects.all()
    return render(request,'givetask.html',{'data':students})

def read_student_login(request):
    username = request.POST["s_username"]
    password = request.POST["s_pass"]
    if Student.objects.filter(Q(UserName=username) & Q(Password=password)).exists():
        return render(request,'student_page.html')
    else:
        return render(request,'student_login.html',{'d':'check password and username correct or not..'})
def read_master_login(request):
    username = request.POST["m_name"]
    password = request.POST["m_pass"]
    if Master.objects.filter(Q(UserName=username) & Q(Password=password)).exists():
        return render(request,'master_page.html')
    else:
        return render(request,'master_login.html',{'d':'check password and username correct or not..'})

def read_student_register(request):
    if request.method == 'POST':
        username = request.POST["s_username"]
        name = request.POST["s_name"]
        password = request.POST["s_pass"]
        if Student.objects.filter(Q(UserName=username) | Q(Password=password)).exists():
            return render(request,'student_register.html',{'d':'username or password already exists..'})
        else:
            s1 = Student()
            s1.Name = name
            s1.UserName = username
            s1.Password = password
            s1.save()
            return render(request,'student_login.html',{'data':''})

def read_master_register(request):
    if request.method == 'POST':
        username = request.POST["m_username"]
        name = request.POST["m_name"]
        password = request.POST["m_password"]
        if Master.objects.filter(Q(UserName=username) | Q(Password=password)).exists():
            return render(request,'master_register.html')
        else:
            m1 = Master()
            m1.Name = name
            m1.UserName = username
            m1.Password = password
            m1.save()
            return render(request,'master_login.html',{'data':''})

def log_out(request):
    return redirect('home')

def create_task(request):
    t1 = Task()
    t1.Left = request.POST["left"]
    t1.Right = request.POST["right"]
    t1.Operation = request.POST["operations"]
    t1.Student_id = Student.objects.get(Name=request.POST["ddl_stu"])
    t1.save()
    tasks = Task.objects.all()
    return render(request,'gettask.html',{'data': tasks})
def solve(request,id):
    t1 = Task.objects.get(id=id)
    left = t1.Left
    left = globals()[left]
    right = t1.Right
    right = globals()[right]
    operation = t1.Operation
    operation = globals()[operation]
    print(left,right)
    res = left(operation(right()))
    return render(request,'gettask.html',{'sol':f'solution is {res}','data':Task.objects.all()})
def make_num(num,fun):
    if fun == None:
        return num
    else:
        return fun(num)
def zero(fun=None):
    return make_num(0,fun)
def one(fun=None):
    return make_num(1,fun)
def two(fun=None):
    return make_num(2,fun)
def three(fun=None):
    return make_num(3,fun)
def four(fun=None):
    return make_num(4,fun)
def five(fun=None):
    return make_num(5,fun)
def six(fun=None):
    return make_num(6,fun)
def seven(fun=None):
    return make_num(7,fun)
def eight(fun=None):
    return make_num(8,fun)
def nine(fun=None):
    return make_num(9,fun)
def plus(right):
    sum = lambda left: left + right
    return sum
def minus(right):
    sum = lambda left: left - right
    return sum
def times(right):
    sum = lambda left: left * right
    return sum
def div(right):
    sum = lambda left: left // right
    return sum
