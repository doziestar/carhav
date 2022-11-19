from carhav.core.models import Interview

def get_interviews(request):
    interviews = Interview.objects.all()
    return {"interviews": interviews}