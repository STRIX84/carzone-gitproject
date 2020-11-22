from django.shortcuts import render

def home(requet):
    return render(request, 'pages/home.html')
