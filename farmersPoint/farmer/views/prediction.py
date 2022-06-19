from django.shortcuts import render
from django.views import View

class Prediction(View):
    def get(self, request):
        request.session["redirect_page"] = "prediction"
        try:
            if len(request.session['email']) > 1:
                return render(request, 'prediction.html')
        except:
            return render(request, 'login.html', {"not_logged_in": True})
    
