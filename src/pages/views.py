from django.shortcuts import render

# Create your views here.
def home_view(request):
  return render(request, 'pages/home.html', { 'title': 'Home page' })

def about_view(request, *args, **kwargs):
  return render(request,'pages/about.html', { 'title': 'About page' })