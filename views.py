from django.shortcuts import render,redirect
from django.http import HttpResponse
from stockm.models import admindb
from django.core.files.storage import FileSystemStorage


# Create your views here.
#def index(request):
 #   return HttpResponse('hai')
def prime(request): 
      num=5
      if num > 1:
        for i in range(2, num):
            if num % i == 0:
               print(num, "is not a prime")
               break    
        else:
            
            return HttpResponse('%d is prime number' %num)         
      return HttpResponse('%d is not prime number' %num)      
def first(request):
    return render(request,'first.html') 
def submit(request):
    if request.method == 'POST':
       firstname   = request.POST.get('firstname')
       lastname    = request.POST.get('lastname')
       email       = request.POST.get('email')
       username    = request.POST.get('username')
       password    = request.POST.get('password')
       age         = request.POST.get('age')
       gender      = request.POST.get('gender')
       image       = request.FILES['image']
       fs = FileSystemStorage()
       savePath = 'image/%s' % image.name
       filename = fs.save(savePath, image)
       db=admindb(firstname=firstname,lastname=lastname,email=email,username=username,password=password,age=age,gender=gender,image=filename)
       db.save()
       return redirect('listfirst')
def listfirst(request):
    db=admindb.objects.all()
    return render(request,'listfirst.html',{'db':db})  
def updatefirst(request,dataid):
    print('************')
    db=admindb.objects.get(id=dataid)
    return render(request,'updatefiest.html',{'db':db})         
def updatereg(request,dataid):
    if request.method == 'POST':
       firstname   = request.POST.get('firstname')
       lastname    = request.POST.get('lastname')
       email       = request.POST.get('email')
       username    = request.POST.get('username')
       password    = request.POST.get('password')
       age         = request.POST.get('age')
       gender      = request.POST.get('gender')
       db=admindb.objects.filter(id=dataid).update(firstname=firstname,lastname=lastname,email=email,username=username,password=password,age=age,gender=gender)
       return redirect('listfirst')  
def deletefirst(request,dataid):
    print('************')
    db=admindb.objects.get(id=dataid)
    db.delete()
    return redirect('listfirst')         
       
def index(request):
    return render(request,'index.html')
