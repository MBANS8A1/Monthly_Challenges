from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

monthly_challenges = {
    "january": "Walk for at least 20 minutes a day!",
    "february": "Learn 200 words of a new language!",
    "march": "Follow a vegetarian diet for the whole month!",
    "april": "Learn Django for 20 minutes a day!",
    "may": "Take up a new hobby!",
    "june": "Take up jogging every two days in the mornings!",
    "july": "Take a trip to another part of the country for the weekend!",
    "august": "Learn how to drive a motorcycle!",
    "september": "Create a discord channel for Python programming!",
    "october": "Create a social media account for you programming work!",
    "november": "Read a new novel from your favourite genre!",
    "december": "Cook something else for Christmas other than turkey!"
}


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
