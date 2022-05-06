from django.shortcuts import render, redirect
from django.http import HttpResponse
import main.models as models
import json

# Create your views here.

def shortcuts(request, shortcut: str):
    try:
        item = models.shortcuts.objects.get(shortcut_key = shortcut)
    except:
        return HttpResponse("Not found, visit api/list to get list of shortcuts.\nRequested shortcut key: {}".format(shortcut), content_type="text/plain", status=404)
    target = item.shortcut_value
    item.shortcut_usage = item.shortcut_usage + 1
    item.save()
    return redirect(target)

def api_list(request, method: str):
    items = models.shortcuts.objects.all()
    items_dict = {}
    for x in items:
        items_dict[x.shortcut_key] = x.shortcut_value
    return HttpResponse(json.dumps(items_dict), content_type="application/json")

def home(request):
    return HttpResponse("Welcome to shortcuts\nList of shortcuts: api/list", content_type="text/plain")
