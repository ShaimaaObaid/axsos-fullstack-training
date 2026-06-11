from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

# Create your views here.
def redirect_root(request):
    return redirect('/shows')


def shows(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'all_shows.html', context)


def new_show(request):
    return render(request, 'new_show.html')



def create_show(request):
    if request.method == "POST":
        errors = Show.objects.validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')

        Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST.get('description', '')
        )

        return redirect('/shows')

    return redirect('/shows/new')


def show_details(request, id):

    context = {
        'show': Show.objects.get(id=id)
    }

    return render(request, 'show_details.html', context)


def edit_show(request, id):

    context = {
        'show': Show.objects.get(id=id)
    }

    return render(request, 'edit_show.html', context)


def update_show(request, id): # Changed show_id to id
    show = Show.objects.get(id=id)

    if request.method == "POST":
        # Pass id to your model validator
        errors = Show.objects.validator(request.POST, show_id=id)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{id}/edit')

        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST.get('description', '')
        show.save()

        return redirect(f'/shows/{id}')

    return redirect('/shows')
def delete_show(request, id):

    show = Show.objects.get(id=id)
    show.delete()

    return redirect('/shows')