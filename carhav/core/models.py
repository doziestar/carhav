from datetime import timezone
from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.mail import send_mail


class Post(TimeStampedModel, TitleSlugDescriptionModel):
    """Post model."""

    image = models.ImageField(
        _("post"),
        upload_to="post",
        height_field=None,
        width_field=None,
        max_length=None,
        default="",
    )
    category = models.CharField(_("category"), max_length=255, default="")

    def __str__(self):
        return self.title


class Course(TimeStampedModel, TitleSlugDescriptionModel):
    image = models.ImageField(
        _("course_image"),
        upload_to="courses",
        height_field=None,
        width_field=None,
        max_length=None,
        default="",
    )
    category = models.CharField(_("category"), max_length=100, default="")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    payment_link = models.CharField(_("payment_link"), max_length=255, default="")
    image2 = models.ImageField(
        _("slide image 2"),
        upload_to="courses",
        height_field=None,
        width_field=None,
        max_length=None,
        default="",
    )
    side_image_1 = models.ImageField(
        _("Side Image 1"),
        upload_to="courses",
        height_field=None,
        width_field=None,
        max_length=None,
        default="",
    )
    side_image_2 = models.ImageField(
        _("Side Image 2"),
        upload_to="courses",
        height_field=None,
        width_field=None,
        max_length=None,
        default="",
    )
    graduated = models.IntegerField(_("Graduated_student"), default=0)
    current = models.IntegerField(_("Current_student"), default=0)
    years = models.IntegerField(_("Number_of_years"), default=0)
    skills = models.TextField(_("Skills students will master"), default="")
    trainer = models.CharField(
        _("Trainers"), max_length=255, default="", help_text="separate with comma"
    )
    duration = models.CharField(_("Training duration"), max_length=255, default="")
    trained_by = models.CharField(
        _("Trained by"),
        max_length=255,
        default="",
        help_text="separate with comma e.g. Amazon, CareerHaveen",
    )
    location = models.CharField(
        _("Location"),
        max_length=255,
        default="",
        help_text="separate with comma e.g. Lagos, Abuja, Remote",
    )
    final_outcome = models.TextField(_("Final outcome"), default="")
    youtube_link = models.CharField(
        _("Youtube Link"),
        max_length=255,
        default="",
        help_text="enter a promotional video link",
    )
    project_goals = models.TextField(_("Project Goals"), default="")

    def __str__(self):
        return self.title

    @property
    def excerpt(self):
        return self.description[:100] + "......"


class Interview(TimeStampedModel, TitleSlugDescriptionModel):
    image = models.ImageField(
        _("image"),
        upload_to="courses",
        height_field=None,
        width_field=None,
        max_length=None,
        default="",
    )
    category = models.CharField(_("category"), max_length=100, default="")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    payment_link = models.CharField(_("payment_link"), max_length=255, default="")

    def __str__(self):
        return self.title

    @property
    def excerpt(self):
        return self.description[:100] + "......"


class UserInterviewSchedule(TimeStampedModel):
    name = models.CharField(_("name"), max_length=255, default="")
    email = models.EmailField(_("email"), max_length=255, default="")
    phone = models.CharField(_("phone"), max_length=255, default="")
    preparation_type = models.ForeignKey(Interview, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="resume/", null=True, blank=True, default="")
    date = models.DateField(_("date"), auto_now=False, auto_now_add=False)
    time = models.TimeField(_("time"), auto_now=False, auto_now_add=False)
    country_of_residence = models.CharField(
        _("country_of_residence"), max_length=255, default=""
    )
    city_of_residence = models.CharField(
        _("city_of_residence"), max_length=255, default=""
    )
    message = models.TextField(_("message"), default="")

    def send_email(self):
        message = f"""
        Hello {self.name},
        Your interview preparation has been scheduled for {self.date} at {self.time}.
        Please be online at least 10 minutes before the scheduled time.
        """
        send_mail(
            "Interview Preparation",
            message,
            settings.EMAIL_HOST_USER,
            [self.email],
            fail_silently=False,
        )
        return

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.send_email()
        super().save(*args, **kwargs)


class Team(TimeStampedModel, TitleSlugDescriptionModel):
    image = models.ImageField(
        _("team_image"),
        upload_to="team",
        height_field=None,
        width_field=None,
        max_length=None,
        default="",
    )
    position = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200, default="instagram.com")
    phone = models.CharField(max_length=200, default="")
    email = models.EmailField(max_length=200, default="")

    def __str__(self):
        return self.title


class BootcampModel(TimeStampedModel, TitleSlugDescriptionModel):
    image = models.ImageField(
        _("bootcamp_image"),
        upload_to="bootcamp",
        height_field=None,
        width_field=None,
        max_length=None,
        default="",
    )
    category = models.CharField(_("category"), max_length=100, default="")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    payment_link = models.CharField(_("payment_link"), max_length=255, default="")


class UserCourseApplicationModel(TimeStampedModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    bootCamp = models.ForeignKey(
        BootcampModel, on_delete=models.CASCADE, null=True, blank=True
    )
    time_to_join = models.CharField(max_length=255, default="")
    country_of_residence = models.CharField(max_length=255, default="")
    city_of_residence = models.CharField(max_length=255, default="")
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def send_email(self):
        subject = "Course Application"
        message = f"Hello {self.name}, \n\nThank you for applying for {self.course.title} course. \n\nWe will get back to you shortly."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [
            self.email,
        ]
        send_mail(subject, message, email_from, recipient_list)
        return

    def save(self, **kwargs):
        # check if the user has already applied for the course
        # if UserCourseApplicationModel.objects.filter(email=self.email, course=self.course).exists():
        #     raise Exception("You have already applied for this course")
        # send email to the user
        self.send_email()
        return super().save(**kwargs)
