from django.views.generic import TemplateView, ListView, DetailView

from carhav.core.models import Post


class HomePage(ListView):
    template_name = "core/home.html"
    context_object_name = "all_posts_list"

    def get_queryset(self):
        return Post.objects.all()


class About(TemplateView):
    template_name = "core/about.html"


class PostDetail(DetailView):
    model = Post
    template_name = "core/post_detail.html"


class PostList(ListView):
    model = Post
    template_name = "core/post_list.html"
    context_object_name = "all_posts_list"

    def get_queryset(self):
        return Post.objects.all()


class Services(TemplateView):
    template_name = "core/services.html"


class Contact(TemplateView):
    template_name = "core/contact.html"
