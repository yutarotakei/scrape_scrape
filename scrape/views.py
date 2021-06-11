from django.shortcuts import render
from django.views import generic
import requests
from bs4 import BeautifulSoup


# Create your views here.


class ScrapeView(generic.TemplateView):
    template_name = 'index.html'


def waittime_land(request):
    url = 'https://tokyodisneyresort.info/realtime.php?park=land'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    attraction = []
    wait_time = []
    for attraction_temp in soup.find_all(class_="realtime-attr-name"):
        attraction.append(attraction_temp.text.strip())

    for wait_time_temp in soup.find_all(class_="realtime-attr-condition"):
        wait_time_treat = wait_time_temp.text.split("分")[0].strip()
        if wait_time_treat.isdecimal():
            wait_time_treat += "分"

        wait_time.append(wait_time_treat)

    temp_list = []
    for i, _ in enumerate(attraction):
        temp_list.append({
            'attraction': attraction[i],
            'wait_time': wait_time[i],
        })
    params = {'templist': temp_list, }

    return render(request, 'land.html', params)


def waittime_sea(request):
    url = 'https://tokyodisneyresort.info/realtime.php?park=sea'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    attraction = []
    wait_time = []
    for attraction_temp in soup.find_all(class_="realtime-attr-name"):
        attraction.append(attraction_temp.text.strip())

    for wait_time_temp in soup.find_all(class_="realtime-attr-condition"):
        wait_time_treat = wait_time_temp.text.split("分")[0].strip()
        if wait_time_treat.isdecimal():
            wait_time_treat += "分"

        wait_time.append(wait_time_treat)

    temp_list = []
    for i, _ in enumerate(attraction):
        temp_list.append({
            'attraction': attraction[i],
            'wait_time': wait_time[i],
        })
    params = {'templist': temp_list, }

    return render(request, 'sea.html', params)

