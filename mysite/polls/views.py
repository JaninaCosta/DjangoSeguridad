from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello word")


def search_form(request):
    if 'start_date' in request.GET and 'end_date' in request.GET:
        query = "SELECT * from myapp_mymodel WHERE myapp_mymodel.date "\
                "BETWEEN '{} 00:00:00' AND '{} 23:59:59'".format(request.GET.get('start_date'),request.GET.get('end_date'))
        model_items = MyModel.objects.raw(query)
    else:
        model_items = MyModel.objects.all()
    return render(request, 'template.html', {'model_items': model_items})
