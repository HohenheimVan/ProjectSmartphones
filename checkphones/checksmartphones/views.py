from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.views import View

from checksmartphones.forms import SearchForm, LoginForm, RegisterForm
from fonoapi import fonoapi

class IndexView(View):

    def get(self, request):
        form = SearchForm()
        return render(request, 'test.html', {'form': form})

    def post(self, request):
        form = SearchForm(request.POST)

        fon = fonoapi.FonoAPI('cf3590b49448175eb05232c57bfc1d257cbf93113742cbfc')
        if form.is_valid():
            device = form.cleaned_data['device']
            position = form.cleaned_data['position']
            brand = form.cleaned_data['brand']
            device2 = form.cleaned_data['device2']
            position2 = form.cleaned_data['position2']
            brand2 = form.cleaned_data['brand2']
            attributes = form.cleaned_data['attributes']

            phones = fon.getdevice(device, brand=brand, position=position)
            phones2 = fon.getdevice(device2, brand=brand2, position=position2)

            list_dicts = phones.list_of_dicts()
            list_dicts2 = phones2.list_of_dicts()
            return render(request, 'test.html', {'form': form, 'list_dicts': list_dicts, 'list_dicts2': list_dicts2, 'ok':True, 'attributes': attributes})

class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self,request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

            else:
                message = 'zly login lub haslo'
                return render(request, 'login.html', {'form': form, 'message': message})
class RegisterView(View):
    def get(self,request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            if password != password2:
                return render(request, 'register.html', {'form': form, 'message': 'Hasło się nie zgadza'})
            else:
                try:
                    User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                             last_name=last_name)
                    return render(request, 'register.html', {'form': form, 'message': 'User created'})
                except:
                    return render(request, 'register.html', {'form': form, 'message': 'Username already exist'})


class UserPageView(View):
    def get(sel, request):
        return render(request, 'userpage.html')
