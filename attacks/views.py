from django.shortcuts import render
from django.db import connection
from .models import User

def home_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        
        # Finding the user using ORM
        user = User.objects.filter(name=name, password=password).first()
        
        # Find the user using a raw MySQL query
        # with connection.cursor() as cursor:
        #     query = f"SELECT * FROM users WHERE name = '{name}' AND password = '{password}'"
        #     cursor.execute(query)
        #     user = cursor.fetchone()
        
        if(user):
            print(f"\nCongrats!\nUser found successfully!\n")
        else:
            print("\nInvalid username or password!\n")
        
    return render(request, 'index.html')