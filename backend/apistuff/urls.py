from django.urls import path, include
from .views import Process, Sample, UpdateModel

urlpatterns = [
    path('accounts/', include("accounts.urls")),
    path('guess/', Process.as_view(), name='process'),
    path('provide-sample/', Sample.as_view()),
    path('update-model/', UpdateModel.as_view()),
]