from django.shortcuts import render

# Create your views here.
def order_home(request):
  return render(request, 'orderhome.html')
