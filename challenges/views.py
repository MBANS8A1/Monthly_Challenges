from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
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


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = """
        <ul>
          <li><a href="challenges/january">January</a></li>
        </ul>
    """
    return HttpResponse()


def monthly_challenge_by_number(request, month):
    # A list of month names
    named_months = list(monthly_challenges.keys())
    if month > len(named_months):
        return HttpResponseNotFound("Invalid month")
    # Subtract 1 becauses lists are zero-indexed
    redirect_month = named_months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
