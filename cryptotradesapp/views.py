from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

class Crypto:
    def __init__(self, name, price):
        self.name = name
        self.price = price

cryptos = [
    Crypto("Ethereum", 4450),
    Crypto("Bitcoin", 66789),
    Crypto("Dogecoin", 25.55),
    Crypto("ChainLink", 35.50)
]

def home(request):
    return render(request, 'home.html')

def crypto_index(request):
    return render(request, 'cryptos/cryptos.html', { "cryptos": cryptos })

def about(request):
    return HttpResponse("<h1>About Page</h1>")





# Create your views here.
