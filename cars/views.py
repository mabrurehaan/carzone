from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import *

# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 3)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    brand_search = Car.objects.values_list('Brand_Name', flat=True).distinct()
    fuel_search = Car.objects.values_list('fuel_Type', flat=True).distinct()
    year_search = Car.objects.values_list('manufacture_Year', flat=True).distinct()
    type_search = Car.objects.values_list('type_of_Vehicle', flat=True).distinct()
    seating_search = Car.objects.values_list('seating_Capacity', flat=True).distinct()
    data = {
        'cars': paged_cars,
        'seating_search': seating_search,
        'brand_search': brand_search,
        'fuel_search': fuel_search,
        'year_search': year_search,
        'type_search': type_search,
    }

    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)

    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_detail.html', data)

def search(request):
    cars = Car.objects.order_by('-created_date')

    brand_search = Car.objects.values_list('Brand_Name', flat=True).distinct()
    fuel_search = Car.objects.values_list('fuel_Type', flat=True).distinct()
    year_search = Car.objects.values_list('manufacture_Year', flat=True).distinct()
    type_search = Car.objects.values_list('type_of_Vehicle', flat=True).distinct()
    seating_search = Car.objects.values_list('seating_Capacity', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission_Type', flat=True).distinct()


    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(passenger_Information__icontains=keyword)
    
    if 'Brand_Name' in request.GET:
        Brand_Name = request.GET['Brand_Name']
        if Brand_Name:
            cars = cars.filter(Brand_Name__iexact=Brand_Name)

    if 'fuel_Type' in request.GET:
        fuel_Type = request.GET['fuel_Type']
        if fuel_Type:
            cars = cars.filter(fuel_Type__iexact=fuel_Type)

    if 'manufacture_Year' in request.GET:
        manufacture_Year = request.GET['manufacture_Year']
        if manufacture_Year:
            cars = cars.filter(manufacture_Year__iexact=manufacture_Year)

    if 'seating_Capacity' in request.GET:
        seating_Capacity = request.GET['seating_Capacity']
        if seating_Capacity:
            cars = cars.filter(seating_Capacity__iexact=seating_Capacity)

    if 'type_of_Vehicle' in request.GET:
        type_of_Vehicle = request.GET['type_of_Vehicle']
        if type_of_Vehicle:
            cars = cars.filter(type_of_Vehicle__iexact=type_of_Vehicle)

    if 'transmission_Type' in request.GET:
        transmission_Type = request.GET['transmission_Type']
        if transmission_Type:
            cars = cars.filter(transmission_Type__iexact=transmission_Type)


    data = {
        'cars': cars,
        'seating_search': seating_search,
        'brand_search': brand_search,
        'fuel_search': fuel_search,
        'year_search': year_search,
        'type_search': type_search,
        'transmission_search': transmission_search,
    }
    return render(request, 'cars/search.html', data)