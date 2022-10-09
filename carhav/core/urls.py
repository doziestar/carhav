from django.urls import path

from carhav.core.views import About, Contact, HomePage, PostDetail, PostList, Services

app_name = "core"

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("about/", About.as_view(), name="about"),
    path("services/", Services.as_view(), name="services"),
    path("contact/", Contact.as_view(), name="contact"),
    path("posts/", PostList.as_view(), name="post_list"),
    path("posts/<str:slug>/", PostDetail.as_view(), name="post_detail"),
]
