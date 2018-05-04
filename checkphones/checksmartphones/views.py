from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.views import View

from checksmartphones import forms
from checksmartphones.forms import SearchForm, LoginForm, RegisterForm, UserSearchForm
from checksmartphones.models import HiddenModel
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
            similar = form.cleaned_data['similar']
            similar2 = form.cleaned_data['similar2']

            phones = fon.getdevice(device, brand=brand, position=position)
            phones2 = fon.getdevice(device2, brand=brand2, position=position2)

            list_dicts = phones.list_of_dicts()
            list_dicts2 = phones2.list_of_dicts()
            dictio = list_dicts[0]
            dictio2 = list_dicts2[0]
            return render(request, 'test.html', {'form': form, 'list_dicts': list_dicts, 'list_dicts2': list_dicts2,
                                                 'ok':True, 'attributes': attributes, 'dictio': dictio,
                                                 'dictio2': dictio2, 'similar': similar, 'similar2': similar2})
        else:
            form = SearchForm()
            return render(request, 'test.html', {'form': form, 'message': 'Choose attributes'})

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
                return redirect('/user_page/')

            else:
                return render(request, 'login.html', {'form': form, 'message': 'Wrong login or password'})

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
                return render(request, 'register.html', {'form': form, 'message': 'The password does not match'})
            else:
                try:
                    User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                             last_name=last_name)
                    return render(request, 'register.html', {'form': form, 'message': 'User created'})
                except:
                    return render(request, 'register.html', {'form': form, 'message': 'Username already exist'})
        else:
            form = RegisterForm()
            return render(request, 'register.html', {'form': form, 'message': 'Invalid data'})

class UserPageView(LoginRequiredMixin, View):

    def get(self, request):
        form = UserSearchForm()
        all_attributes = forms.all_attributes
        favourites = HiddenModel.objects.filter(user_id=request.user.id)
        return render(request, 'userpage.html', {'form': form, 'all_attributes': all_attributes,
                                                 'favourites': favourites})


    def post(self, request):
        form = UserSearchForm(request.POST)
        fon = fonoapi.FonoAPI('cf3590b49448175eb05232c57bfc1d257cbf93113742cbfc')

        if 'find' in request.POST:
            if form.is_valid():
                device = form.cleaned_data['device']
                position = form.cleaned_data['position']
                brand = form.cleaned_data['brand']
                attributes = form.cleaned_data['attributes']
                phones = fon.getdevice(device, brand=brand, position=position)
                list_dicts = phones.list_of_dicts()
                dictio = list_dicts[0]
                all_attributes = forms.all_attributes
                favourites = HiddenModel.objects.filter(user_id=request.user.id)

                return render(request, 'userpage.html',
                              {'form': form, 'list_dicts': list_dicts, 'ok': True, 'attributes': attributes,
                               'dictio': dictio, 'favourites': favourites, 'all_attributes': all_attributes})

            else:
                form = UserSearchForm()
                all_attributes = forms.all_attributes
                favourites = HiddenModel.objects.filter(user_id=request.user.id)
                return render(request, 'userpage.html', {'form': form, 'all_attributes': all_attributes,
                                                         'favourites': favourites, 'message': 'Choose attributes'})

        elif 'to_db_btn' in request.POST:
            to_db = request.POST['to_db']
            all_attributes = forms.all_attributes
            favourites = HiddenModel.objects.filter(user_id=request.user.id)
            HiddenModel.objects.create(to_db=to_db, user_id=request.user.id)
            return render(request, 'userpage.html', {'form': form, 'favourites': favourites,
                                                     'all_attributes': all_attributes})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class Boot(View):
    def get(self, request):
        return render(request, 'index.html')

#Co jest do zrobienia:
    # - wyszukiwanie po atrybutach, np mniejsze od 150g wg. slownika
    # - jeden tel moze byc dodany tylko raz(id to bedzie DeviceName)

    # -
    #
    # - **mozna zmienic nazwy atrybutow na ladniejsze**
