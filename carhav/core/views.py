from django.views.generic import TemplateView, ListView, DetailView

from carhav.core.models import Post


class HomePage(ListView):
    template_name = "core/home.html"
    context_object_name = "all_posts_list"

    def get_queryset(self):
        return Post.objects.all()


class About(TemplateView):
    template_name = "core/about.html"
    
class Appointment(TemplateView):
    template_name = "core/appointment.html"
    

class ResumeRevamp(TemplateView):
    template_name = "core/resume.html"
    
    
class InterviewPrep(TemplateView):
    template_name = "core/interview_prep.html"
    
    
class Partners(TemplateView):
    template_name = "core/partners.html"


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
    
class Bootcamp(TemplateView):
    template_name = "core/bootcamps.html"
