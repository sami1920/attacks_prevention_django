from django.shortcuts import render
from .forms import UserInfoForm

def user_info(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Do something with the form data (e.g., save to the database)
            # For now, just print the data
            print(f"Received form submission:\nEmail: {email}\nPassword: {password}")
            return render(request, 'success.html')  # Create success.html later
    else:
        form = UserInfoForm()

    return render(request, 'user_info.html', {'form': form})
