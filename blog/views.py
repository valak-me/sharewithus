from django.shortcuts import render
from .models import post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)

def index(request):
    context={'key':post.objects.all()}
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'site'})

class PostListView(ListView):
    model=post
    template_name='blog/index.html'
    context_object_name='key'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model=post

class PostCreateView(LoginRequiredMixin, CreateView):
    model=post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=post
    success_url = '/blog/'
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

