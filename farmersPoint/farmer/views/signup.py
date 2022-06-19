from unittest import result
from django.shortcuts import render, redirect
from django.views import View
from farmer.models import UserDetails
import re
from django.contrib.auth.hashers import make_password


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        req = request.POST
        data = {
            'name' : req['username'],
            'email':req['email'],
            'password': req['password'],
            'confirm_password' : req['confirm_password']
        }
        
        errors = self.validate(data)

        if errors['error1'] != '' or errors['error2'] != '' or errors['error3']:
            return render(request, 'signup.html', {'errors' : errors, 'data' : data})

        userDetails = UserDetails(name = data['name'],email = data['email'], password = data['password'])

        res = userDetails.account_exists(data['email'])

        if res:
            return render(request, 'signup.html', {'msg' : 'Account with this mail already exists!'})
        
        userDetails.password = make_password(userDetails.password)
        userDetails.register()

        request.session["registered"] = True
        request.session["email"] = userDetails.email
        request.session["name"] = userDetails.name
        return redirect('home')
    
    def validate(self, data):
        errors = {
            'error1':'',
            'error2':'',
            'error3':''
        }
        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']

        matcher = re.compile(r'^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$')
        result = matcher.match(email)
        
        if len(password) > 15 or len(password) < 5:
            errors['error2'] = "password length should be between 5 and 15"
        if not result:
            errors['error1'] = "email is not in proper format"
        if confirm_password != password and not errors['error2']:
            errors['error3'] = "password don't match"

        return errors 