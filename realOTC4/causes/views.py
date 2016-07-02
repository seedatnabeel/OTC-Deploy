from django.http import HttpResponse
from django.shortcuts import render
import infermedica_api
from django.http import HttpResponseRedirect


infermedica_api.configure(app_id='945555e1', app_key='be2ee424c225c567086a084637a359de')

def index(request):
    api = infermedica_api.get_api()
    template = 'causes/index.html'
    response = HttpResponse("<h1>This is the causes page")
    debug = request.session['name']
    print(request.session['name'])
    print("we have this many:", len(debug))

    cause = infermedica_api.Diagnosis(sex='female', age=35)

    for x in range(0, len(debug)):
        cause.add_symptom(debug[x], 'present')

    cause = api.diagnosis(cause)


    first_cause=cause.conditions[0]['name']
    second_cause=cause.conditions[1]['name']
    third_cause=cause.conditions[2]['name']

    first_prob=cause.conditions[0]['probability']
    second_prob=cause.conditions[1]['probability']
    third_prob=cause.conditions[2]['probability']

    print(first_cause)
    print(first_prob*100)

##############################
    common_cold = 'http://otcsa.azurewebsites.net/list-of-illnesses/cold/'
    influenza = 'http://otcsa.azurewebsites.net/list-of-illnesses/influenza-flu/'


    if first_cause == "Common cold":
        first_cause1 = common_cold
    elif first_cause == "Influenza":
        first_cause1 = influenza
    elif first_cause == "Acute sinusitis":
        first_cause1 = acute_sinusitis

    context = {
        "first_cause": first_cause,
        "second_cause" : second_cause,
        "third_cause" : third_cause,
        "first_prob" : int(first_prob*100),
        "second_prob" : int(second_prob*100),
        "third_prob" : int(third_prob*100),
        "first_cause1": first_cause1
    }

    return render(request, "causes/index.html", context)

