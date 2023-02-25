from django.urls import path
from .views import Process, Sample, UpdateModel

urlpatterns = [
    path('guess/', Process.as_view(), name='process'),
    path('provide-sample/', Sample.as_view()),
    path('update-model/', UpdateModel.as_view())
]