from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from django.http import HttpResponse


# Create your views here.
def home(request):
    # return HttpResponse("Hello World !")
    return render(request, 'home.html', {'name': 'Gowrav'})


def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    res = int(val1) + int(val2)
    return render(request, 'result.html', {'result': res})
>>>>>>> addition-of-two-numbers
