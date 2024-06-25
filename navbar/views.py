from django.shortcuts import render
from . models import Department,Doctor
from .forms import BookingForm

# Create your views here.
def home(request):
    return render(request,"home.html")
def contact(request):
    return render(request,"contact.html")

def department(request):
    dictionary_department={
        'department_key':Department.objects.all()
    }
    return render(request,"department.html",dictionary_department)

def doctors(request):
    dictionary_doctors={
        'doctors_key':Doctor.objects.all()
    }
    return render(request,"doctors.html",dictionary_doctors)
def about(request):
    return render(request,"about.html")




def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=BookingForm()
    dict_booking={
        'form_key' :form
    }
    return render(request,"booking.html",dict_booking)

