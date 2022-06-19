import imp
import re
from tabnanny import check
from django.shortcuts import redirect, render
from django.views import View
from farmer.models.UserDetails import UserDetails
from django.contrib.auth.hashers import check_password

class Login(View):
    def get(self, request):
        try:
            redirect_page = request.session.redirect_page
        except:
            pass
        return render(request, 'login.html')    

    def post(self, request):
        req = request.POST
        email = req['email']
        password = req['password']
        try:
            redirect_page = req['redirect_page']
        except:
            redirect_page = ""

        userDetails = UserDetails.get_userDetalils_by_email(email)

        if not userDetails:
            msg = 'User with this mail does not exist'
            return render(request, 'login.html', {'msg' : msg})
        
        if not check_password(password, userDetails.password):
            msg = 'wrong password'
            return render(request, 'login.html', {'msg':msg})

        request.session['email'] = email
        request.session['name'] = userDetails.name
        
        if redirect_page != "":
                if redirect_page == "prediction":
                    return render(request, 'prediction.html')
        
        return render(request, 'home.html', {"logged_in":True})
                   
        
