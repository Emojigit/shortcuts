from django.shortcuts import render, redirect
from django.http import HttpResponse
import main.models as models
import json

# Create your views here.

def shortcuts(request, shortcut: str):
    try:
        item = models.shortcut.objects.get(shortcut_key = shortcut)
    except:
        return HttpResponse("Not found, visit api/list to get list of shortcuts.\nRequested shortcut key: {}".format(shortcut), content_type="text/plain", status=404)
    target = item.shortcut_value
    item.shortcut_accesses = item.shortcut_accesses + 1
    item.save()
    return redirect(target)

def api_list(request):
    items = models.shortcut.objects.all()
    items_dict = {}
    for x in items:
        items_dict[x.shortcut_key] = x.shortcut_value
    return HttpResponse(json.dumps(items_dict), content_type="application/json")

def api_stat(request, item: str):
    try:
        item = models.shortcut.objects.get(shortcut_key = item)
    except:
        try:
            item = models.shortcut.objects.get(shortcut_value = item)
        except:
            return HttpResponse("Not found, visit api/list to get list of shortcuts.\nRequested shortcut key or value: {}".format(item), content_type="text/plain", status=404)
    respond = {
        "shortcut_key": item.shortcut_key,
        "shortcut_value": item.shortcut_value,
        "shortcut_accesses": item.shortcut_accesses
    }
    return HttpResponse(json.dumps(respond), content_type="application/json")

def home(request):
    return HttpResponse("Welcome to shortcuts\nList of shortcuts: api/list\nShortcut usage: api/stat/<key or target>", content_type="text/plain")
