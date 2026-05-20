from django.shortcuts import render
from time import gmtime, strftime
# Create your views here.
def index(request):
    current_time = strftime("%b %d, %Y %I:%M %p", gmtime())

    return render(request, 'index.html', {
        "time": current_time
    })