from django.shortcuts import render
from .models import Post

# Vista per la homepage
def home(request):
    return render(request, 'home.html')

# Vista per la lista dei post
def post_list(request):
    posts = Post.objects.all()  
    return render(request, 'blog/post_list.html', {'posts': posts})

# Vista per la pagina Destinazioni
def destinazioni(request):
    return render(request, 'blog/destinazioni.html')


