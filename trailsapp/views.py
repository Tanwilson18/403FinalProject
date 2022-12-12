#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from trailsapp.models import trails
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.


def indexPageView(request):
    return render(request, 'trailsapp/index.html')


def createPageView(request):
    if request.method == "POST":
        trail = trails()
        trail.trail_name = request.POST['trail_name']
        trail.length_miles = request.POST['length_miles']
        trail.difficulty = request.POST['difficulty']
        trail.completion_time = request.POST['completion_time']
        trail.img_url = request.POST['img_url']
        trail.description = request.POST['description']
        trail.location = request.POST['location']

        trail.save()

        return showTrailsPageView(request)
    else:
        return render(request, 'trailsapp/create.html')


def showTrailsPageView(request):
    data = trails.objects.all()

    context = {
        "traillist": data
    }
    return render(request, 'trailsapp/showtrails.html', context)


def mapPageView(request):
    return render(request, 'trailsapp/map.html')


def updatePageView(request):
    trail_id = request.POST.get("trail_id")
    data = trails.objects.get(trail_id=trail_id)
    context = {
        "record": data
    }
    return render(request, 'trailsapp/update.html', context)


def makeUpdatePageView(request):
    trail_ID = request.POST['trail_id']
    trail = trails.objects.get(trail_id=trail_ID)
    trail.trail_id = request.POST['trail_id']
    trail.trail_name = request.POST['trail_name']
    trail.length_miles = request.POST['length_miles']
    trail.difficulty = request.POST['difficulty']
    trail.completion_time = request.POST['completion_time']
    trail.img_url = request.POST['img_url']
    trail.description = request.POST['description']
    trail.location = request.POST['location']
    trail.save()

    data = trails.objects.all()

    context = {
        "traillist": data
    }
    return render(request, 'trailsapp/showtrails.html', context)


def deleteTrailPageView(request, trail_id):
    data = trails.objects.get(trail_id=trail_id)

    data.delete()

    return showTrailsPageView(request)


def viewOneTrailView(request, trail_id):
    data = trails.objects.get(trail_id=trail_id)
    context = {
        "trail": data
    }
    return render(request, 'trailsapp/viewtrail.html', context)

# login pages


def loginPageView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                # once logged in automatically redirects
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login.html', context={"login_form": form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, 'register.html', context={"register_form": form})


def logout_request(request):
    messages.info(request, "You have successfully logged out.")
    logout(request)
    return render(request, 'logout.html')
