from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



# Create your views here.

def home(request):
        # 'posts': posts,
    context_dict={
        'posts': Post.objects.all(),
        'title': 'rob-title'
    }
    return render(request, 'blog/home.html', context_dict)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] #ordering the posts by date posted in descending order.

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    #Override form_valid() method 
    def form_valid(self, form):
        form.instance.author = self.request.user    # Set the author on the form
        return super().form_valid(form)             # Validate form by running form_valid method from parent class.
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    #Override form_valid() method 
    def form_valid(self, form):
        form.instance.author = self.request.user    # Set the author on the form
        return super().form_valid(form)             # Validate form by running form_valid method from parent class.
    
      #Added 'test_func':  check the request to .../update is from the post.author 
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False