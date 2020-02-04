from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from project.models import FinalProject
from project.filters import PostFilter
from django.contrib.auth.decorators import login_required


def project(request):
    pros = FinalProject.objects.all()
    filters = PostFilter(request.GET, queryset=pros)
    pros = filters.qs
    context = {
        'pros': pros,
        'filters': filters
    }
    paginate_by = 2
    return render(request, 'project/projects.html', context=context)


class PostListView(ListView):
    model = FinalProject
    template_name = 'project/post.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


class UserPostListView(ListView):
    model = FinalProject
    template_name = 'project/finalproject_list.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return FinalProject.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = FinalProject


class PostCreateView(LoginRequiredMixin, CreateView):
    model = FinalProject
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = FinalProject
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = FinalProject
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
