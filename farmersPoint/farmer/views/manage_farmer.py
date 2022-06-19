from django.shortcuts import render
from django.views import View
from farmer.models.UserDetails import UserDetails

class Manage_Farmer(View):
    def get(self, request):
        userDetails = UserDetails.objects.all().values()
        print("-----userdetails",userDetails)
        return render(request, 'manage_farmer.html', {"userDetails":userDetails})

    def post(self, request):
        req = request.POST
        if req["action"] == "delete":
            UserDetails.objects.filter(email=req["mail"]).delete()
            userDetails = UserDetails.objects.all().values()
            return render(request, 'manage_farmer.html', {"userDetails":userDetails})
        elif req["action"] == "add":
            return render(request, 'signup.html')