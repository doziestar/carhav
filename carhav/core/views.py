from django.views.generic import TemplateView, ListView, DetailView

from carhav.core.models import Post, Course, Team, BootcampModel


class HomePage(ListView):
    template_name = "core/home.html"
    context_object_name = "all_posts_list"

    def get_queryset(self):
        return Post.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all()
        return context


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
    
class Bootcamp(ListView):
    template_name = "core/bootcamps.html"
    paginate_by = 4
    model: BootcampModel = BootcampModel
    context_object_name = "bootcamps"

class SpecializeTraining(ListView):
    template_name = "core/training.html"
    model = Course
    context_object_name = "courses_list"
    paginate_by: int = 4
    
class SpecializeTrainingDetails(DetailView):
    model = Course
    template_name = "core/training-details.html"
    context_object_name: str = "course"
    
class BootcampDetails(DetailView):
    model = BootcampModel
    template_name = "core/bootcamp-details.html"
    context_object_name: str = "bootcamp"
    

class TeamDetail(DetailView):
    model = Team
    template_name = "core/team_detail.html"
    context_object_name: str = "team"