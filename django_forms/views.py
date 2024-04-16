from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import UserData

def save_user_data(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Saves data to the database
            return render (request,'index.html')  # Redirect to success page after saving
    else:
        form = UserForm()  # Create an empty form for GET requests

    return render(request, 'form.html', {'form': form})
from .models import UserData

def read_user_data(request):
    users = UserData.objects.all()  # Retrieve all data from the model

    return render(request, 'data.html', {'users': users})

