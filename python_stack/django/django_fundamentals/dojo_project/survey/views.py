from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def result(request):
    if request.method == "POST":
        print(request.POST)  
        context = {
            "name": request.POST.get("name"),
            "dojo": request.POST.get("dojo"),
            "language": request.POST.get("language"),
            "comment": request.POST.get("comment"),
        }
        return render(request, "result.html", context)

    return render(request, "result.html")