from django.urls import path

from reservations.views import ReservetionView

app_name = 'reservations'

urlpatterns = [
    path('reserve/', ReservetionView.as_view(), name='reserve')
]