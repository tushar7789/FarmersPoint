import imp
import re
from tabnanny import check
from django.shortcuts import redirect, render
from django.views import View
from farmer.models.UserDetails import UserDetails
from django.contrib.auth.hashers import check_password

class Admin_Login(View):
    def get(self, request):
        return render(request, 'admin_login.html')    

    def post(self, request):
        req = request.POST
        email = req['email']
        password = req['password']

        userDetails = UserDetails.get_userDetalils_by_email(email)

        if not userDetails:
            msg = 'User with this mail does not exist'
            return render(request, 'admin_login.html', {'msg' : msg})
        
        if not check_password(password, userDetails.password):
            msg = 'wrong password'
            return render(request, 'admin_login.html', {'msg':msg})
        
        userDetails = UserDetails.objects.all().values()

        return render(request, 'manage_farmer.html', {"userDetails": userDetails})