from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    data = [
        {'name': 'Erica', 'age': 23},
        {'name': 'Paul', 'age': 22},
        {'name': 'Maxx', 'age': 39},
        {'name': 'Robert', 'age': 12},
        {'name': 'Mexina', 'age': 21}
    ]

    text = 'Text Generated!!'

    listof = ['Erica','Paul', 'Maxx', 'Robert', 'Mexina']

    context = {'peoples': data, 'text': text, "listof": listof, 'page': 'Home Page'}

    return render(request, "index.html", context)

def contact(request):
    context = {'page': 'Contact'}
    return render(request, "contact.html", context)

def about(request):
    context = {'page': 'about'}
    return render(request, "about.html", context)

def success_page(request):
    context = {'page': 'Success Page'}
    return HttpResponse('<h1>This is first Success page!!</h1>', context)