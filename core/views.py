from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Template, Context
import core.models


def index(request):
    hum = core.models.Human.objects.all()
    return render(request, 'core/index.html', {'objects_list': hum})


def company(request, pk):
    comp = get_object_or_404(core.models.Company, id=pk)
    return render(request, 'core/company_detail.html', {'object': comp})


def companies(request):
    comp = core.models.Company.objects.all()
    return render(request, 'core/company.html', {'objects_list': comp})
