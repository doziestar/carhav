from datetime import timezone
from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel
from django.utils.translation import ugettext_lazy as _


class Post(TimeStampedModel, TitleSlugDescriptionModel):
    """Post model."""
    image = models.ImageField(_("post"), upload_to="post", height_field=None, width_field=None, max_length=None, default="")
    category = models.CharField(_("category"), max_length=255, default="")
    def __str__(self):
        return self.title

class Course(TimeStampedModel, TitleSlugDescriptionModel):
    image = models.ImageField(_("course_image"), upload_to="courses", height_field=None, width_field=None, max_length=None, default="")
    category = models.CharField(_("category"), max_length=100, default="")
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
    
class Team(TimeStampedModel, TitleSlugDescriptionModel):
    image = models.ImageField(_("team_image"), upload_to="team", height_field=None, width_field=None, max_length=None, default="")
    position = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)

    def __str__(self):
        return self.title