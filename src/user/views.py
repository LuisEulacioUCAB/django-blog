from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Profile
# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin
from .forms import RegisterForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.models import User


class RegisterUser(SuccessMessageMixin, CreateView):
    template_name = "user/register.html"
    model = Profile
    form_class = RegisterForm
    success_url = reverse_lazy('register')
    success_message = "El usuario %(username)s  se ha registrado correctamente"


    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            username=self.object.username,
        )

    def form_valid(self, form ):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)


def valid_username(request):
    if request.method == "POST":
        data = request.POST
        username = str(data.get('username',''))
        user = User.objects.filter(username=username)
        s = serializers.serialize('json', user)
        if user != None:
            return HttpResponse(s)
        else:
            return HttpResponse(s)


def login(request):
    return render(request, 'user/login.html')

