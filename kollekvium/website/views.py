from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    """Ana səhifə - HTML template ilə"""
    return render(request, 'home.html')

def about_view(request):
    """Haqqında səhifəsi"""
    return render(request, 'about.html')

def fastfood_view(request):
    """FastFood sifariş səhifəsi"""
    # FastFood məlumatları
    menu_items = [
        {'name': 'Klassik Burger', 'price': 7.90, 'category': 'Burger'},
        {'name': 'Double Burger', 'price': 10.50, 'category': 'Burger'},
        {'name': 'Pepperoni Pizza', 'price': 12.90, 'category': 'Pizza'},
        {'name': 'Vegetarian Pizza', 'price': 11.50, 'category': 'Pizza'},
        {'name': 'Kola', 'price': 2.50, 'category': 'İçki'},
        {'name': 'Çizkeyk', 'price': 6.90, 'category': 'Şirniyyat'},
    ]
    
    context = {
        'title': 'FastFood Express',
        'menu_items': menu_items,
        'categories': ['Hamısı', 'Burger', 'Pizza', 'İçki', 'Şirniyyat']
    }
    return render(request, 'fastfood.html', context)

def test_view(request):
    """Test səhifəsi"""
    context = {
        'title': 'Template Test',
        'message': 'Bu Django template ilə göstərilir',
        'items': ['HTML', 'CSS', 'JavaScript', 'Python', 'Django']
    }
    return render(request, 'test.html', context)