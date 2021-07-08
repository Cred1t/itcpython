from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("Hello from homepage!")

def test(request):
    return render(request, "index.html")