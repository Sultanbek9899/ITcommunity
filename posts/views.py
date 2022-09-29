from django.urls import reverse
from django.forms import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView, 
    DetailView,
    DeleteView,
    UpdateView
)

# Create your views here.

from posts.models import Post
from posts.forms import PostCreateForm, PostUpdateForm

# def index_page(request):
#     name = "Aitegin"
#     products = ["Orange", "Bread", "Milk", "Melon"]
#     is_admin = True
#     context = {"name":name, "products":products, "is_admin":is_admin}
#     return render(request, 'index.html', context=context)

# Есть два вида создание логики в django. Через классы и через функции.
# Через классы называется Class Based Views - CBV
# Через функции называется Function Based Views - FBV

class IndexPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context


class UserPostsView(ListView):
    template_name = "user_posts.html"
    model = Post


    def get_queryset(self):
        posts = Post.objects.filter(is_archive=False, author=self.request.user)
        return posts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["form"] = PostCreateForm()
        return context


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy("my_posts")


    def form_valid(self, form):
        post=form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)




# class PostDetailView(DetailView):
#     template_name = "post_details.html"
#     model = Post
#     queryset = Post.objects.all()


# def get_post_detail(request, pk):
#     try:
#         post = Post.objects.get(id=pk) # pk - Primary Key
#     except Post.DoesNotExist:
#         return Http404()
#     context = {
#         "post":post
#     }
#     return render(request, "post_details.html", context)


class PostDetailView(DetailView):
    template_name = "post_details.html"
    model = Post
    queryset = Post.objects.filter()
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PostUpdateForm(instance=self.get_object())
        return context


def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect("my_posts")

# class PostDeleteView(DeleteView):
#     model = Post
#     success_url = reverse_lazy("my_posts")



class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    
    def get_success_url(self):
        pk = self.kwargs.get("pk")
        print(self.kwargs)
        return reverse_lazy("post_details", kwargs={"pk":pk})


def archivate_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if not post.is_archive:
        post.is_archive = True
        post.save()
    return redirect(reverse_lazy("post_details", kwargs={"pk":pk}))

def unarchive_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.is_archive:
        post.is_archive = False
        post.save()
    return redirect(reverse_lazy("post_details", kwargs={"pk":pk}))