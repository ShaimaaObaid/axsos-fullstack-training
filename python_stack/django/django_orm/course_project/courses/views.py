from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Course, Description, Comment

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def create_course(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        desc_text = request.POST.get('description', '').strip()
        errors = False

        if len(name) < 6:
            messages.error(request, "Course name must be more than 5 characters.")
            errors = True
        if len(desc_text) < 16:
            messages.error(request, "Description must be more than 15 characters.")
            errors = True

        if errors:
            return redirect('/')

        # Save entries across both related tables
        new_course = Course.objects.create(name=name)
        Description.objects.create(course=new_course, text=desc_text)
        
    return redirect('/')

def destroy(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    # Sensei Bonus: Process via AJAX request
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "POST":
        course.delete()
        return JsonResponse({'status': 'success'})
        
    # Fallback standard routing functionality if JS is disabled
    if request.method == "POST":
        if 'yes' in request.POST:
            course.delete()
        return redirect('/')
        
    return render(request, 'courses/destroy.html', {'course': course})

def comments(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        content = request.POST.get('content', '').strip()
        if content:
            Comment.objects.create(course=course, content=content)
        return redirect(f'/courses/{course_id}/comments')
        
    context = {
        'course': course,
        'comments': course.comments.all()
    }
    return render(request, 'courses/comments.html', context)
