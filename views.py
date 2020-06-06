from django.http import HttpResponse
from django.shortcuts import render
from . import weather
def index(request):
    html = ''
    if request.method == 'POST':
        query = request.POST['query']
        answer = weather.weather_get(query)
        html = f'<mark>{answer}</mark>'
    context = {
        'response': html,
        'where': request.path
    }
    return render(request, 'index.html', context)
