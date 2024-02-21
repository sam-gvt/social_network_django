from django.shortcuts import render
from .forms import PostCreateForm


def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(data=request.POST)

        if form.is_valid():
            form.save(commit)