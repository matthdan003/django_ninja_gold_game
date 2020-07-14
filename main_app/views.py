from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime

def index(request):
    if 'gold_count' not in request.session:
        request.session['gold_count'] = 0
        request.session['activities'] = []
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def process_money(request):
    activities = []

    if 'farm' in request.POST:
        random_number = random.randrange(10,21,1)
        request.session['gold_count'] += random_number
        activities.append('<p id="gain">Earned {} golds from the farm! ({})</p>'.format(random_number, strftime("%Y/%m/%d  %I:%M %p")))

    if 'cave' in request.POST:
        random_number = random.randrange(5,11,1)
        request.session['gold_count'] +=  random_number
        activities.append('<p id="gain">Earned {} golds from the cave! ({})</p>'.format(random_number, strftime("%Y/%m/%d  %I:%M %p")))

    if 'house' in request.POST:
        random_number = random.randrange(2,6,1)
        request.session['gold_count'] +=  random_number
        activities.append('<p id="gain">Earned {} golds from the house! ({})</p>'.format(random_number, strftime("%Y/%m/%d  %I:%M %p")))

    if 'casino' in request.POST:
        random_number = random.randrange(-50,51,1)
        if random_number < 0:
            request.session['gold_count'] +=  random_number
            activities.append('<p id="loss">Entered a casino and lost {} golds.. Ouch.. ({})</p>'.format(random_number, strftime("%Y/%m/%d  %I:%M %p")))
        else:
            request.session['gold_count'] +=  random_number
            activities.append('<p id="gain">Entered a casino and gained {} golds! ({})</p>'.format(random_number, strftime("%Y/%m/%d  %I:%M %p")))

    request.session['activities'] += activities
    return redirect('/')

def reset(request):
    del request.session['gold_count']
    del request.session['activities']
    return redirect('/')