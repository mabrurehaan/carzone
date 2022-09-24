from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User


# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        destination = request.POST['destination']
        phone = request.POST['phone']
        requisition_form = request.POST['requisition_form']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an reguisition about this vehicle. Please wait until we get back to you.')
                return redirect('/cars/'+car_id)

        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id,
        first_name=first_name, last_name=last_name, customer_need=customer_need, start_date=start_date,
        end_date=end_date, destination=destination, phone=phone, requisition_form=requisition_form, message=message)

        # admin_info = User.objects.get(is_superuser=True)
        # admin_email = admin_info.email
        # send_mail(
        #         'New Car Reguisition',
        #         'You have a new inquiry for the car ' + car_title + '. Please login to your admin panel for more info.',
        #         'mabrurehaan@gmail.com',
        #         [admin_email],
        #         fail_silently=False,
        #     )

        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('/cars/'+car_id)
