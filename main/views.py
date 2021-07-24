from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.models import Restaurant
import random


# Create your views here.

def get_store(info_dict):
    store_list = []
    for store in Restaurant.objects.all():
        if info_dict['money'] == 'scrooge' and store.price > 12000:
            continue
        elif info_dict['money'] == 'yolo' and store.price < 12000:
            continue

        list_who = store.who.split('/')
        if info_dict['who'] not in list_who:
            continue
        if info_dict['drink'] != str(store.drink):
            continue
        if info_dict['emotion'] != str(store.emotion):
            continue

        store_list.append(store)

    if len(store_list) == 0:
        for store in Restaurant.objects.all():
            if info_dict['money'] == 'scrooge' and store.price > 12000:
                continue
            elif info_dict['money'] == 'yolo' and store.price < 12000:
                continue

            list_who = store.who.split('/')
            if info_dict['who'] not in list_who:
                continue
            if info_dict['emotion'] != str(store.emotion):
                continue

    answer = store_list[random.randrange(0, len(store_list))]
    return answer


def vote(request):
    try:
        emotion = request.GET['emotion']
        drink = request.GET['drink']
        who = request.GET['who']
        money = request.GET['money']
        info_dict = {'emotion': emotion, 'drink': drink, 'who': who, 'money': money}
        store = get_store(info_dict)
    except (KeyError):
        print("ERROR")
    else:
        return HttpResponseRedirect(reverse('result', args=(store.name,)))

    return render(request, 'test.html')


def main(request):
    return render(request, 'main.html')


def result(request, store_name):
    try:
        store = get_object_or_404(Restaurant, pk=store_name)
    except (KeyError):
        print('ERROR')
        return render(request, 'result.html')
    else:
        return render(request, 'result.html', {'store': store})