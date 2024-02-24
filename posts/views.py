from django.shortcuts import render
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from .models import Post, Chat
from users.models import Profile



@login_required
def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()

    else:
        form = PostCreateForm(data=request.GET)
        
    return render(request, 'posts/create.html', {'form':form})


@login_required
def posts_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts.html', {'posts':posts})

@login_required
def post_detail(request, id):
    post = Post.objects.get(id = id)
    return render(request, 'posts/post_detail.html', {'post':post})


@login_required
def chat(request): 
    chats = Chat.objects.all()
    return render(request, 'posts/chat.html', {'chats':chats})


@login_required
def my_posts(request):

    current_user = request.user
    posts = Post.objects.filter(user=current_user)

    return render(request, 'posts/my_posts.html', {'posts':posts})
