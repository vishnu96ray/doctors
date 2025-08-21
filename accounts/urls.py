from django.urls import path
from accounts import views

urlpatterns = [
    path('account/', views.account, name='account'),
    path('register/user/', views.user_regiter, name="accounts"),
    path('change/password/', views.changepassword, name='changepassword'),
    path('forgot/password/', views.forgotpassword, name='forgotpassword'),
    path('signin/', views.login_site, name='login'),
    path('logout/', views.auth_logout, name='logout'),

    path('allowtalks/aboutus/', views.aboutus, name="aboutus"),
    path('allowtalks/contactus/', views.contactus, name="contactus"),
]