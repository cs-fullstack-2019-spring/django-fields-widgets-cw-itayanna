from django.shortcuts import render, redirect
from .forms import RegistrationForm

# Create your views here.



def index(request):
    return render(request, 'HeroRegistrationApp/index.html')

def form(request):
    form = RegistrationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("stage 1")
            form.save()
            return redirect('thankyou')
        else:
            print(form.errors)
            print("Form not valid")
    return render(request,'HeroRegistrationApp/form.html', {'form': form})

def thankyou(request):
    return render(request, 'HeroRegistrationApp/thankyou.html')