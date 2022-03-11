from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm


class RegisterView(View):
    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'register.html')
    def get(self, request):
        form = NewUserForm()
        return render(request, 'register.html', context = {'register_form' : form })


class LoginView(View):
    def post(self, request):
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('admin-home')
                    #return render(request, 'home_admin.html')
                else:
                    return redirect('user-home')
                    #return render(request, 'home_user.html')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
            return render(request, 'login.html')
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', context = {'login_form' : form })



# Logout view
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

def logout_request(request):
	logout(request)
	return redirect('login')