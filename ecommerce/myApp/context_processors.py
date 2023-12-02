from myApp.models import BasketShop
from django.contrib.auth.models import User

def myContext(request):
    basketlength=0
    
    if request.user.is_authenticated:
        basketlength = len(BasketShop.objects.filter(user=request.user))
    
    return {'basketlength':basketlength}    