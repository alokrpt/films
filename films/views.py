from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def main(request):
    return render(request, 'films/main.html')
def user_info(request):
    return render(request, 'films/user_info.html')