from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from calendog.forms import CallendogForm
from calendog.models import Caretaker, AddCallendog


def home(request):
    return render(request, "calendog/home.html")

# Auth


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"

    # add automatic login after signup
    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get("username"), form.cleaned_data.get("password1"),
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view


class AddCaretaker(generic.CreateView):
    model = Caretaker
    fields = ["name", "email"]
    template_name = "calendog/add_caretaker.html"
    success_url = reverse_lazy("home")

    # adding user data to the form
    def form_valid(self, form):
        form.instance.user = self.request.user
        super(AddCaretaker, self).form_valid(form)
        return redirect("home")


# class CreateCalendog(generic.CreateView):
#     model = AddCallendog
#     fields = ["title", "start_date", "stop_date", "frequency", "caretakers"]
#     template_name = "calendog/create_callendog.html"
#     success_url = reverse_lazy("home")
#
#     # adding user data to the form
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         super(CreateCalendog, self).form_valid(form)
#         return redirect("home")


class CreateCallendog(generic.CreateView):
    template_name = "calendog/create_callendog.html"
    form_class = CallendogForm

    def get_form_kwargs(self):
        kwargs = super(CreateCallendog, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
