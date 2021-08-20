from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
import core.models


def index(request):
    hum = core.models.Human.objects.all()
    return render(request, 'core/index.html', {'objects_list': hum})
