from django.contrib import admin
from carhav.core.models import Post, Course, Team
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ('title', 'created', 'modified')
    search_fields = ('title', 'description')
    list_filter = ('created', 'modified')
    
@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ('title', 'created', 'modified')
    search_fields = ('title', 'description')
    list_filter = ('created', 'modified')
    
@admin.register(Team)
class TeamAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ('title', 'created', 'modified')
    search_fields = ('title', 'description')
    list_filter = ('created', 'modified')
