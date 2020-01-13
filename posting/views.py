from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def index(request):

    postings = Post.objects.order_by('-created_date')
    return render(request, 'posting.html', {'postings': postings})


def new(request):
    if request.user:
        return redirect('/admin')

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('postings', id=post.pk)
    else:
        form = PostForm()

    return render(request, 'form_post.html', {'form': form})    

def detail(request, id):

    post = Post.objects.get(pk=id)
    return render(request, 'detail_post.html', { 'post': post})  