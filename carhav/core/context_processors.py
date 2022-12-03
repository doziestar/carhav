from carhav.core.models import Interview, BootcampModel, Post

def get_interviews(request):
    interviews = Interview.objects.all()
    return {"interviews": interviews}

def get_bootcamps(request):
    bootcamps = BootcampModel.objects.all()
    return {"bootcamp": bootcamps}

def get_posts(request):
    posts = Post.objects.all()
    return {"posts": posts}