from django.shortcuts import render

# Create your views here.


def product_home(request):
  return render(request, 'producthome.html')
