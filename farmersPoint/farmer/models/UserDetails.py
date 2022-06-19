import email
from pyexpat import model
from django.db import models

class UserDetails(models.Model):
    name = models.CharField(null = True, max_length=50)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)

    def register(self):
        self.save()

    def account_exists(self, email):
        if UserDetails.objects.filter(email = email):
            return True
        
        return False

    @staticmethod
    def get_userDetalils_by_email(email):
        try:
            return UserDetails.objects.get(email = email)
        except:
            return False