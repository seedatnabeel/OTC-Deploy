from django.http import  HttpResponse
from django.shortcuts import render
from .forms import PostForm

def index(request):
    form=PostForm(request.POST or None)
    context = {
        "form":form,
    }
    return render(request, "contact/post_form.html", context)


# def index(request):
#     template = 'contact/index.html'
#     return render(request, template)
#
# def create_user(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         comment= request.POST['comment']
