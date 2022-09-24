from django.shortcuts import render, redirect
from .models import *
from cars.models import Car
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home(request):
    teams = Team.objects.all()
    requisition_cars = Car.objects.order_by('-created_date').filter(is_requisition=True)
    all_cars = Car.objects.order_by('-created_date')
    #search_fields = Car.objects.values('Brand_Name', 'manufacture_Year', 'fuel_Type', 'seating_Capacity', 'type_of_Vehicle')
    brand_search = Car.objects.values_list('Brand_Name', flat=True).distinct()
    fuel_search = Car.objects.values_list('fuel_Type', flat=True).distinct()
    year_search = Car.objects.values_list('manufacture_Year', flat=True).distinct()
    type_search = Car.objects.values_list('type_of_Vehicle', flat=True).distinct()
    seating_search = Car.objects.values_list('seating_Capacity', flat=True).distinct()
    context = {
        'teams' : teams,
        'requisition_cars' : requisition_cars,
        'all_cars': all_cars,
        'seating_search': seating_search,
        'brand_search': brand_search,
        'fuel_search': fuel_search,
        'year_search': year_search,
        'type_search': type_search,
    }
    return render(request, 'pages/home.html', context)

def about(request):
    teams = Team.objects.all()
    
    context = {
        'teams' : teams,
        
    }
    return render(request, 'pages/about.html', context)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from Carzone website regarding ' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message

        # admin_info = User.objects.get(is_superuser=True)
        # admin_email = admin_info.email
        # send_mail(
        #         email_subject,
        #         message_body,
        #         'mabrurehaan@gmail.com',
        #         [admin_email],
        #         fail_silently=False,
        #     )
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')

    return render(request, 'pages/contact.html')