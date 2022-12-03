from carhav.core.models import Interview, BootcampModel

def get_interviews(request):
    interviews = Interview.objects.all()
    return {"interviews": interviews}

def get_bootcamps(request):
    bootcamps = BootcampModel.objects.all()
    return {"bootcamp": bootcamps}