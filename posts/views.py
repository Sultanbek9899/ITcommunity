from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

from posts.models import Post


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

