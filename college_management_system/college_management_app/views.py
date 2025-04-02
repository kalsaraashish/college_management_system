from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from college_management_app.EmailBackEnd import EmailBackEnd
from django.urls import reverse


# Create your views here.
def showDemo(request):
    return render(request,'demo.html')

def ShowLoginPage(request):
    return render(request,"login_page.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            # return HttpResponseRedirect('/admin_home')
            if user.user_type=="1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("staff_home"))
                # return HttpResponse("Staff login"+str(user.user_type))
            else:
                return HttpResponseRedirect(reverse("student_home"))
                # return HttpResponse("Student login"+str(user.user_type))
            # return HttpResponse(request.POST.get("email") + request.POST.get("password"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")
            # return HttpResponse("Invalid login")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")

from django.template.loader import get_template

try:
    template = get_template("registration/password_reset_form.html")
    print(f"Template found: {template.origin.name}")
except:
    print("Template NOT found!")
