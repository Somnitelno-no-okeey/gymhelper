from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from user.models import CustomUser

def auth(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        if 'registration-button' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = CustomUser.objects.create_user(username=email, email=email, password=password, first_name=name)
            user.save()
            login(request, user)
            return redirect('profile')
        elif 'enter-button' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    return render(request, 'user/authorization.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('auth')
    user = request.user
    context = {
        'name' : user.first_name,
        'email' : user.email,
    }
    return render(request, 'user/profile.html', context)


def logout_view(request):
    logout(request)
    return redirect('auth') 