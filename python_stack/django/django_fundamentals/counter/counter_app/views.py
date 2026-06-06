from django.shortcuts import render, redirect

def index(request):

    if 'visits' not in request.session:
        request.session['visits'] = 0

    if 'counter' not in request.session:
        request.session['counter'] = 0

    # زيادة زيارة الصفحة
    request.session['visits'] += 1

    context = {
        'visits': request.session['visits'],
        'counter': request.session['counter']
    }

    return render(request, 'index.html', context)


def destroy_session(request):
    request.session.flush()  # يمسح كل session
    return redirect('/')


def add_two(request):
    if 'counter' in request.session:
        request.session['counter'] += 2
    return redirect('/')


def set_increment(request):
    if request.method == 'POST':
        value = int(request.POST.get('increment', 1))
        request.session['counter'] += value
    return redirect('/')