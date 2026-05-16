from django.shortcuts import render,redirect
from .forms import SignUpForm
from .models import Profile, CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages



#defalt page
def index(request):
  return render(request, "auth_app/base.html") 


# login View
def login_view(request):
  if request.method == 'POST':
    user_username = request.POST.get('username_or_email')
    user_password = request.POST.get('password')
    user = authenticate(request, 
      username = user_username,
      password = user_password)

    if user is not None:
      login(request, user)
      next_url = request.POST.get('next') or request.GET.get('next') 
      messages.success(request, "user login successfully")
      return redirect(next_url or "auth_app:index")
    messages.error(request, "your credentials does not match")    
  return render(request, "auth_app/login.html") 


# custom logout
def logout_view(request):
  logout(request)
  return redirect("auth_app:login")

# protected page
@login_required
def dashboard_view(request):
  return render(request, "auth_app/dashboard.html")

# register view
def register_view(request):
  if request.method == "POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data["username"]
      email = form.cleaned_data["email"]
      password = form.cleaned_data["password"]
      phone = form.cleaned_data["phone"]  
      new_user = CustomUser.objects.create_user(      
        username = username,
        email = email,
        password = password        
      )
      Profile.objects.create(user = new_user, phone_number = phone)
      return redirect("auth_app:login")
    else:
       return render(request, "auth_app/signup.html", {
        "form": form
       })   
  else:
    form =  SignUpForm()
  
    return render(request, "auth_app/signup.html", {
    "form": form
  })
 