from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from . import util
import random
from markdown2 import Markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(), "f":True
    })
def get_page(request, title):
    if util.get_entry(title):
        markdowner = Markdown()
        content = markdowner.convert(util.get_entry(title))
        return render(request, "encyclopedia/entry.html", {"content": content, "title":title})
    else:
        return render(request, "encyclopedia/error.html", {"title":title})
def get_random(request):
    index = random.randint(0,len(util.list_entries())-1)
    title = util.list_entries()[index]
    markdowner = Markdown()
    content = markdowner.convert(util.get_entry(title))
    return render(request, "encyclopedia/entry.html", {"content": content, "title":title})
def newpage(request):
    return render(request, "encyclopedia/newpage.html", {"error":False})
def search(request):
    title = request.POST.get('q')
    if util.get_entry(title):
        markdowner = Markdown()
        content = markdowner.convert(util.get_entry(title))
        return render(request, "encyclopedia/entry.html", {"content": content, "title":title})
    else:
        valid_entries = []
        for entry in util.list_entries():
            if title.lower() in entry.lower():
                valid_entries.append(entry)
        if not valid_entries:
            return render(request, "encyclopedia/error.html", {"title":title})
        else:
            return render(request, "encyclopedia/index.html", {
        "entries": valid_entries, "f":False, "q":title
    })
def add(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    if not content or not title:
        return render(request, "encyclopedia/newpage.html", {"empty":True, "error":True})
    elif util.get_entry(title):
        return render(request, "encyclopedia/newpage.html", {"empty":False, "error":True})
    else:
        util.save_entry(title, content)
        markdowner = Markdown()
        content = markdowner.convert(util.get_entry(title))
        return render(request, "encyclopedia/entry.html", {"content": content, "title":title})
def edit(request):
    title = request.POST.get('title')
    return render(request, "encyclopedia/edit.html", {"title":title, "content":util.get_entry(title)})
def save_edit(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    util.save_entry(title, content)
    markdowner = Markdown()
    content = markdowner.convert(util.get_entry(title))
    return render(request, "encyclopedia/entry.html", {"content": content, "title":title})