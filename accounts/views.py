from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView, UpdateView, ListView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse_lazy

from accounts.forms import LoginForm, UserRegisterForm, UserUpdateForm
from accounts.models import User

# Create your views here.
class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        username = data["username"]
        password = data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect("index")
            return HttpResponse("<h1> You account is not active</h1>")
        return HttpResponse("<h1> Invalid user data </h1>")


def logout_user(request):
    if request.user.is_authenticated: 
        logout(request)
    return redirect("index")



class UserRegisteView(CreateView):
    template_name = "register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("index")


class UpdateUserView(UpdateView):
    form_class = UserUpdateForm
    template_name = "profile.html"
    success_url = reverse_lazy("user_profile")


    def get_object(self):
        return self.request.user



class UsersSearchListView(ListView):
    template_name = "users.html"
    model = User


    def get_queryset(self): 
        search_text = self.request.GET.get("query")
        if search_text:
            search_users = User.objects.filter(username__icontains=search_text)
            return search_users
        return None  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_text"] = self.request.GET.get("query")
        return context
