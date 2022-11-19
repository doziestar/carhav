from django.contrib import admin
from carhav.core.models import Interview, Post, Course, Team, BootcampModel, UserCourseApplicationModel, UserInterviewSchedule
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("description",)
    list_display = ("title", "created", "modified")
    search_fields = ("title", "description")
    list_filter = ("created", "modified")


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    summernote_fields = ("description", "final_outcome", "project_goals")
    list_display = ("title", "created", "modified")
    search_fields = ("title", "description")
    list_filter = ("created", "modified")


@admin.register(Team)
class TeamAdmin(SummernoteModelAdmin):
    summernote_fields = ("description")
    list_display = ("title", "created", "modified")
    search_fields = ("title", "description")
    list_filter = ("created", "modified")


@admin.register(BootcampModel)
class BootcampAdmin(SummernoteModelAdmin):
    summernote_fields = ("description",)
    list_display = ("title", "created", "modified")
    search_fields = ("title", "description")
    list_filter = ("created", "modified")
    
@admin.register(UserCourseApplicationModel)
class UserCourseApplicationAdmin(SummernoteModelAdmin):
    # summernote_fields = ("name", "course", "email", "phone")
    list_display = ("name","created", "modified")
    search_fields = ("name", "email", "phone")
    list_filter = ("created", "modified")
    # make all fields readonly
    readonly_fields = [f.name for f in UserCourseApplicationModel._meta.fields]
    
    
@admin.register(UserInterviewSchedule)
class UserCourseApplicationAdmin(SummernoteModelAdmin):
    # summernote_fields = ("name", "course", "email", "phone")
    list_display = ("name","created", "modified")
    search_fields = ("name", "email", "phone")
    list_filter = ("created", "modified")
    # make all fields readonly
    readonly_fields = [f.name for f in UserInterviewSchedule._meta.fields]
    
    
@admin.register(Interview)
class UserCourseApplicationAdmin(SummernoteModelAdmin):
    summernote_fields = ("description")
    list_display = ("title","created", "modified")
    search_fields = ("name", "email", "phone")
    list_filter = ("created", "modified")
