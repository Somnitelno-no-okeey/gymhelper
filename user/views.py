from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from user.models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

def auth(request):
    if request.user.is_authenticated:
        return redirect('configurator')
    if request.method == 'POST':
        if 'registration-button' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                validate_password(password)
            except ValidationError:
                return render(request, 'user/authorization.html')
            user = CustomUser.objects.create_user(username=email, email=email, password=password, first_name=name)
            user.save()
            login(request, user)
            return redirect('configurator')
        elif 'enter-button' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('configurator')
    return render(request, 'user/authorization.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('configurator')
    user = request.user
    context = {
        'name' : user.first_name,
        'email' : user.email,
    }
    return render(request, 'user/profile.html', context)

def logout_view(request):
    logout(request)
    return redirect('auth') 