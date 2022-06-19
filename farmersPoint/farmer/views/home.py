from django.shortcuts import render
from django.views import View

class Home(View):
    def get(self, request):
        try:
            print("---in try")
            if request.session["registered"]:
                response = render(request, 'home.html')
                request.session["registered"] = False
                return response
            else:
                return render(request, 'home.html')
        except:
            print("---in except")
            return render(request, 'home.html')