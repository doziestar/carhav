from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from carhav.core.models import (
    Interview,
    Post,
    Course,
    Team,
    BootcampModel,
    UserCourseApplicationModel,
    UserInterviewSchedule
)

from carhav.core.form import BootcampForm, SpecializeCourseForm, UserInterviewScheduleForm


class HomePage(ListView):
    template_name = "core/home.html"
    context_object_name = "all_posts_list"

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teams"] = Team.objects.all()
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
    context_object_name: str = "post"


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
    context_object_name = "bootcamp"


class SpecializeTraining(ListView):
    template_name = "core/training.html"
    model = Course
    context_object_name = "courses_list"
    paginate_by: int = 4


class SpecializeTrainingDetails(DetailView):
    model = Course
    template_name = "core/training_details.html"
    context_object_name: str = "training"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SpecializeCourseForm()
        return context


class BootcampDetails(DetailView):
    model = BootcampModel
    template_name = "core/bootcamp-details.html"
    context_object_name: str = "boot"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BootcampForm()
        return context


class TeamDetail(DetailView):
    model = Team
    template_name = "core/team_detail.html"
    context_object_name: str = "team"


class UserCourseApplicationView(CreateView):
    template_name = "core/training_details.html"
    model = UserCourseApplicationModel
    form_class: SpecializeCourseForm = SpecializeCourseForm 
    # success_url = reverse_lazy("core:training")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # redirect to payment page
    # stripe payment link is on the course model
    def get_success_url(self):
        # get the course id from the form
        course_id = self.request.POST.get("course")
        # get the course object
        course = Course.objects.get(id=course_id)
        # get the course payment link
        payment_link = course.payment_link
        return payment_link
    
class UserBootCampApplicationView(CreateView):
    template_name = "core/bootcamp-details.html"
    model = UserCourseApplicationModel
    form_class: BootcampForm = BootcampForm 
    # success_url = reverse_lazy("core:training")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # redirect to payment page
    # stripe payment link is on the course model
    def get_success_url(self):
        # get the course id from the form
        bootcamp_id = self.request.POST.get("bootCamp")
        # get the course object
        bootcamp = BootcampModel.objects.get(id=bootcamp_id)
        # get the course payment link
        payment_link = bootcamp.payment_link
        return payment_link
    
    
class UserInterviewScheduleView(CreateView):
    template_name = "core/interview_details.html"
    model = UserInterviewSchedule
    form_class: UserInterviewScheduleForm = UserInterviewScheduleForm
    # success_url = reverse_lazy("core:training")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors)
        # re render the page that the user is on
        link = self.request.path
        return redirect(link)

    # redirect to payment page
    # stripe payment link is on the course model
    def get_success_url(self):
        # get the course id from the form
        interview_id = self.request.POST.get("preparation_type")
        # get the course object
        interview = Interview.objects.get(id=interview_id)
        # get the course payment link
        payment_link = interview.payment_link
        return payment_link
    

class InterviewDetailView(DetailView):
    model = Interview
    template_name = "core/interview_details.html"
    context_object_name: str = "interview"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = UserInterviewScheduleForm()
        return context