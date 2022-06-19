from django.shortcuts import render
from django.views import View

class Logout(View):
    def get(self, request):
        del request.session["email"]
        return render(request, 'home.html', {"logged_out":True})