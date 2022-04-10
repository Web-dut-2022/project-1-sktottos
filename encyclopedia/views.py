from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
import os
import re
from . import util
from django.urls import reverse
import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def AllPages(request, entry_name):
    content = util.get_entry(entry_name)

    if content is None:
        return render(request, "encyclopedia/Error.html", {
            'content': 'Not Found Entry'
        })
    else:
        return render(request, "encyclopedia/AllPages.html", {
            'entry_name': entry_name,
            'content': markdown2.markdown(content)
        })


def Error(request):
    return render(request, "encyclopedia/Error.html")


def search_item(request):
    if request.method == "POST":
        name = request.POST.get("name")
    filename = os.listdir('entries')
    l = sorted(re.sub(r".md", '', file) for file in filename if file.endswith(".md"))
    list = []
    for file in l:
        if name in file:
            list.append(file)

    if len(list) == 0:
        return render(request, "encyclopedia/Error.html")
    else:
        return render(request, "encyclopedia//index.html", {"entries": list})


def create_new_page(request):
    return render(request, "encyclopedia/create_new_page.html")


def new_entry(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
    if util.get_entry(title) == None:
        util.save_entry(title, content)
        return redirect('/wiki/'+title+'/')

    else:
        return render(request, 'encyclopedia/error.html')