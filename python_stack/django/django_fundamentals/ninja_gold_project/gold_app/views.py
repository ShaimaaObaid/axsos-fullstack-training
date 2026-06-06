from django.shortcuts import render, redirect
import random
from datetime import datetime


def index(request):

    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []

    context = {
        'gold': request.session['gold'],
        'activities': request.session['activities']
    }

    return render(request, 'index.html', context)


def process_money(request):

    if request.method == "POST":

        location = request.POST['location']

        places = {
            'farm': (10, 20),
            'cave': (5, 10),
            'house': (2, 5),
            'quest': (-50, 50)
        }

        low, high = places[location]

        earned = random.randint(low, high)

        request.session['gold'] += earned

        time = datetime.now().strftime("%Y/%m/%d %I:%M %p")

        if earned >= 0:
            activity = {
                'message': f"Earned {earned} gold from the {location}! ({time})",
                'color': 'green'
            }
        else:
            activity = {
                'message': f"Entered a {location} and lost {abs(earned)} gold... Ouch. ({time})",
                'color': 'red'
            }

        activities = request.session['activities']
        activities.insert(0, activity)

        request.session['activities'] = activities

    return redirect('/')