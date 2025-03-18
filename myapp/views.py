from django.http import HttpResponse
from django.shortcuts import render
import datetime
def home(request):
    isActive = False
    if request.method=='POST':       
        check = request.POST.get('check')
        print(check)
        if check is None: isActive=False
        else: isActive= True
    
    
    date  = datetime.datetime.now()
    
    name = "AJAY PANDEY"
    list_of_programmes = [
        'WAP to check even or odd',
        'WAP to check prime',
        'WAP to print all primes numbers from ! to 100',
        'WAP to print pascals triangle'
    ]
    student={
        'studentName':"Ajay",
        'studentCollege':"KIET",
        'city':'Lucknow'
    }
    data = {
        'date':date,
        'isActive':isActive,'name':name,
        'list_of_programmes':list_of_programmes,
        'student_data':student
    }
    print("test function from view")
    return render(request,"home.html",data)
   # return HttpResponse("<h1>Index Page</h1>"+str(date))

def about(request):
    return render(request,"about.html",{})
   # return HttpResponse("<h2>About is here <h2>")

def services(request):
    return render(request,"services.html",{})
    #return HttpResponse("<h2>Services is here <h2>")