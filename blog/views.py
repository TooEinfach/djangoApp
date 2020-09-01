from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

# post = [
#     {
#         'author': 'Nick',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_post': 'August 30, 2020'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_post': 'September 1, 2020'
#     }
# ]

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})