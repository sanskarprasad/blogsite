from django.shortcuts import render

posts = [
    {
        'author':'Sanskar P',
        'title': 'Blog Post 1',
        'date_posted':'August 27, 2018'
    },
    {
        'author':'shubh',
        'title': 'Blog Post 2',
        'date_posted':'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})