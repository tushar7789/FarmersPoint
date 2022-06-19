from django.urls import path
from .views import home, about, signup, login, prediction, logout, admin_login, manage_farmer

urlpatterns = [
    path('', home.Home.as_view(), name='home'),
    path('about', about.About.as_view(), name='about'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login'),
    path('prediction', prediction.Prediction.as_view(), name='prediction'),
    path('logout', logout.Logout.as_view(), name='logout'),
    path('admin-login', admin_login.Admin_Login.as_view(), name='admin-login'),
    path('manage-farmer', manage_farmer.Manage_Farmer.as_view(), name='manage-farmer')
]