from django.shortcuts import render
from django.http import HttpResponse

def set_language(request):
    user_language = request.GET.get('language', 'spanish')  # Default to English
    response = HttpResponse("Preferred language set: " + user_language)
    response.set_cookie('user_language', user_language)
    return response

def get_language(request):
    user_language = request.COOKIES.get('user_language', 'en')  # Default to English
    context = {'user_language': user_language}
    return render(request, 'preferences/get_language.html', context)
