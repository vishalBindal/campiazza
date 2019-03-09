from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1> Head over to <a href='/shop'>Shop</a> for all the goodness</h1>")

