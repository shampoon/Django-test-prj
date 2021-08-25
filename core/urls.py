from django.urls import path

import core.views

app_name = 'core'

urlpatterns = [
    path('', core.views.index, name='people'),
    path('company/<int:pk>', core.views.company, name='company'),
    path('companies/', core.views.companies.as_view(), name='companies'),
]
