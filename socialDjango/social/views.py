from django.shortcuts import render

# Create your views here.
def socialHomeView(request):
    return render(request, 'index.html')