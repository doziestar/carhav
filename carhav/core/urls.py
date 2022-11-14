from django.urls import path
from django.views.generic import TemplateView

from carhav.core.views import (
    About,
    Contact,
    HomePage,
    PostDetail,
    PostList,
    Services,
    Appointment,
    Partners,
    InterviewPrep,
    ResumeRevamp,
    Bootcamp,
    SpecializeTraining
)

app_name = "core"

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("about/", About.as_view(), name="about"),
    path("appointment/", Appointment.as_view(), name="appointment"),
    path("partners/", Partners.as_view(), name="partners"),
    path("services/", Services.as_view(), name="services"),
    path("contact/", Contact.as_view(), name="contact"),
    path("posts/", PostList.as_view(), name="post_list"),
    path("posts/<str:slug>/", PostDetail.as_view(), name="post_detail"),
    path("resume/", ResumeRevamp.as_view(), name="resume"),
    path("interview_prep/", InterviewPrep.as_view(), name="interview_prep"),
    path("ecba/", TemplateView.as_view(template_name="core/ecba.html"), name="ecba"),
    path("ccba/", TemplateView.as_view(template_name="core/ccba.html"), name="ccba"),
    path("cbap/", TemplateView.as_view(template_name="core/cbap.html"), name="cbap"),
    path("cca/", TemplateView.as_view(template_name="core/cca.html"), name="cca"),
    path("cbda/", TemplateView.as_view(template_name="core/cbda.html"), name="cbda"),
    path("aac/", TemplateView.as_view(template_name="core/aac.html"), name="aac"),
    path("careers/", TemplateView.as_view(template_name="core/careers.html"), name="careers"),
    path("bootcamp/", Bootcamp.as_view(), name="bootcamp"),
    path("training/", SpecializeTraining.as_view(), name="training"),
]
