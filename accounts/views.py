import json
import binascii
import os
from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.db.models import Q, Sum
from django.contrib.auth.decorators import login_required
#from .decorators import login_required_ajax


def account(request):
	pass



def user_regiter(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')

        email = email.lower()
        cus = User.objects.filter(Q(email=email) | Q(username=username))
        if cus:
            return HttpResponse(json.dumps(2), content_type="application/json")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_active = True
            user.save()
            profileinfo = UserProfile(user=user, mobile=mobile, userstatus=1,)
            profileinfo.save()

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            return HttpResponseRedirect("/")
    else:
       return render(request, 'accounts/register.html')


def login_site(request):
    if request.method == "POST":
        cus = None
        username = request.POST.get('username') 
        password = request.POST.get('password')
        try:
            cus = User.objects.get(username=username)
        except:
            try:
                cus = User.objects.get(email=username)
            except:
                return HttpResponseRedirect("/signin/?msg=Username is not correct.Please fill correct one.")
        user = authenticate(username=cus.username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect("/iq/")
        else:
            return HttpResponseRedirect("/signin/?msg=Password is not correct.Please fill correct one.")
    else:
        return render(request, 'accounts/login.html', {})


#@login_required
def changepassword(request):
    if not request.user.is_authenticated:
        return HttpResponse(json.dumps(3), content_type="application/json")
    password = request.POST.get('new_password')
    try:
        user = request.user
        user.set_password(password)
        user.save()
    except:
        return HttpResponse(json.dumps(2), content_type="application/json")

    return HttpResponse(json.dumps(1), content_type="application/json")



def forgotpassword(request):
    template_name = 'accounts/forgotpassword.html'
    msg = None
    if request.method == "POST":
        sourcemail = request.POST.get('email')
        username = request.POST.get('username')
        asd = str(sourcemail)
        try:
            obj = User.objects.get(email=asd, username=username)
            password=obj.userdetail.mobile
            password= ''.join(random.choice(string.ascii_letters) for x in range(6))
            obj.set_password(password)
            obj.save()
            templatename="mail/forgot-mailer.html"
            c={'user':obj,}
            message = loader.render_to_string(templatename, c)
            send_mail('Instructions for changing your blacknwhite Password',message,'"BlacknWhite Account" <support@blacknwhite.org>',[sourcemail],fail_silently=False,html_message=message)
            msg = "Please <a href='/signin/%s/'>click here</a> for login on your account. After login please visit profile page to change your password for further use." % (
                obj.username)
        except Exception as e:
            return render(request, template_name,
                          {'msg': "We have not any user associated with that username and email id."})
        return render(request, template_name, {'msg': msg})
    return render(request, template_name, {})


def admin_login(request, username):
    user = User.objects.get(username=username)
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)
    return HttpResponseRedirect("/")


#@login_required_ajax
def accounts(request):
    try:
        referal = UserProfile.objects.get(user=request.user)
        refer = referal.refer_by
    except:
        refer = 'No refer'
    template_name = 'accounts/profile.html'
    if request.method == "POST":
        try:
            name = request.POST.get('first_name')
            mobile = request.POST.get('mobile')
            request.user.first_name = name
            request.user.save()
            request.user.userdetail.mobile = mobile
            request.user.userdetail.save()
            return HttpResponse(json.dumps(1), content_type="application/json")
        except:
            return HttpResponse(json.dumps(2), content_type="application/json")
    return render(request, template_name, {'refer':refer})



def auth_logout(request):
    logout(request)
    return HttpResponseRedirect("/")



def aboutus(request):
    return render(request, 'aboutus.html')


def contactus(request):
    if request.method == "contactform" and "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = int(request.POST.get('mobile'))
        message = request.POST.get('message')
        # country_id = int(request.POST.get('country'))
        status = 1
        c = ContactUs(name=name, email=email, mobile=mobile, message=message, status=status)
        c.save()     
    return render(request, 'contactus.html')

