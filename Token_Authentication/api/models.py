from django.db import models

class Studnet(models.Model):
    name = models.CharField(max_length = 50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# This singnal creates Auth Token for users
@receiver(post_save, sender=settings.AUTH_USER_MODEl)
def create_auth_token(sender, instance=None, Created=False, **kwargs):
    if Created:
        Token.objects.create(user=instance)
