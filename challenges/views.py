from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Walk for at least 20 minutes a day!"
    elif month == "february":
        challenge_text = "Learn 200 words of a new language!"
    elif month == "march":
        challenge_text = "Follow a vegetarian diet for the whole month!"
    else:
        challenge_text = "This month is not supported!"
        HttpResponseNotFound(challenge_text)
    return HttpResponse(challenge_text)
