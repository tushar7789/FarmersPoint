from django.urls import path
from .views import home, about, signup, login, prediction, logout, prediction_with_id

urlpatterns = [
    path('', home.Home.as_view(), name='home'),
    path('about', about.About.as_view(), name='about'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login'),
    path('prediction', prediction.Prediction.as_view(), name='prediction'),
    path('logout', logout.Logout.as_view(), name='logout'),
    path('predict/<str:f_mail>', prediction_with_id.Prediction_With_Id.as_view() , name='prediction_with_id')
]