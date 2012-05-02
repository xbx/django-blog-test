from blog.models import Post
from django.shortcuts import render_to_response

def index(request):
    latest_posts_list = Post.objects.all()
    return render_to_response('index.html', \
                              {'latest_posts_list': latest_posts_list})

