from django.shortcuts import render
import random


def cat(request):
    cat_state = {
        "name":  request.POST.get('name', ''),
        "age": 4,
        "satiety_level": 50,
        "happiness_level": 50,
        "state": "awake",
    }
    action = None
    if request.method == "POST":
        action = request.POST.get('action')

    if action == "feed":
        if cat_state["state"] == "sleeping":
            pass
        else:
            cat_state["satiety_level"] += 15
            cat_state["happiness_level"] += 5
            if cat_state["satiety_level"] > 100:
                cat_state["happiness_level"] -= 30
    elif action == "play":
        if cat_state["state"] == "sleeping":
            cat_state["state"] = "awake"
            cat_state["happiness_level"] -= 5
        else:
            cat_state["happiness_level"] += 15
            cat_state["satiety_level"] -= 10
            if random.randint(1, 3) == 1:
                cat_state["happiness_level"] = 0
    elif action == "sleep":
        cat_state["state"] = "sleeping"
        cat_state["name"] = request.POST.get('name', cat_state["name"])
        cat_state["age"] = request.POST.get('age', cat_state["age"])
        cat_state["satiety_level"] = request.POST.get('satiety_level', cat_state["satiety_level"])
        cat_state["happiness_level"] = request.POST.get('happiness_level', cat_state["happiness_level"])
        cat_state["state"] = request.POST.get('state', cat_state["state"])
    context = {
        "cat_state": cat_state,
    }
    return render(request, "cat.html", context=context)
