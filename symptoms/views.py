from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Symptoms
from .forms import PostForm
# from django.utils import encoding
from unidecode import unidecode


def index(request):

    # all_symptoms = Symptoms.objects.all()
    # context = {'all_symptoms' : all_symptoms,}
    print(request.method)
    # print(request)
    if (request.method == "POST"):
        debug = request.POST.getlist('checks[]')

            # print(next((item for item in request if item["probability"] >= "0.10")))
        # print(request['question'])

        #request.session['debug'] = debug
        request.session['name'] = debug

        return HttpResponseRedirect('/causes/')

    else:  # request.GET
        form = PostForm()

    context = {
        "form": form,
    }
    return render(request, "symptoms/post_form.html", context)


