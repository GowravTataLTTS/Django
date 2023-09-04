from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html', {'street': 123, 'email': 'gowrav', 'domain': 'ltts'})
