from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic

# 登录
class SigninView(LoginView):
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')
    template_name = "pages/signin.html"

# 注册
class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("signin")
    template_name = "pages/signup.html"

# 登出
def signout(request):
    logout(request)
    messages.success(request,'成功退出登录')
    return redirect('signin')

# 个人信息
@login_required
def profile(request):
    return render(request, "pages/profile.html")

