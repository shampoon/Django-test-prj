from django.urls import path

import core.views

urlpatterns = [
    path('', core.views.index),
    path('company/<int:pk>', core.views.company),
]
