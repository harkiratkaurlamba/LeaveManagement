from django.shortcuts import render
from django.http import HttpResponse
from todolist.models import todayOnLeave

# Create your views here.
def todolist(request):

    team_mates = todayOnLeave.objects.all
    return render(request, 'todolist.html', {'team_mates':team_mates} )

def applyleave(request):

    context = {"Apply_leaves_text":"applyleave"}
    return render(request, 'applyleave.html', context )

def companycalendar(request):

    context = {"company_calendar_text":"companycalendar table goes here"}
    return render(request, 'companycalendar.html', context )