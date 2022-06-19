from django.shortcuts import render, redirect
from django.views import View
import requests

class Prediction_With_Id(View):
    def post(self, request, f_mail):
        # response = requests.get(f"https://cd8b-34-123-179-230.ngrok.io/output/{f_mail}")
        # print("-----response", response.json())
        # print("-------fmail", f_mail)
        return redirect('prediction')