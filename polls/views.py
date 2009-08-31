from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")
    
def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)