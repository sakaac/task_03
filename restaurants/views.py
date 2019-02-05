from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {

    "my_list":[{"restaurant_name": "kofe", "food_type":"coffee" },
    {"restaurant_name": "Mcdonalds", "food_type": "junkfood"},
    {"restaurant_name": "JOA", "food_type": "sushi"}]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {

    "my_object": 
    {"restaurant_name": "JOA", "food_type": "sushi"}



    }
    return render(request, 'detail.html', context)
