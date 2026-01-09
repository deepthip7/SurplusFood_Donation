from django.shortcuts import render, redirect
from .models import FoodItem

def welcome_view(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'restaurant':
            return redirect('restaurant-dashboard')
        elif role == 'volunteer':
            return redirect('volunteer-dashboard')
    return render(request, 'login.html')

def restaurant_dashboard(request):
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        temperature = request.POST['temperature']
        restaurant_name = request.POST['restaurant_name']
        address = request.POST['address']
        FoodItem.objects.create(
            name=name,
            quantity=quantity,
            temperature=temperature,
            restaurant_name=restaurant_name,
            address=address
        )
    #foods = FoodItem.objects.all()
    return render(request, 'restaurant_dashboard.html', )

def volunteer_dashboard(request):
    foods = FoodItem.objects.all()
    needy_areas = [
        "Slum Area - Gandhi Nagar",
        "Old Age Home - Lakshmi Layout",
        "Children Shelter - Green Road",
        "Community Hall - West End"
    ]
    if request.method == 'POST':
        food_id = request.POST.get('food_id')
        area = request.POST.get('area')
        food = FoodItem.objects.get(id=food_id)
        food.assigned = True
        food.delivered = True
        food.save()
    return render(request, 'volunteer_dashboard.html', {'foods': foods, 'needy_areas': needy_areas})