from django.shortcuts import render,redirect, get_object_or_404
from Face_Detection.detection import FaceRecognition
from .forms import *
from django.contrib import messages

faceRecognition = FaceRecognition()

def home(request):
    if request.method == "POST":
        form = ResgistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            print("IN HERE")
            messages.success(request,"SucceessFully registered")
            addFace(request.POST['reg_number'])
            redirect('home')
        else:
            messages.error(request,"Account registered failed")
    else:
        form = ResgistrationForm()
    return render(request,'faceDetection/home.html', {'form':form})


def register(request):
    if request.method == "POST":
        form = ResgistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            print("IN HERE")
            messages.success(request,"SuceessFully registered")
            addFace(request.POST['reg_number'])
            redirect('home')
        else:
            messages.error(request,"Account registered failed")
    else:
        form = ResgistrationForm()

    return render(request, 'faceDetection/register.html', {'form':form})

def addFace(reg_number):
    reg_number = reg_number
    faceRecognition.faceDetect(reg_number)
    faceRecognition.trainFace()
    return redirect('/')

def login(request):
    reg_number = faceRecognition.recognizeFace()
    print(reg_number)
    return redirect('quizes:main-view' ,str(reg_number))

# def Greeting(request,reg_number):
#     reg_number = int(reg_number)

#     context = {
# 		'user' : UserProfile.objects.get(reg_number = reg_number)
# 	}
#     return render(request,'faceDetection/greeting.html',context=context)

