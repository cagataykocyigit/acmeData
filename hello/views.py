import json

from django.http import HttpResponse, response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from hello.models import Talents
from hello.serializers import TalentSerializer


import requests


# Create your views here.
def index(request):
    return HttpResponse("Hello World!")


query_keyword = ""
url_code = "https://api.github.com/search/code?q=android in:file)"
url_topics = "https://api.github.com/search/topics?q=full stack developer in:name,description"
url_repo = "https://api.github.com/search/repositories?q=topic:aoc-2021-in-kotlin"


def home(request):
    global query_keyword
    url_user = "https://api.github.com/search/users?q="
    query_url = f"{url_user}{query_keyword}"
    response = requests.get(query_url,headers={'Authorization':'login'})
    talents = response.json()

    return HttpResponse(query_keyword)


def form(request):
    return render(request, 'form.html')


def display(request):
    global query_keyword
    keyword_input = request.POST.get("a1")
    message = "KeyWord is =" + keyword_input
    query_keyword = keyword_input.replace(" ", "+")

    url_user = 'https://api.github.com/search/users?q='
    query_url = f"{url_user}{query_keyword}"
    context = requests.get(query_url)
    final_result = []
    output = json.loads(context.text)
    org_id = int(request.GET.get('org'))
    for todo in output:
        if (todo['id'] == org_id):
            content = requests.get(todo['repos_url'] + '?sort=stargazers_count&direction=desc')
    result = json.loads(content.text)
    for test in result:
        value = json.dumps({
            "name": test['name'],
            "stars": test['stargazers_count']
        }, sort_keys=True, indent=4)
        final_result.append(value)

    return HttpResponse((final_result))



